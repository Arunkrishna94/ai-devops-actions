# AI DevOps Debugger

An AI-powered DevOps assistant that analyzes CI/CD pipeline logs and explains the root cause of failures.

This project demonstrates how AI can help DevOps engineers automatically debug build and deployment failures.

---

## Project Overview

When a CI/CD pipeline fails, engineers usually spend time reading logs to find the root cause.

This project automates that process using AI.

Workflow:

CI/CD logs → AI analysis → Root cause explanation

The script reads pipeline logs and asks an AI model to analyze them like a DevOps expert.

---

## Project Structure

```
ai-devops-actions/
│
├── scripts/
│   └── ai-debugger.py
│
├── logs.txt
├── .gitignore
└── README.md
```

---

## Prerequisites

Make sure you have:

* Python 3.9 or later
* pip installed
* An OpenAI API key

Install Python if needed.

---

## Step 1: Clone the Repository

```
git clone https://github.com/Arunkrishna94/ai-devops-actions.git
cd ai-devops-actions
```

---

## Step 2: Create a Virtual Environment (Recommended)

```
python -m venv venv
```

Activate it:

Mac/Linux

```
source venv/bin/activate
```

Windows

```
venv\Scripts\activate
```

---

## Step 3: Install Dependencies

```
pip install openai
```

---

## Step 4: Set Your API Key

Set the environment variable.

Mac/Linux

```
export OPENAI_API_KEY="your-api-key"
```

Windows

```
set OPENAI_API_KEY=your-api-key
```

---

## Step 5: Create a Sample Log File

Create a file called `logs.txt`.

Example:

```
ERROR: Connection refused to database
Service postgres not available
Build failed during integration tests
```

This simulates a CI/CD pipeline failure.

---

## Step 6: Run the AI Debugger

Execute the script:

```
python scripts/ai-debugger.py
```

The AI will analyze the log and produce a root cause explanation.

Example output:

```
Possible Cause:
Database service is not running.

Suggested Fix:
Ensure the database container is started before the application connects.
```

---

## Example Script

```
import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

log_data = open("logs.txt").read()

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": "You are a DevOps expert."},
        {"role": "user", "content": f"Analyze this CI/CD failure log:\n{log_data}"}
    ]
)

print(response.choices[0].message.content)
```

---

## Future Improvements

Possible improvements for this project:

* Automatically capture CI logs from GitHub Actions
* Post AI debugging comments on Pull Requests
* Detect common DevOps issues (Docker, Kubernetes, Terraform)
* Add automated remediation suggestions

---

## Use Case

This project demonstrates how AI can assist DevOps teams in:

* CI/CD troubleshooting
* Faster incident response
* Automated root cause analysis

---

## Author

Arun Krishna

DevOps Engineer exploring AI-powered infrastructure automation.

