```markdown
# Canary Engine

A lightweight, high-performance Multi-Tenant Feature Flag and Canary Deployment Engine built with FastAPI, SQLAlchemy, and SQLite. This system enables real-time feature toggling and deterministic user traffic allocation without database bloat, managed entirely through an interactive administrative control board.

## Features

- **Tenant Isolation Matrix:** Secure runtime segregation of feature flags across multiple distinct corporate environments.
- **Deterministic Canary Allocation:** High-efficiency hashing algorithm ensuring that test users are assigned consistently to rollout buckets (0-100%) with zero database state tracking.
- **Dynamic Simulation Rig:** An integrated 100x bulk traffic simulator built into the control board to visually verify rollout distribution models instantly.
- **Context Evaluation Guardrails:** Real-time request context matching (e.g., user tiers or geographic markers) during evaluation pipelines.

## Project Architecture

```text
canary_engine/
├── app/
│   ├── models/
│   │   ├── tenant.py
│   │   └── flag.py
│   ├── routers/
│   │   ├── tenants.py
│   │   └── flags.py
│   ├── schemas/
│   │   ├── tenant.py
│   │   └── flag.py
│   ├── services/
│   │   └── evaluator.py
│   ├── database.py
│   └── main.py
├── templates/
│   └── dashboard.html
├── .gitignore
├── requirements.txt
└── canary_engine.db

```

## Tech Stack

* **Backend Framework:** FastAPI (Python)
* **Asynchronous ORM:** SQLAlchemy with `aiosqlite`
* **Database Engine:** SQLite
* **Data Validation:** Pydantic v2
* **Administrative Interface:** HTML5, JavaScript (Fetch API), Tailwind CSS

## Installation and Setup

1. **Clone the Repository:**
```bash
git clone [https://github.com/rutush2/canary-engine.git](https://github.com/rutush2/canary-engine.git)
cd canary-engine

```


2. **Activate Your Virtual Environment:**
```powershell
# On Windows PowerShell
.\venv\Scripts\activate

```


3. **Install Core Dependencies:**
```bash
pip install -r requirements.txt

```


4. **Boot Up the Application Server:**
```bash
uvicorn app.main:app --reload

```


5. **Access the Application Workspace:**
* **Interactive Control Board Dashboard:** Open [http://127.0.0.1:8000/dashboard](http://127.0.0.1:8000/dashboard)
* **Interactive OpenAPI/Swagger Documentation:** Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)



## License

This project is open-source and available under the MIT License.

```

```