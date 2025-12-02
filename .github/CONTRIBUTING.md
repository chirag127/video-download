# Contributing to CourseVault-Python-Udemy-Offline-Course-Downloader-CLI

As the Apex Technical Authority, we welcome contributions that elevate this project to future-proof, zero-defect standards. All contributions must adhere to the established **Apex Toolchain** and architectural principles.

## 1. Core Architectural Mandates

Before submitting any Pull Request, understand and commit to the underlying philosophy derived from the **AGENTS.md** directives:

1.  **Zero-Defect Focus:** Code must pass static analysis (Ruff) and exhibit high test coverage (Pytest).
2.  **Modularity (Modular Monolith):** New features must be encapsulated within their own modules, adhering to clear input/output contracts. Avoid tight coupling.
3.  **Dependency Management:** All new dependencies **MUST** be added via `uv` and must align with security best practices. Minimize third-party dependencies where native Python capabilities suffice.
4.  **CLI Ergonomics:** Changes to the CLI interface must be backward-compatible or accompanied by clear deprecation warnings, following best practices defined by the underlying framework (e.g., Click).

## 2. Contribution Workflow

We follow the standard GitHub Flow, augmented by our strict CI/CD pipeline:

1.  **Fork & Clone:** Fork the repository and clone your fork locally.
    bash
    git clone https://github.com/chirag127/CourseVault-Python-Udemy-Offline-Course-Downloader-CLI.git
    cd CourseVault-Python-Udemy-Offline-Course-Downloader-CLI
    

2.  **Environment Setup:** Utilize `uv` for environment isolation.
    bash
    uv venv
    source .venv/bin/activate  # On Windows use .venv\Scripts\activate
    uv sync  # Installs dependencies defined in pyproject.toml
    

3.  **Branching Strategy:** Create a new feature or fix branch from `main`:
    bash
    git checkout -b feat/descriptive-branch-name
    

4.  **Development & Verification:** Implement your changes. Before committing, ensure all local checks pass:
    bash
    # Run Linter/Formatter Check (Ruff)
    ruff check --fix .
    ruff format .

    # Run Unit/Integration Tests (Pytest)
    pytest
    

5.  **Commit Messages:** Use Conventional Commits (e.g., `feat: added new download queue management` or `fix: resolved authentication token expiry`).

6.  **Pull Request (PR):** Push your branch and open a Pull Request targeting the `main` branch on `chirag127/CourseVault-Python-Udemy-Offline-Course-Downloader-CLI`.

## 3. Pull Request Requirements

Every submitted PR **MUST** satisfy these automated and manual checks:

*   **CI Status:** Must pass all checks defined in `.github/workflows/ci.yml` (Build, Lint, Test).
*   **Documentation:** If new functionality is added, update the relevant sections of `README.md`.
*   **Code Quality:** Adherence to **SOLID** and **DRY** principles is mandatory. Any new logic must be accompanied by corresponding Pytest fixtures and tests.
*   **Security Review:** Ensure no hardcoded credentials or use of deprecated libraries. Refer to the security policy in `.github/SECURITY.md`.

## 4. Reporting Issues & Security Vulnerabilities

### Bugs and Feature Requests
Use the provided templates in `.github/ISSUE_TEMPLATE/` for filing:
*   **Bug Reports:** Detail reproduction steps clearly.
*   **Feature Requests:** Explain the use case and technical feasibility.

### Security Vulnerabilities
**DO NOT** report security vulnerabilities publicly via standard Issues. Follow the protocol outlined in **`.github/SECURITY.md`** for responsible disclosure.