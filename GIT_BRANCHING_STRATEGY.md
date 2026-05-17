# 🌿 Git Branching Strategy - Phase 3 Onwards

**Created**: May 17, 2026  
**Branching Model**: Main/Develop Split Model  
**Status**: ✅ ACTIVE  

---

## 📊 Branch Structure

```
Repository: aanya-science-exam-prep
│
├── main (FROZEN - v4.5-stable-frozen)
│   ├── Tag: v4.5-stable-frozen
│   ├── Status: PRODUCTION (Testing Phase)
│   ├── Protection: YES - No direct commits
│   ├── Deploy: Manually reviewed merges only
│   └── Purpose: Stable, tested, released versions
│
└── develop/v4.5-phase3-onwards (ACTIVE - Development)
    ├── Base: Created from main @ commit ae6c890
    ├── Status: DEVELOPMENT (Active)
    ├── Protection: NO - Feature development here
    ├── Deploy: Auto-deploy on push (optional)
    └── Purpose: All Phase 3+ development
```

---

## 🔄 Workflow

### Development Workflow (Phase 3 onwards)

```
develop/v4.5-phase3-onwards
│
├── Feature: GUI Redesign
│   ├── Commit: Add rainbow color palette
│   ├── Commit: Implement design system
│   ├── Commit: Add responsive layout
│   └── Commit: Add animations
│
├── Feature: Mobile Optimization
│   ├── Commit: Mobile-first redesign
│   ├── Commit: Touch-friendly buttons
│   └── Commit: Responsive breakpoints
│
├── Feature: Persistent Database
│   ├── Commit: Add PostgreSQL config
│   ├── Commit: Migrate from SQLite
│   └── Commit: Test database layer
│
└── [Merge to main when v4.6 ready for release]
    └── Create Pull Request → Review → Merge → Tag v4.6-stable
```

---

## 📋 Branch Rules

### `main` Branch (FROZEN)
**Status**: 🔴 PROTECTED - No direct commits

```
Rules:
- ✅ Only merge from pull requests
- ✅ Requires testing verification
- ✅ Requires at least 1 review (human)
- ✅ All tests must pass
- ✅ Auto-deploy disabled
- ✅ Tag each release (v4.5, v4.6, etc.)
```

**When to commit to main**:
- ❌ NEVER commit directly
- ✅ ONLY merge tested, reviewed code via PR
- ✅ ONLY after Aanya's testing feedback reviewed
- ✅ ONLY after Phase 3 development complete

**Protected from**:
- ✅ Accidental commits
- ✅ Incomplete features
- ✅ Untested code
- ✅ Breaking changes

---

### `develop/v4.5-phase3-onwards` Branch (ACTIVE)
**Status**: 🟢 OPEN - Active development

```
Rules:
- ✅ Direct commits allowed
- ✅ Feature development here
- ✅ Frequent commits encouraged
- ✅ Commit message format: "Feat/Fix/Docs: [description]"
- ✅ Testing encouraged but not required
- ✅ Auto-deploy disabled (manual only if needed)
```

**When to commit to develop**:
- ✅ Phase 3 development (GUI redesign)
- ✅ Phase 4+ development (new features)
- ✅ Bug fixes discovered during testing
- ✅ Improvements and enhancements
- ✅ Documentation updates

**Workflow**:
```
1. Make changes on develop branch
2. Commit frequently with clear messages
3. Push to GitHub
4. When feature complete:
   → Create Pull Request to main
   → Request review
   → Get approval
   → Merge to main
   → Tag new version
```

---

## 🚀 Release Process

### From develop/v4.5-phase3-onwards → main

**Step 1: Prepare Release**
```bash
# On develop branch
git status  # Ensure clean
git log --oneline -10  # Review commits
```

**Step 2: Create Pull Request**
```bash
# Create PR from develop to main
gh pr create --base main --head develop/v4.5-phase3-onwards \
  --title "Release: v4.6 - Phase 3 Complete" \
  --body "Release PR description"
```

**Step 3: Review & Test**
```
- Test on staging/development
- Verify all Phase 3 features work
- Check for regressions
- Get approval from lead
```

**Step 4: Merge to main**
```bash
gh pr merge <PR_NUMBER> --squash
# OR merge via GitHub UI
```

**Step 5: Tag Release**
```bash
git checkout main
git pull
git tag -a v4.6-stable -m "Version 4.6 - Phase 3 Complete"
git push origin v4.6-stable
```

**Step 6: Deploy**
```
- Update deployment config to point to main
- Deploy to Streamlit Cloud
- Run post-deployment tests
- Announce release
```

---

## 📝 Commit Message Format

Use this format for all commits on develop branch:

```
Type: Brief description (50 chars max)

More detailed explanation (if needed)
- Bullet point 1
- Bullet point 2

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>
```

**Types**:
- `Feat:` - New feature
- `Fix:` - Bug fix
- `Docs:` - Documentation
- `Refactor:` - Code refactoring
- `Test:` - Tests
- `Style:` - Formatting/style
- `Perf:` - Performance improvement

