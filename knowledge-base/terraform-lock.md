Problem: Terraform state lock

Error:
Error acquiring the state lock

Root Cause:
Another Terraform process running.

Fix:
terraform force-unlock
Check CI pipeline concurrency
