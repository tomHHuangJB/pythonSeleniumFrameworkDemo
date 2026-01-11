import base64
import json
import os
import urllib.request


def _get_env(key: str, default: str = "") -> str:
    return os.getenv(key, default)


def base_url() -> str:
    return _get_env("JIRA_BASE_URL")


def user() -> str:
    return _get_env("JIRA_USER")


def token() -> str:
    return _get_env("JIRA_TOKEN")


def project_key() -> str:
    return _get_env("JIRA_PROJECT_KEY")


def issue_type() -> str:
    return _get_env("JIRA_ISSUE_TYPE", "Bug")


def enabled() -> bool:
    return bool(base_url() and project_key())


def create_issue(summary: str, description: str) -> bool:
    if not enabled():
        return False

    payload = {
        "fields": {
            "project": {"key": project_key()},
            "summary": summary,
            "description": description,
            "issuetype": {"name": issue_type()},
        }
    }
    data = json.dumps(payload).encode("utf-8")
    headers = {"Content-Type": "application/json"}
    auth = _basic_auth()
    if auth:
        headers["Authorization"] = auth

    request = urllib.request.Request(
        f"{base_url().rstrip('/')}/rest/api/2/issue",
        data=data,
        headers=headers,
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=10):
            return True
    except Exception:
        return False


def _basic_auth() -> str:
    if not user() or not token():
        return ""
    raw = f"{user()}:{token()}".encode("utf-8")
    return "Basic " + base64.b64encode(raw).decode("utf-8")
