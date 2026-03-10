import os
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

Below is a knowledge base of CI/CD failures:

{knowledge}

Now analyze this CI/CD log:

{log_data}

Provide:
1. Root cause
2. Suggested fix
3. Whether it matches a known failure pattern
"""

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": "You are a DevOps expert helping debug CI pipelines."},
        {"role": "user", "content": prompt}
    ]
)

print("====== AI ANALYSIS ======")
print(response.choices[0].message.content)
