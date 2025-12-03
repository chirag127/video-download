# Contributing to FileFlow-Automated-Asset-Synchronization-Python-CLI

Thank you for your interest in contributing to FileFlow-Automated-Asset-Synchronization-Python-CLI! We aim to maintain a high standard of quality, velocity, and future-proofing. Please adhere to the following guidelines to ensure a smooth and productive contribution process.

## 1. Code of Conduct

This project adheres to the Contributor Covenant Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to [your-email@example.com](mailto:your-email@example.com).

## 2. Getting Started

### Prerequisites

*   **Python:** Version 3.10+ installed.
*   **uv:** Installed for dependency management. If not present, run `pip install uv`.
*   **Git:** For version control.

### Project Setup

1.  **Clone the Repository:**
    bash
    git clone https://github.com/chirag127/FileFlow-Automated-Asset-Synchronization-Python-CLI.git
    cd FileFlow-Automated-Asset-Synchronization-Python-CLI
    

2.  **Create a Virtual Environment (Recommended):**
    bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    

3.  **Install Dependencies using uv:**
    bash
    uv pip install -r requirements.txt
    uv pip install -r requirements-dev.txt # For development tools
    

## 3. Development Workflow

We follow a standard Gitflow-like workflow for contributions:

1.  **Feature Branches:** Create a new branch for each feature or bug fix. Use a descriptive name, e.g., `feature/add-s3-support` or `fix/sync-error-handling`.
    bash
    git checkout -b feature/your-branch-name
    

2.  **Coding Standards:**
    *   **Language:** Python 3.10+
    *   **Linting & Formatting:** Adhere to Ruff standards. All code will be automatically checked during CI. Ensure your code passes `ruff check .` and `ruff format .`.
    *   **Architecture:** Follow the Modular Monolith principles. Ensure clear separation of concerns and well-defined API contracts between modules.
    *   **Testing:** Write comprehensive unit and integration tests using Pytest. Aim for high code coverage. All tests must pass.
    *   **Async:** Leverage Python's `asyncio` for asynchronous operations where appropriate, as per the project's nature.

3.  **Committing Changes:**
    *   Write clear, concise commit messages. Follow conventional commit format if possible (e.g., `feat: Add S3 synchronization`, `fix: Correct handling of empty directories`).
    *   Stage your changes:
        bash
        git add .
        
    *   Commit your changes:
        bash
        git commit -m "feat: Implement feature X"
        

4.  **Testing and Linting:**
    *   Run tests locally before pushing:
        bash
        pytest
        
    *   Run linters and formatters locally:
        bash
        ruff check .
        ruff format .
        

5.  **Submitting a Pull Request (PR):**
    *   Ensure your branch is up-to-date with the main branch:
        bash
        git fetch origin
        git rebase origin/main
        
    *   Push your branch to your fork:
        bash
        git push origin feature/your-branch-name
        
    *   Open a Pull Request on the `chirag127/FileFlow-Automated-Asset-Synchronization-Python-CLI` repository.
    *   Provide a clear title and detailed description for your PR, explaining the changes and the problem they solve.
    *   Link to any relevant issues.

## 4. Architectural Principles (Apex Standard)

*   **SOLID:** Adhere to the Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, and Dependency Inversion principles.
*   **DRY:** Don't Repeat Yourself. Abstract common functionality.
*   **YAGNI:** You Ain't Gonna Need It. Implement only what is currently required.
*   **Modular Monolith:** Maintain a cohesive codebase with well-defined internal boundaries, allowing for potential future extraction into microservices if needed.

## 5. AI Agent Directives

This project integrates with AI models for intelligent file processing. When contributing:

*   Ensure all AI-related code is modular and easily testable.
*   Handle API errors gracefully and provide informative feedback.
*   Document any changes to AI model interactions or configurations.
*   Refer to the `AGENTS.md` file for detailed AI interaction protocols and configurations.

## 6. Reporting Issues

If you find a bug or have a feature request, please open an issue on GitHub. Use the provided issue templates (`bug_report.md`) for detailed reporting.

## 7. License

This project is licensed under the **CC BY-NC 4.0** license. By contributing, you agree to license your contributions under this license.

---

*Last Updated: December 2025*
