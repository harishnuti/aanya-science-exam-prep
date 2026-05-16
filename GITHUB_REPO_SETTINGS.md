# 🔧 GITHUB REPOSITORY SETTINGS - Phase 2 v4.0

**Date**: May 16, 2026  
**Repository**: https://github.com/harishnuti/aanya-science-exam-prep  
**Status**: Production Ready  
**Branch**: main (protected)

---

## 📋 TABLE OF CONTENTS

1. [Repository Overview](#repository-overview)
2. [Current Configuration](#current-configuration)
3. [Branch Settings](#branch-settings)
4. [Collaborators & Permissions](#collaborators--permissions)
5. [Secrets & Environment Variables](#secrets--environment-variables)
6. [Webhooks & Integrations](#webhooks--integrations)
7. [Actions & CI/CD](#actions--cicd)
8. [Protection Rules](#protection-rules)
9. [Tags & Releases](#tags--releases)
10. [GitHub Actions Workflows](#github-actions-workflows)

---

## 📊 REPOSITORY OVERVIEW

**Repository Details**:
- **URL**: https://github.com/harishnuti/aanya-science-exam-prep
- **Owner**: harishnuti
- **Type**: Public (code visible) / Private (configure as needed)
- **Description**: Aanya's Science Exam Prep App - Phase 2 v4.0
- **Language**: Python 3.14
- **Framework**: Streamlit
- **License**: (Configure based on preference)

**Repository Statistics**:
```
Total Commits: 50+
Total Branches: 1 (main)
Total Releases: 1 (v4.0)
Code Size: ~5 MB (without PDFs)
Repository Size: ~120 MB (with PDFs, git-ignored)
Last Update: May 16, 2026
```

**Key Files at Root**:
```
streamlit_app.py          (Main entry point for Streamlit Cloud)
app_exam_prep_pro.py      (Backward compatibility wrapper)
requirements.txt          (All Python dependencies)
.gitignore               (Exclusion rules)
README.md                (Project overview)
```

---

## ⚙️ CURRENT CONFIGURATION

### Repository Type

**Recommended Settings** (adjust based on privacy needs):

**Option 1: Public Repository** (Current)
- ✅ Anyone can view code
- ✅ Better for educational projects
- ✅ GitHub pages can be enabled
- ⚠️ Secrets must be protected via GitHub Secrets
- **Use if**: Sharing with community, open-source project

**Option 2: Private Repository**
- ✅ Only you and collaborators can view
- ✅ Better for proprietary code
- ✅ Still requires GitHub Secrets for sensitive data
- ⚠️ Collaborators need to be invited
- **Use if**: Commercial product, want privacy

**To Change**:
1. Go to https://github.com/harishnuti/aanya-science-exam-prep/settings
2. Scroll to "Repository Visibility"
3. Click "Change visibility"
4. Select Public or Private
5. Confirm

### Default Branch

**Current**: `main`

**To Verify/Change**:
1. Settings → Branches
2. "Default branch" section
3. Select `main`
4. Click "Update"

---

## 🌳 BRANCH SETTINGS

### Branch Protection Rules

**Current Setup**: `main` branch protection recommended

**To Enable**:

1. Go to Settings → Branches
2. Click "Add rule"
3. Fill in pattern: `main`
4. Enable protections:

#### Protection Rule Configuration

```
Branch name pattern: main

✅ Require pull request reviews before merging
   - Required number of reviews before merge: 1
   - Dismiss stale pull request approvals: Checked
   - Require review from code owners: Unchecked (unless CODEOWNERS file)

✅ Require status checks to pass before merging
   - Require branches to be up to date before merging: Checked
   - (Optional) Require passing builds before merge

✅ Restrict who can push to matching branches
   - Allow force pushes: Unchecked (prevents accidental overwrites)
   - Allow deletions: Unchecked (prevents branch deletion)

✅ Require signed commits
   - Unchecked (optional, more secure)

✅ Require linear history
   - Unchecked (allows merge commits, rebase allows history rewriting)

✅ Include administrators
   - Checked (applies rules to repository owner too)
```

### Active Branches

**Current Active Branches**:
```
main (production)  - Latest stable v4.0
   └── Always points to latest working version
       - All changes tested before merge
       - Auto-deploys to Streamlit Cloud on push
       - Never broken, always live-ready
```

**Archived Branches** (if any):
```
None currently - all development on main
```

**To View All Branches**:
```bash
git branch -a
# Shows: * main (current)
```

---

## 👥 COLLABORATORS & PERMISSIONS

### Current Collaborators

**Owner**: harishnuti
- ✅ Full administrative access
- ✅ Can push, delete, manage settings
- ✅ Can manage secrets and deployments
- ✅ Can manage collaborators

### Adding Collaborators

**To add a team member**:

1. Go to Settings → Collaborators and teams
2. Click "Add people"
3. Enter GitHub username (e.g., `aanyadev`)
4. Select permission level:

**Permission Levels**:

| Role | Permissions | Use Case |
|------|-------------|----------|
| **Pull** | Read-only | Viewers, testers |
| **Triage** | Pull + label, close issues | Community maintainers |
| **Push** | Pull + Push | Active developers |
| **Maintain** | Push + manage releases/branches | Project leads |
| **Admin** | All permissions | Repository owner |

**Recommended Setup for This Project**:
- Owner: `harishnuti` (Admin)
- Teachers/Testers: `pull` (view-only)
- Future Developers: `push` (can commit)

### Managing Access

**To change collaborator permissions**:
1. Settings → Collaborators → Find person
2. Click the role dropdown
3. Select new role
4. Confirm

**To remove collaborator**:
1. Settings → Collaborators → Find person
2. Click the three dots (...)
3. Select "Remove access"
4. Confirm

---

## 🔐 SECRETS & ENVIRONMENT VARIABLES

### Using GitHub Secrets

**Secrets** are encrypted values for sensitive data (passwords, API keys, tokens).

**Never commit secrets** to git - use GitHub Secrets instead.

### Adding Secrets

**Via GitHub Web Interface**:
1. Go to Settings → Secrets and variables → Actions
2. Click "New repository secret"
3. Name: `ADMIN_PASSWORD`
4. Value: `admin123` (or whatever your secret is)
5. Click "Add secret"

**Secrets for This Project**:

```
ADMIN_PASSWORD = "admin123"

# If using external services (future):
DATABASE_URL = "your_external_db_url"
API_KEY = "your_api_key"
SMTP_PASSWORD = "email_password"  (if sending emails)
```

### Using Secrets in GitHub Actions

Secrets are automatically available in GitHub Actions workflows:

```yaml
- name: Deploy to Streamlit Cloud
  env:
    ADMIN_PASSWORD: ${{ secrets.ADMIN_PASSWORD }}
  run: |
    # Use secret in command
    echo "Deploying with admin security..."
```

### Using Secrets in Application Code

For local development, create `.streamlit/secrets.toml`:

```toml
# .streamlit/secrets.toml (NEVER COMMIT THIS)
admin_password = "admin123"
```

Then access in code:
```python
import streamlit as st
admin_pwd = st.secrets.get("admin_password", "admin123")
```

**IMPORTANT**: Add to `.gitignore`:
```
.streamlit/secrets.toml
```

### Environment Variables vs Secrets

**Environment Variables** (in .env files):
- For non-sensitive configuration
- Development-specific settings
- Committed to git (if not sensitive)
- Example: `DEBUG_MODE=true`, `LOG_LEVEL=INFO`

**Secrets** (via GitHub Secrets):
- For sensitive data only
- Passwords, API keys, tokens
- NOT committed to git
- Encrypted in GitHub
- Example: `ADMIN_PASSWORD`, `DATABASE_URL`

---

## 🪝 WEBHOOKS & INTEGRATIONS

### Streamlit Cloud Webhook

**Status**: ✅ Configured (auto-created by Streamlit Cloud)

**Purpose**: Triggers app redeployment when you push to GitHub

**To Verify**:
1. Settings → Webhooks
2. Should see webhook for Streamlit Cloud
3. URL format: `https://api.streamlit.cloud/deploy/...`

**Test Webhook**:
1. Make a small commit and push to main
2. Streamlit Cloud should automatically detect change
3. App redeployment starts (1-3 minutes)
4. Visit app URL to verify update

### Webhook Configuration

**Delivery events**:
- ✅ Push events (main trigger for redeployment)
- ✅ Pull request events (optional)
- ✅ Repository events (optional)

**To Configure**:
1. Settings → Webhooks → Find Streamlit webhook
2. Click "Edit"
3. Check "Let me select individual events"
4. Select desired events
5. Click "Update webhook"

### Other Integrations

**GitHub Pages** (Optional):
- For project documentation website
- Configure in Settings → Pages
- Source: Deploy from a branch (`main` or `gh-pages`)

**GitHub Apps**:
- Dependabot (dependency updates) - Recommended
- CodeQL (security scanning) - Recommended
- Snyk (vulnerability scanning) - Optional

**To Enable Dependabot**:
1. Settings → Code security and analysis
2. Click "Enable" for Dependabot
3. Creates PRs for dependency updates

---

## ⚙️ ACTIONS & CI/CD

### GitHub Actions Workflows

**Current Status**: No custom workflows configured (not required for this project)

**Optional Workflows to Add** (for future enhancement):

#### Workflow 1: Run Tests on Push

**File**: `.github/workflows/test.yml`

```yaml
name: Run Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: 3.11
      - run: pip install -r requirements.txt
      - run: pytest tests/  # If tests exist
      - run: streamlit run streamlit_app.py --headless  # Verify app loads
```

#### Workflow 2: Code Quality Check

**File**: `.github/workflows/lint.yml`

```yaml
name: Lint Code

on: [push]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
      - run: pip install flake8 black
      - run: flake8 apps/ src/  # Check code style
      - run: black --check apps/ src/  # Check formatting
```

### Enabling Actions

**To verify Actions are enabled**:
1. Go to Settings → Actions → General
2. Under "Policies", select "Allow all actions and reusable workflows"
3. Allow local workflows
4. Save

---

## 🛡️ PROTECTION RULES

### Branch Protection Rule Details

**For `main` branch**, recommended configuration:

| Rule | Setting | Reason |
|------|---------|--------|
| **Require pull request reviews** | 1 approval | Catch issues before merge |
| **Dismiss stale reviews** | Checked | Reviews outdated by new commits require re-approval |
| **Require status checks** | Checked | Ensures tests/builds pass |
| **Require up-to-date branches** | Checked | Prevents merge conflicts |
| **Include administrators** | Checked | Rules apply to everyone |
| **Force pushes** | Disable | Prevents history rewriting |
| **Deletions** | Disable | Prevents branch deletion |
| **Signed commits** | Optional | Extra security, requires GPG key |
| **Linear history** | Optional | Cleaner commit history |

### Creating Protection Rule

**Step-by-step**:
1. Settings → Branches
2. Click "Add rule"
3. Branch name pattern: `main`
4. Check all recommended protections above
5. Click "Create"

### Bypassing Protections (Emergency Only)

**If main branch is broken**:
1. Push to temporary branch (e.g., `hotfix`)
2. Fix the issue
3. Create pull request
4. Request emergency review
5. Merge to main
6. Monitor for immediate issues

---

## 🏷️ TAGS & RELEASES

### Current Release

**Latest Release**: v4.0 (May 16, 2026)

**To Create a Release**:

1. Go to Releases (on main GitHub page)
2. Click "Create a new release"
3. Fill in:
   - **Tag version**: `v4.0` (format: `vX.Y.Z`)
   - **Release title**: `Phase 2 v4.0 - Complete & Production Ready`
   - **Description**:
     ```
     Phase 2 v4.0 Master App - Final Freeze
     
     ✅ Features Complete
     - Multi-user support with SQLite database
     - 6 complete chapters with learning content
     - Gamification system (XP, levels, streaks, achievements)
     - 45-minute mock exam (PSLE format)
     - Brain drainer challenge mode (228+ questions)
     - Admin dashboard
     - Comprehensive documentation
     
     ✅ Deployment Status
     - Live at https://aanya-science-exam-prep.streamlit.app/
     - GitHub: https://github.com/harishnuti/aanya-science-exam-prep
     
     🔒 Frozen for Testing
     - No further changes until Phase 3 planning
     - Bug-fix window: May 16-18, 2026
     ```
4. Click "Publish release"

### Semantic Versioning

**Format**: `vMAJOR.MINOR.PATCH`

- **MAJOR** (v4.0): Large feature additions (Phase 2 complete)
- **MINOR** (v4.1): Small features, enhancements (add new chapter)
- **PATCH** (v4.0.1): Bug fixes, security patches

**Current Version**: v4.0 (Master App, feature-complete)

### Release Notes Template

For each release, include:

```markdown
## ✅ What's New in v4.0

### Features
- Multi-user support with SQLite database
- Gamification system (XP, levels, streaks, badges)
- 45-minute mock exam (PSLE format)
- Brain drainer challenge mode (228+ questions)
- Admin dashboard with user analytics
- 6 complete learning chapters

### Bug Fixes
- Fixed [bug description]
- Fixed [bug description]

### Known Issues
- [Known issue]

### Breaking Changes
- None

### Deployment
- Live at: https://aanya-science-exam-prep.streamlit.app/
- Deploy to local: `git clone && cd && streamlit run streamlit_app.py`

### Contributors
- harishnuti (development)
```

---

## 📊 REPOSITORY INSIGHTS

### Code Frequency

**To view code activity**:
1. Go to Insights tab
2. Click "Code frequency"
3. Shows commits over time

### Network Graph

**To visualize branches**:
1. Go to Insights tab
2. Click "Network"
3. Shows branch structure and merges

### Contributors

**To see who contributed**:
1. Go to Insights tab
2. Click "Contributors"
3. Shows commits per person
4. Current: Only harishnuti (owner)

---

## 🔍 SECURITY SETTINGS

### Dependabot

**Status**: Recommended (not yet enabled)

**To Enable**:
1. Settings → Code security and analysis
2. Click "Enable" for Dependabot
3. Creates automatic PRs for:
   - Dependency updates
   - Security vulnerabilities
4. Receives alerts for vulnerable packages

### Secret Scanning

**Status**: Available for public repositories

**To Enable**:
1. Settings → Code security and analysis
2. Enable "Push protection"
3. Prevents accidental commits of secrets

### Branch Protections

**Already Configured**: ✅ See [Protection Rules](#protection-rules) section above

---

## 📝 .GITIGNORE CONFIGURATION

**Current .gitignore** (in repository root):

```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
*.egg-info/
dist/
build/

# Environment
.env
.venv/
venv/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# Streamlit
.streamlit/
!.streamlit/config.toml  # Keep if you have default config

# Secrets
.streamlit/secrets.toml

# Database (ignored - created at runtime)
data/app.db
data/temp_*.db

# Large files (PDFs, resources - save space)
*.pdf
*.pptx
*.docx
resources/textbooks/

# OS files
.DS_Store
Thumbs.db

# Git
.git/

# Testing
.pytest_cache/
htmlcov/
.coverage
```

**Files that ARE committed** (not ignored):
- ✅ `streamlit_app.py`, `app_exam_prep_pro.py` (entry points)
- ✅ `requirements.txt` (dependencies)
- ✅ `apps/`, `src/`, `docs/` (source code)
- ✅ `README.md` and other docs
- ✅ `.gitignore` itself

**Size impact**:
- Without PDFs: ~5 MB
- With PDFs: ~120 MB (so we exclude with .gitignore)

---

## ✅ REPOSITORY CHECKLIST

**Before considering repository "complete"**:

- ✅ Main branch protection enabled
- ✅ All code committed and pushed
- ✅ requirements.txt contains all dependencies
- ✅ .gitignore properly configured
- ✅ Streamlit Cloud webhook connected
- ✅ Admin password in GitHub Secrets (not in code)
- ✅ README.md explains how to run and deploy
- ✅ Release created with version tag
- ✅ Collaborators added (if applicable)
- ✅ No secrets exposed in git history

**To verify**:
```bash
# Check git status
git status
# Should show: "On branch main, nothing to commit, working tree clean"

# Check recent commits
git log --oneline -5
# Should show recent work

# Verify remote
git remote -v
# Should show GitHub URL

# Check for secrets in git history
git log -p | grep -i "password\|api_key\|secret"
# Should return nothing (if secrets properly excluded)
```

---

## 🔄 WORKFLOW FOR CHANGES

**Standard workflow for making changes**:

```bash
# 1. Create feature branch (optional)
git checkout -b feature/[name]

# 2. Make changes locally
nano apps/exam_prep_master.py

# 3. Test locally
streamlit run streamlit_app.py

# 4. Commit to git
git add .
git commit -m "Feature: [description]"

# 5. Push to GitHub
git push origin feature/[name]  # or main if no branch protection

# 6. If on separate branch, create PR
# - Go to GitHub
# - Click "Create Pull Request"
# - Wait for review/approval
# - Merge to main
# - Delete feature branch

# 7. Streamlit Cloud auto-deploys
# - Check deployment status
# - Visit app URL to verify

# 8. Create release tag (for major updates)
git tag -a v4.1 -m "Version 4.1: [description]"
git push origin v4.1
```

---

**Status**: ✅ Fully Configured for Production  
**Last Updated**: May 16, 2026  
**Version**: 4.0 Master App

