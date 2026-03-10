import os
import requests
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

# Load CI logs
with open("logs/sample-log.txt", "r") as f:
    log_data = f.read()

# Load knowledge base
knowledge = ""

for file in os.listdir("knowledge-base"):
    path = f"knowledge-base/{file}"
    with open(path, "r") as f:
        knowledge += f.read() + "\n\n"

prompt = f"""
You are a Senior DevOps engineer.

Below is a knowledge base of CI/CD failure patterns.

Knowledge Base:
{knowledge}

CI/CD Log:
{log_data}

Tasks:
1. Identify the root cause.
2. Suggest the fix.
3. If the issue matches ANY knowledge base problem, explicitly say which one.
4. If it does not match, say "New failure pattern".
"""

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": "You are a DevOps expert helping debug CI pipelines."},
        {"role": "user", "content": prompt}
    ]
)

analysis = response.choices[0].message.content

print("====== AI ANALYSIS ======")
print(analysis)

# Post comment to PR
repo = os.environ.get("GITHUB_REPOSITORY")
token = os.environ.get("GITHUB_TOKEN")
pr_number = os.environ.get("PR_NUMBER")

if pr_number:
    url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"

    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json"
    }

    body = {
        "body": f"🤖 **AI CI Failure Analysis**\n\n{analysis}"
    }

    requests.post(url, json=body, headers=headers)