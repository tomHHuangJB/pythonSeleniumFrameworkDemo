# Python Selenium Framework Demo

A pytest + Selenium 4 demo framework targeting LocalAutomationApp.

## Prereqs
- Python 3.10+
- LocalAutomationApp running on http://localhost:5173

## LocalAutomationApp Setup
This repo expects LocalAutomationApp at `../../LocalAutomationApp` (see `.env`).

```bash
cd /Users/tomhuang/prog
git clone <LocalAutomationApp repo URL> LocalAutomationApp
cd LocalAutomationApp
docker compose --profile stable up -d --build
```

Confirm the app is up:
- Frontend: `http://localhost:5173`
- API: `http://localhost:3001/health`

## Install
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run
```bash
pytest -q --base-url=http://localhost:5173 --browser=chrome --headless=false
```

## CI (Local Jenkins)
This repo ships a local Jenkins setup via Docker Compose.

Defaults are in `.env` for first-time users. Use `.env.example` as a starting point if you want to customize.

1) Start Jenkins + Selenium:
```bash
docker compose -f docker-compose.jenkins.yml up -d --build
```

To also start LocalAutomationApp from this repo, use the `app` profile:
```bash
docker compose -f docker-compose.jenkins.yml --profile app up -d --build
```

2) Unlock Jenkins:
```bash
docker exec python-selenium-jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

3) Create a Pipeline job:
- Pipeline from SCM, repository path = this repo
- Script path: `Jenkinsfile`
- For local Jenkins in Docker, use repo URL `file:///opt/python-repo` (mounted by `docker-compose.jenkins.yml`).

First run checklist:
- Install suggested plugins (Git, Pipeline, JUnit, Docker).
- Create the Pipeline job.
- Start LocalAutomationApp (host or `--profile app`).
- Run the job with `USE_APP_PROFILE=true` if using the app profile.

Notes:
- Jenkins UI runs on `http://localhost:9082`.
- When using the `app` profile, set `BASE_URL` to `http://local-frontend:5173`.
- If you're running LocalAutomationApp on the host, keep `BASE_URL` as `http://host.docker.internal:5173`.
- In Jenkins, you can toggle `USE_APP_PROFILE` to auto-set `BASE_URL` to `http://local-frontend:5173`.
- Local SCM uses a mounted repo at `file:///opt/python-repo`, with local checkout enabled in `docker-compose.jenkins.yml`.

## Troubleshooting
- `host.docker.internal` not resolving: set `BASE_URL` to your host IP (e.g. `http://192.168.1.10:5173`) or use the `app` profile.
- Wrong LocalAutomationApp path: update `LOCAL_AUTOMATION_APP_DIR` in `.env`.
- Port conflicts: change `JENKINS_HTTP_PORT` or `SELENIUM_PORT` in `.env`.

## Layout
- `src/utils`: driver factory, config, waits
- `src/pages`: page objects
- `src/tests`: UI tests
- `resources`: fixture files

## Jira Integration (Optional, Local Docker)
If you want to run Jira locally for demos:

1) Start Jira + Postgres:
```bash
docker compose -f docker-compose.jira.yml up -d
```

Useful commands:
```bash
docker compose -f docker-compose.jira.yml logs -f
docker compose -f docker-compose.jira.yml ps
docker compose -f docker-compose.jira.yml stop
docker compose -f docker-compose.jira.yml down
```

2) Complete Jira setup in browser:
- Visit `http://localhost:8080`
- Choose **I'll set it up myself**
- Database: use the built-in database if you just need a local demo
- Application Title: `Local Jira (CI)`
- Mode: **Private**
- Base URL: `http://localhost:8080`
- License: generate a trial key from MyAtlassian and paste it in
- Create an admin user
- Create a project with key `DEMO` (or your preferred key)

3) Export Jira environment variables before running tests:
```bash
export JIRA_BASE_URL=http://localhost:8080
export JIRA_USER=admin
export JIRA_TOKEN=admin
export JIRA_PROJECT_KEY=DEMO
export JIRA_ISSUE_TYPE=Bug
```

4) Run tests (will file Jira issues on failures):
```bash
pytest -q --base-url=http://localhost:5173 --browser=chrome --headless=false
```

Note: The Jira hook is **demo-only**. In production, failures should be deduplicated and sanitized.
