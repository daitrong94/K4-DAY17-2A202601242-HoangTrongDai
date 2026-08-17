# Lab 17 Benchmark Report

- Implementation: `student`
- Kind: `practice`
- Cases: **11**
- Passed: **11/11**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **618.6 ms**
- Average token reduction vs full source context: **19.0%**

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| E01 | short_term | PASS | 0.0 | 133 | 0.0% |  |
| E06 | semantic | PASS | 310.0 | 56 | 87.8% |  |
| E09 | long_term | PASS | 1146.3 | 787 | 0.0% |  |
| E10 | short_term | PASS | 0.3 | 195 | 0.0% |  |
| E02 | long_term | PASS | 1170.1 | 1518 | 0.0% |  |
| E03 | long_term | PASS | 1123.1 | 1485 | 0.0% |  |
| E04 | episodic | PASS | 213.1 | 587 | 0.0% |  |
| E05 | episodic | PASS | 224.1 | 596 | 0.0% |  |
| E07 | mixed | PASS | 1310.2 | 392 | 30.6% |  |
| E11 | semantic | PASS | 204.9 | 55 | 90.3% |  |
| E08 | long_term | PASS | 1102.2 | 1514 | 0.0% |  |

## Evidence excerpts

### E01 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### E06 - semantic

`EPISODE: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. metadata=`

### E09 - long_term

`<USER_SUMMARY> The user's project is LOTUS-88. The user prioritizes Java and Spring Boot for backend examples and does not use Python for the backend. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-01 11:00:20     Source: message     Content: Lab Assistant (assistant): Da hieu: LOTUS-88, Java + Spring Boot cho backend examples.   - Created At: 2026-08-01 11:00:00     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Lan Tran" }: Toi la Lan. Du an cua toi la LOTUS-88. Toi uu tien Java va Spring Boot, va khong dung Python trong vi du backe`

### E10 - short_term

`<SESSION_SUMMARY> user: Constraint: REVIEW-DEADLINE-1600 - project review is Friday at 16:00 and must not be forgotten. | assistant: Acknowledged review constraint. | user: Filler turn 1 about UI spacing. | assistant: Filler answer 1. | user: Filler turn 2 about naming. | assistant: Filler answer 2. | user: Filler turn 3 about logging. | assistant: Filler answer 3. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint: REVIEW-DEADLINE-1600 - project review is Friday at 16:00 and must not be forgotten. - assistant: Acknowledged review constraint. </DURABLE_NOTES> <RECENT_TURNS> user: Filler turn 4 about tests. assistant: Filler answer 4. user: Filler turn 5 about docs. assistant: Filler answe`

### E02 - long_term

`<USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer using Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. They are also working on a benchmark report, LAB-REPORT-1600, which is open-loop and due by Friday at 16:00. Currently, they are debugging an async HTTP process, investigating connection churn, connection pooling, client lifecycle, and concurrency. They have tried increasing the timeout to 60 seconds without success, and this issue is related to ASYNC-FIX-20. A suggested efficient approach is to reuse the aiohttp ClientSession and set concurrency to 20, which has been`

### E03 - long_term

`<USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer using Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. They are also working on a benchmark report, LAB-REPORT-1600, which is open-loop and due by Friday at 16:00. Currently, they are debugging an async HTTP process, investigating connection churn, connection pooling, client lifecycle, and concurrency. They have tried increasing the timeout to 60 seconds without success, and this issue is related to ASYNC-FIX-20. A suggested efficient approach is to reuse the aiohttp ClientSession and set concurrency to 20, which has been`

### E04 - episodic

`EPISODE: Minh sap giai thich coroutine cho ban, dong thoi can nhac policy retry payment vao vi du. Minh hoc kieu nao thi de nho? Va request retry payment phai mang header nao? Dung lay styl EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Cuoi tuan minh ngoi mot minh lam demo rieng, khong hop team. Truoc khi chon template, nhac lai: khi lam viec ca nhan minh uu tien ngon ngu nao, va ma du an demo ca nhan la gi? Chi  EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00.`

### E05 - episodic

`EPISODE: Minh sap giai thich coroutine cho ban, dong thoi can nhac policy retry payment vao vi du. Minh hoc kieu nao thi de nho? Va request retry payment phai mang header nao? Dung lay styl EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Cuoi tuan minh ngoi mot minh lam demo rieng, khong hop team. Truoc khi chon template, nhac lai: khi lam viec ca nhan minh uu tien ngon ngu nao, va ma du an demo ca nhan la gi? Chi  EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EP`

### E07 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer using Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. They are also working on a benchmark report, LAB-REPORT-1600, which is open-loop and due by Friday at 16:00. Currently, they are debugging an async HTTP process, investigating connection churn, connection pooling, client lifecycle, and concurrency. They have tried increasing the timeout to 60 seconds without success, and this issue is related to ASYNC-FIX-20. A suggested efficient approach is to reuse the aiohttp ClientSession and set concurrency to 20, wh`

### E11 - semantic

`EPISODE: When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST. metadata=`

### E08 - long_term

`<USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer using Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. They are also working on a benchmark report, LAB-REPORT-1600, which is open-loop and due by Friday at 16:00. Currently, they are debugging an async HTTP process, investigating connection churn, connection pooling, client lifecycle, and concurrency. They have tried increasing the timeout to 60 seconds without success, and this issue is related to ASYNC-FIX-20. A suggested efficient approach is to reuse the aiohttp ClientSession and set concurrency to 20, which has been`