**Examples**:
```
Feat: Add rainbow color palette to design system

Refactor: Simplify quiz display logic

Fix: Mobile button alignment on small screens

Docs: Update branching strategy guide
```

---

## 🔍 Current Status

### Main Branch (FROZEN)
```
Branch: main
Latest Tag: v4.5-stable-frozen
Latest Commit: ae6c890 (Docs: Add comprehensive testing and freeze documentation)
Status: 🔴 PROTECTED & FROZEN
Deployment: Manual (testing phase)
```

### Development Branch (ACTIVE)
```
Branch: develop/v4.5-phase3-onwards
Base Commit: ae6c890 (same as main)
Status: 🟢 OPEN & ACTIVE
Deployment: Manual (testing phase)
```

---

## ✅ Phase 3 Development Checklist

When starting Phase 3 development on `develop/v4.5-phase3-onwards`:

- [ ] Verify you're on correct branch: `git branch` shows `develop/v4.5-phase3-onwards`
- [ ] Verify main is protected and frozen
- [ ] Pull latest from develop branch
- [ ] Create feature branches for major features (optional)
- [ ] Make commits with clear messages
- [ ] Push to develop branch frequently
- [ ] Test on development server
- [ ] Document changes
- [ ] When Phase 3 complete: Create PR to main

---

## 🛡️ Safety Features

### Main Branch Protection
- ✅ Prevents accidental overwrites
- ✅ Requires code review before merge
- ✅ Requires all tests pass
- ✅ Maintains version history
- ✅ Clear release points (tags)

### Develop Branch Safety
- ✅ Separate from production code
- ✅ Easy to reset if needed
- ✅ All development isolated
- ✅ Can test features before merge
- ✅ Commits can be amended (before push)

---

## 📊 Example: Phase 3 Development Timeline

```
Timeline:
│
├─ May 17 (Today)
│  ├─ main: Frozen at v4.5-stable-frozen
│  └─ develop/v4.5-phase3-onwards: Created
│
├─ May 18-28 (Testing Phase)
│  └─ Main: Frozen for testing
│
├─ May 29 (Phase 3 Begins)
│  ├─ develop: Feature work starts
│  ├─ Commit: Add color system
│  ├─ Commit: Add navigation redesign
│  └─ Commit: Add animations
│
├─ June 10 (Phase 3 Complete)
│  ├─ develop: All features done
│  ├─ Testing on develop branch
│  └─ Create PR to main
│
├─ June 12 (Code Review)
│  ├─ main: PR reviewed
│  ├─ main: Tests pass
│  └─ main: Approved for merge
│
└─ June 13 (Release v4.6)
   ├─ main: Merged
   ├─ main: Tagged v4.6-stable
   └─ Deploy to production
```

---

## 🚨 Important Rules

### NEVER on Main Branch
- ❌ Don't commit directly
- ❌ Don't force push
- ❌ Don't delete branches
- ❌ Don't merge without review

### ALWAYS on Develop Branch
- ✅ Make all Phase 3+ changes here
- ✅ Commit frequently with clear messages
- ✅ Push to GitHub regularly
- ✅ Test features before merging to main

### Before Merging to Main
- ✅ Complete all Phase 3 features
- ✅ Test thoroughly on develop
- ✅ No breaking changes
- ✅ Update documentation
- ✅ Get code review

---

## 🔄 Reverting Changes (If Needed)

**If something goes wrong on develop branch**:

```bash
# See commit history
git log --oneline -10

# Revert to previous commit (creates new commit)
git revert <commit_hash>

# Or reset to previous state (use carefully!)
git reset --hard <commit_hash>  # CAREFUL!
```

**If something goes wrong on main branch**:
```bash
# NEVER use reset on main
# Instead:
# 1. Revert the problematic merge
# 2. Create new PR with fix
# 3. Merge new PR to main
```

---

## 📞 Questions About Branching?

Reference this document or ask:
- "What branch should I work on?" → `develop/v4.5-phase3-onwards`
- "Can I commit to main?" → No, use develop only
- "How do I release?" → Create PR from develop → Merge to main → Tag
- "What if I make a mistake?" → Ask, we can revert!

---

## ✅ Summary

| Item | Main | Develop |
|------|------|---------|
| **Status** | 🔴 FROZEN | 🟢 ACTIVE |
| **Latest** | v4.5-stable-frozen | Phase 3 dev |
| **Commits** | PR only | Direct commits |
| **Deploy** | Manual (testing) | Manual or auto |
| **Purpose** | Stable releases | Active development |
| **Merge** | After review | To main when done |

---

**Remember**: 
- ✅ `main` = Frozen and tested (DO NOT TOUCH)
- ✅ `develop/v4.5-phase3-onwards` = Where all Phase 3+ work happens
- ✅ Keep them separate until Phase 3 is complete and approved!

