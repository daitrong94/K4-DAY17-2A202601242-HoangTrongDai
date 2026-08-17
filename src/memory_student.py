from __future__ import annotations

import json
from types import SimpleNamespace
from typing import Any

from .config import settings
from .context_budget import ContextBudgetManager
from .utils import cap_query, join_nonempty
from .zep_common import prime_eval_thread, render_graph_search


class StudentMemory:
    """Only this file needs to be edited by students."""

    def __init__(self, client: Any):
        self.client = client
        self.budget = ContextBudgetManager(settings.context_tokens)

    # NOTE: Zep rejects graph.search queries longer than 400 characters. Some
    # eval queries are longer than that, so wrap every query with
    # `cap_query(query)` (see src/utils.py) before passing it to graph.search.

    def retrieve_long_term(self, user_id: str, thread_id: str, query: str) -> str:
        # LAB TODO 1/4
        # 1) prime_eval_thread(...) has already been provided as scaffolding.
        # 2) call thread.get_user_context(thread_id=...)
        # 3) return the .context string.
        # Bonus: append graph.search(scope="edges", limit>=20) facts with
        #        validity ranges (a low limit can miss deadline/open-loop facts).
        prime_eval_thread(self.client, user_id, thread_id, query)
        user_context = self.client.thread.get_user_context(thread_id=thread_id)
        context_block = getattr(user_context, "context", "") or ""

        try:
            facts = self.client.graph.search(
                user_id=user_id,
                query=cap_query(query),
                scope="edges",
                limit=20,
            )
            fact_text = render_graph_search(facts)
        except Exception:
            fact_text = ""
        return join_nonempty([context_block, fact_text], sep="\n\n")

    def retrieve_episodic(self, user_id: str, query: str) -> str:
        # LAB TODO 2/4
        # Use client.graph.search(user_id=..., query=cap_query(query),
        #     scope="episodes", limit=...) then render_graph_search(...).
        # Tip: verbose session episodes can crowd out concise, marker-bearing
        # reflections under the tight episodic budget — render_graph_search
        # accepts an `episode_char_cap` to keep more distinct episodes.
        results = self.client.graph.search(
            user_id=user_id,
            query=cap_query(query),
            scope="episodes",
            limit=15,
        )
        return render_graph_search(results, episode_char_cap=180)

    def retrieve_semantic(self, graph_id: str, query: str) -> str:
        # LAB TODO 3/4
        # Search the standalone graph (graph_id, NOT user_id).
        # Recommended: scope="episodes" — it returns raw document text that keeps
        # literal markers (e.g. PAYMENT-RULE-3). The "auto" scope returns
        # extracted facts that DROP those literal codes, so avoid it here.
        # Fallback: scope="nodes".
        q = cap_query(query)
        try:
            results = self.client.graph.search(
                graph_id=graph_id,
                query=q,
                scope="episodes",
                limit=12,
            )
        except Exception:
            results = self.client.graph.search(
                graph_id=graph_id,
                query=q,
                scope="nodes",
                limit=12,
            )
        # Each KB doc is ingested twice (verbose JSON blob + compact summary
        # text, see add_semantic_documents). For mixed queries that touch two
        # different KB docs, the verbose duplicate can eat the whole semantic
        # token budget and push a later, still-relevant doc's marker past the
        # trim cutoff. Dedupe by doc id, keeping the shorter (text) representation
        # so more distinct markers survive the 3% budget. The compact text
        # episode isn't valid JSON itself, so first map summary text -> id from
        # the JSON episodes, then match text episodes against that map.
        episodes = getattr(results, "episodes", None) or []
        if episodes:
            id_by_summary: dict[str, str] = {}
            for ep in episodes:
                content = getattr(ep, "content", "") or ""
                try:
                    parsed = json.loads(content)
                except (ValueError, TypeError):
                    continue
                if isinstance(parsed, dict) and parsed.get("id") and parsed.get("summary"):
                    id_by_summary[parsed["summary"]] = parsed["id"]

            best_by_id: dict[str, Any] = {}
            for ep in episodes:
                content = getattr(ep, "content", "") or ""
                doc_id = content
                try:
                    parsed = json.loads(content)
                    if isinstance(parsed, dict) and parsed.get("id"):
                        doc_id = parsed["id"]
                except (ValueError, TypeError):
                    if content in id_by_summary:
                        doc_id = id_by_summary[content]
                current = best_by_id.get(doc_id)
                if current is None or len(content) < len(getattr(current, "content", "") or ""):
                    best_by_id[doc_id] = ep
            # results is a frozen pydantic model (can't reassign .episodes in
            # place), so pass a plain namespace copy with the deduped list.
            results = SimpleNamespace(
                context=getattr(results, "context", None),
                edges=getattr(results, "edges", None),
                episodes=list(best_by_id.values()),
                nodes=getattr(results, "nodes", None),
                observations=getattr(results, "observations", None),
                thread_summaries=getattr(results, "thread_summaries", None),
            )
        return render_graph_search(results)

    def assemble_context(self, layers: dict[str, str]) -> tuple[str, dict[str, dict[str, int]]]:
        # LAB TODO 4/4
        # Use ContextBudgetManager to enforce 10/4/3/3 budget and priority order.
        return self.budget.assemble(layers)
