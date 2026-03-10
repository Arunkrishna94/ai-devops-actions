Problem: No space left on device

Keywords:
no space left on device
disk full
docker build disk error
runner disk exhausted
npm install disk error

Root Cause:
The CI/CD runner ran out of available disk space during the build process.

Common Situations:
- Docker build layers consuming disk
- Large dependency installs (npm, pip, maven)
- Cached artifacts filling disk

Fix:
- Run docker system prune -af
- Remove unused containers and volumes
- Clean build workspace
- Increase disk size of CI runner