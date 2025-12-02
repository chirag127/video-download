--- 
name: Pull Request
about: Submit changes to the CourseVault-Python-Udemy-Offline-Course-Downloader-CLI project.
title: "[TYPE]: Short, descriptive title (e.g., [FEAT]: Implement course resume functionality)"
labels: ''
assignees: ''
---

## 🚀 Pull Request Checklist: The Apex Review Protocol

Before submitting your pull request, please ensure you have completed the following steps. This template guides you through our "Zero-Defect, High-Velocity" standard.

### 🎯 Purpose & Impact

*   **What problem does this PR solve?** (Provide a clear, concise summary of the issue addressed.)
*   **What new functionality or improvement does this PR introduce?**
*   **How does this change align with the project's overall goals?** (e.g., improved stability, new core feature, better user experience).

### 📖 Changes Made

*   List the main changes introduced in this PR.
    *   [ ] Added/Modified/Deleted: `path/to/file.py` - brief description
    *   [ ] Added/Modified/Deleted: `path/to/another_file.py` - brief description

### 🔗 Related Issues & Documentation

*   **Closes:** #ISSUE_NUMBER (if applicable)
*   **References:** #ISSUE_NUMBER (if applicable)
*   **Is there any associated documentation (internal or external) that needs updating?**
    *   [ ] Yes (Link to documentation changes/PR)
    *   [ ] No

### ✅ Testing & Verification

*   **Have you tested these changes thoroughly?** Describe the testing approach.
    *   [ ] **Unit Tests (`pytest`):** New tests added or existing tests updated to cover changes.
        *   Have all `pytest` tests passed locally?
        *   Command run: `uv run pytest`
    *   [ ] **Integration Tests:** (Describe any integration tests conducted, e.g., end-to-end download flow).
    *   [ ] **Manual/Functional Tests:** (Describe specific manual steps taken to verify the feature).
        *   Steps to reproduce/verify manually:
            1. Step 1
            2. Step 2
*   **Test Environment:**
    *   Python Version: `x.y.z`
    *   OS: `Linux/macOS/Windows`

### 🏗️ Architectural & Code Quality Standards

*   **Adherence to "Modular Monolith" Principles:**
    *   [ ] Are concerns clearly separated within modules?
    *   [ ] Are dependencies managed appropriately (e.g., no forbidden cross-module imports)?
*   **Code Style & Linting (`ruff`):**
    *   [ ] Have you run `uv run ruff check --fix .` and `uv run ruff format .`?
    *   [ ] Are there any new linting warnings or errors introduced?
*   **Readability & Maintainability:**
    *   [ ] Is the code clear, concise, and well-commented where necessary?
    *   [ ] Are variable and function names descriptive?
    *   [ ] Are complex algorithms explained?
*   **Performance & Efficiency:**
    *   [ ] Are there any known performance implications? (If yes, describe them.)
    *   [ ] Have you considered potential resource usage (memory, CPU, network)?
*   **Error Handling & Robustness:**
    *   [ ] Does the code gracefully handle expected errors and edge cases?
    *   [ ] Are appropriate exceptions raised and caught?
*   **Security Considerations:**
    *   [ ] Have potential security vulnerabilities been considered and mitigated?
    *   [ ] Are sensitive data or credentials handled securely (e.g., environment variables, not hardcoded)?
    *   Refer to our [Security Policy](https://github.com/chirag127/CourseVault-Python-Udemy-Offline-Course-Downloader-CLI/blob/main/.github/SECURITY.md).

### 📦 Dependencies

*   **New Dependencies:**
    *   [ ] Have any new dependencies been added to `pyproject.toml`? If so, why?
    *   [ ] Are these dependencies well-maintained and from reputable sources?
*   **Updated Dependencies:**
    *   [ ] Have existing dependencies been updated? If so, why (e.g., security, new features)?

### 📝 Reviewer Checklist (For the Reviewer)

*   [ ] Code functionality verified.
*   [ ] Adheres to architectural patterns and design principles (Modular Monolith, SOLID/DRY where applicable).
*   [ ] Code quality and style standards met (Ruff output clean).
*   [ ] Tests are sufficient and pass.
*   [ ] Documentation (if any) is updated.
*   [ ] No new security vulnerabilities introduced.
*   [ ] Performance implications considered.

---

### 💡 Additional Notes for Reviewers
(Any specific areas to pay attention to, or complex logic that might need extra scrutiny.)
