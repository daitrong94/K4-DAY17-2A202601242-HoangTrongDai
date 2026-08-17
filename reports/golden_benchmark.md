# Lab 17 Golden Set Report

- Implementation: `student`
- Kind: `golden`
- Cases: **20**
- Passed: **20/20**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **943.9 ms**
- Average token reduction vs full source context: **13.4%**
- Golden bonus: **10/10** (100% required)

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| G01 | short_term | PASS | 0.2 | 227 | 0.0% |  |
| G02 | short_term | PASS | 0.1 | 133 | 0.0% |  |
| G06 | long_term | PASS | 1664.7 | 760 | 0.0% |  |
| G09 | semantic | PASS | 218.5 | 155 | 66.2% |  |
| G10 | semantic | PASS | 212.0 | 100 | 78.2% |  |
| G14 | mixed | PASS | 1401.2 | 436 | 0.0% |  |
| G03 | long_term | PASS | 1266.7 | 1528 | 0.0% |  |
| G04 | long_term | PASS | 1233.9 | 1504 | 0.0% |  |
| G07 | episodic | PASS | 312.5 | 564 | 0.0% |  |
| G08 | episodic | PASS | 254.9 | 578 | 0.0% |  |
| G11 | mixed | PASS | 1369.4 | 444 | 21.4% |  |
| G13 | mixed | PASS | 465.8 | 413 | 26.9% |  |
| G15 | mixed | PASS | 1619.2 | 744 | 0.0% |  |
| G16 | mixed | PASS | 1386.3 | 492 | 12.9% |  |
| G17 | mixed | PASS | 1338.5 | 492 | 12.9% |  |
| G18 | mixed | PASS | 440.6 | 447 | 20.9% |  |
| G19 | mixed | PASS | 1350.0 | 581 | 0.0% |  |
| G05 | long_term | PASS | 1130.2 | 1537 | 0.0% |  |
| G12 | mixed | PASS | 1633.8 | 473 | 25.2% |  |
| G20 | mixed | PASS | 1578.6 | 614 | 2.9% |  |

## Evidence excerpts

### G01 - short_term

`<SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. | assistant: Noted staging constraint. | user: Filler A about button padding. | assistant: Filler A. | user: Filler B about color tokens. | assistant: Filler B. | user: Filler C about copy tone. | assistant: Filler C. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. - user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. - assistant: Noted staging constraint. </DURA`

### G02 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### G06 - long_term

`<USER_SUMMARY> The user's project is LOTUS-88. The user prioritizes Java and Spring Boot for backend examples and does not use Python for the backend. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-17 13:55:35     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Evaluation User" }: Minh la Lan, phap ly hoi gat truoc khi bat memory tren san pham. Viet hop dong ngan: backend minh dang dung ngon ngu/framework nao, va quy tac luu/xoa bo nho ca nhan trong lab yeu cau opt-in va verify ra sao? Chi stack cua Lan.   - Created At: 2026-08-01 11:0`

### G09 - semantic

`EPISODE: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. metadata= EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. metadata= EPISODE: Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodic 3 percent, semantic 3 percent; trim lower-priority memory first. Marker: BUDGET-10-4-3-3. metadata=`

### G10 - semantic

`EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. metadata= EPISODE: Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodic 3 percent, semantic 3 percent; trim lower-priority memory first. Marker: BUDGET-10-4-3-3. metadata=`

### G14 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's project is LOTUS-88. The user prioritizes Java and Spring Boot for backend examples and does not use Python for the backend. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-17 13:56:04     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Evaluation User" }: Lan uu tien stack backend nao cho LOTUS-88?   - Created At: 2026-08-01 11:00:20     Source: message     Content: Lab Assistant (assistant): Da hieu: LOTUS-88, Java + Spring Boot cho backend examples.   - Created At: 2026-08-01 11:00:00     Source:`

### G03 - long_term

`<USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer using Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. They are also working on a benchmark report, LAB-REPORT-1600, which is open-loop and due by Friday at 16:00. Currently, they are debugging an async HTTP process, investigating connection churn, connection pooling, client lifecycle, and concurrency. They have tried increasing the timeout to 60 seconds without success, and this issue is related to ASYNC-FIX-20. A suggested efficient approach is to reuse the aiohttp ClientSession and set concurrency to 20, which has been`

### G04 - long_term

`<USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer using Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. They are also working on a benchmark report, LAB-REPORT-1600, which is open-loop and due by Friday at 16:00. Currently, they are debugging an async HTTP process, investigating connection churn, connection pooling, client lifecycle, and concurrency. They have tried increasing the timeout to 60 seconds without success, and this issue is related to ASYNC-FIX-20. A suggested efficient approach is to reuse the aiohttp ClientSession and set concurrency to 20, which has been`

### G07 - episodic

`EPISODE: Minh sap giai thich coroutine cho ban, dong thoi can nhac policy retry payment vao vi du. Minh hoc kieu nao thi de nho? Va request retry payment phai mang header nao? Dung lay styl EPISODE: Backend cua BLUEBIRD-42 bat buoc dung stack gi? EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai time`

### G08 - episodic

