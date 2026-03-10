import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

log_data = """
Build failed
Connection refused to database
"""

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": "You are a DevOps expert."},
        {"role": "user", "content": f"Analyze this CI/CD failure:\n{log_data}"}
    ]
)

print(response.choices[0].message.content)