`EPISODE: Minh sap giai thich coroutine cho ban, dong thoi can nhac policy retry payment vao vi du. Minh hoc kieu nao thi de nho? Va request retry payment phai mang header nao? Dung lay styl EPISODE: Hay chon huong dan code retry payment phu hop voi preference ca nhan cua Minh. EPISODE: Cuoi tuan minh ngoi mot minh lam demo rieng, khong hop team. Truoc khi chon template, nhac lai: khi lam viec ca nhan minh uu tien ngon ngu nao, va ma du an demo ca nhan la gi? Chi  EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai `

### G11 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer using Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. They are also working on a benchmark report, LAB-REPORT-1600, which is open-loop and due by Friday at 16:00. Currently, they are debugging an async HTTP process, investigating connection churn, connection pooling, client lifecycle, and concurrency. They have tried increasing the timeout to 60 seconds without success, and this issue is related to ASYNC-FIX-20. A suggested efficient approach is to reuse the aiohttp ClientSession and set concurrency to 20, wh`

### G13 - mixed

`<EPISODIC> EPISODE: Minh sap giai thich coroutine cho ban, dong thoi can nhac policy retry payment vao vi du. Minh hoc kieu nao thi de nho? Va request retry payment phai mang header nao? Dung lay styl EPISODE: Hay chon huong dan code retry payment phu hop voi preference ca nhan cua Minh. EPISODE: Cuoi tuan minh ngoi mot minh lam demo rieng, khong hop team. Truoc khi chon template, nhac lai: khi lam viec ca nhan minh uu tien ngon ngu nao, va ma du an demo ca nhan la gi? Chi  EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: C`

### G15 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer using Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. They are also working on a benchmark report, LAB-REPORT-1600, which is open-loop and due by Friday at 16:00. Currently, they are debugging an async HTTP process, investigating connection churn, connection pooling, client lifecycle, and concurrency. They have tried increasing the timeout to 60 seconds without success, and this issue is related to ASYNC-FIX-20. A suggested efficient approach is to reuse the aiohttp ClientSession and set concurrency to 20, wh`

### G16 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer using Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. They are also working on a benchmark report, LAB-REPORT-1600, which is open-loop and due by Friday at 16:00. Currently, they are debugging an async HTTP process, investigating connection churn, connection pooling, client lifecycle, and concurrency. They have tried increasing the timeout to 60 seconds without success, and this issue is related to ASYNC-FIX-20. A suggested efficient approach is to reuse the aiohttp ClientSession and set concurrency to 20, wh`

### G17 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer using Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. They are also working on a benchmark report, LAB-REPORT-1600, which is open-loop and due by Friday at 16:00. Currently, they are debugging an async HTTP process, investigating connection churn, connection pooling, client lifecycle, and concurrency. They have tried increasing the timeout to 60 seconds without success, and this issue is related to ASYNC-FIX-20. A suggested efficient approach is to reuse the aiohttp ClientSession and set concurrency to 20, wh`

### G18 - mixed

`<EPISODIC> EPISODE: Cuoi tuan minh ngoi mot minh lam demo rieng, khong hop team. Truoc khi chon template, nhac lai: khi lam viec ca nhan minh uu tien ngon ngu nao, va ma du an demo ca nhan la gi? Chi  EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. EPISODE: Toi se uu tien timeline khi giai thich coroutine va Task. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hay kiem tra connection pool, lifecycle cua client va concurrency. EPISODE: Cach hieu qua la reuse aiohttp Cli`

### G19 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer using Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. They are also working on a benchmark report, LAB-REPORT-1600, which is open-loop and due by Friday at 16:00. Currently, they are debugging an async HTTP process, investigating connection churn, connection pooling, client lifecycle, and concurrency. They have tried increasing the timeout to 60 seconds without success, and this issue is related to ASYNC-FIX-20. A suggested efficient approach is to reuse the aiohttp ClientSession and set concurrency to 20, wh`

### G05 - long_term

`<USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer using Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. They are also working on a benchmark report, LAB-REPORT-1600, which is open-loop and due by Friday at 16:00. Currently, they are debugging an async HTTP process, investigating connection churn, connection pooling, client lifecycle, and concurrency. They have tried increasing the timeout to 60 seconds without success, and this issue is related to ASYNC-FIX-20. A suggested efficient approach is to reuse the aiohttp ClientSession and set concurrency to 20, which has been`

### G12 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer using Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. They are also working on a benchmark report, LAB-REPORT-1600, which is open-loop and due by Friday at 16:00. Currently, they are debugging an async HTTP process, investigating connection churn, connection pooling, client lifecycle, and concurrency. They have tried increasing the timeout to 60 seconds without success, and this issue is related to ASYNC-FIX-20. A suggested efficient approach is to reuse the aiohttp ClientSession and set concurrency to 20, wh`

### G20 - mixed

`<SHORT_TERM> <SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Filler about dashboard widgets. | assistant: Filler. | user: Filler about CSS variables. | assistant: Filler. | user: Filler about copy review. | assistant: Filler. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. </DURABLE_NOTES> <RECENT_TURNS> user: Filler about empty charts. assistant: Filler. user: Filler about telemetry. assistant: Filler. user: Filler about a11y labels. assistant: Filler. </RECENT_TURNS> </SHORT_TERM>`
