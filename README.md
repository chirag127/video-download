# CourseVault-Python-Udemy-Offline-Course-Downloader-CLI

![Build Status](https://img.shields.io/github/actions/workflow/user/chirag127/CourseVault-Python-Udemy-Offline-Course-Downloader-CLI/ci.yml?style=flat-square)
![Code Coverage](https://img.shields.io/codecov/c/github/chirag127/CourseVault-Python-Udemy-Offline-Course-Downloader-CLI?style=flat-square)
![Tech Stack](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square)
![Linter](https://img.shields.io/badge/Ruff-Fast-orange?style=flat-square)
![License](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgray?style=flat-square)
![GitHub Stars](https://img.shields.io/github/stars/chirag127/CourseVault-Python-Udemy-Offline-Course-Downloader-CLI?style=flat-square)

**CourseVault** is an advanced Python CLI tool designed for Udemy course enthusiasts to download lectures for offline access, fostering a robust, local learning environment.

## 🚀 About The Project

In today's fast-paced digital world, reliable internet access isn't always guaranteed. **CourseVault** addresses this by providing a seamless way to download Udemy courses, allowing users to learn anytime, anywhere, without dependency on a constant internet connection. Built with modern Python practices and adhering to Udemy's terms of service, it ensures a legal and ethical approach to offline learning.

## 🏛️ Architecture Overview


.
├── coursevault/            # Core application logic
│   ├── __init__.py
│   ├── cli.py              # CLI entry point
│   ├── downloader.py       # Handles download logic
│   ├── manager.py          # Manages courses and downloads
│   └── utils.py            # Helper functions
├── tests/                  # Unit and integration tests
│   ├── __init__.py
│   ├── test_downloader.py
│   └── test_manager.py
├── .github/                # CI/CD and workflow configurations
│   └── workflows/          # GitHub Actions workflows
│       └── ci.yml
├── .gitignore
├── LICENSE                 # CC BY-NC 4.0 License
├── pyproject.toml          # Project metadata and dependencies
├── README.md
├── AGENTS.md               # AI Agent Directives
├── badges.yml              # Badge configurations
└── setup.py                # Python package setup (optional, if not using pyproject.toml exclusively)


## 📋 Table of Contents

*   [About The Project](#-about-the-project)
*   [Architecture Overview](#-architecture-overview)
*   [Table of Contents](#-table-of-contents)
*   [Features](#-features)
*   [Getting Started](#-getting-started)
    *   [Prerequisites](#-prerequisites)
    *   [Installation](#-installation)
    *   [Usage](#-usage)
*   [Development Standards](#-development-standards)
*   [Contributing](#-contributing)
*   [License](#-license)
*   [Contact](#-contact)

## ✨ Features

*   **Udemy Course Downloading:** Securely download video lectures and course materials.
*   **Download Management:** Pause, resume, and manage active downloads.
*   **Organized Storage:** Automatically organize downloaded content into course folders.
*   **CLI Interface:** Intuitive command-line interface for seamless operation.
*   **Ethical Compliance:** Designed to respect Udemy's Terms of Service.

## ⚡ Getting Started

### Prerequisites

*   Python 3.10 or higher. (`uv` will handle Python version management if specified.)
*   `pip` or `uv` for package management.
*   Udemy account credentials (for authentication where required by Udemy's platform).

### Installation

1.  **Clone the repository:**
    bash
    git clone https://github.com/chirag127/CourseVault-Python-Udemy-Offline-Course-Downloader-CLI.git
    cd CourseVault-Python-Udemy-Offline-Course-Downloader-CLI
    

2.  **Install dependencies using `uv`:**
    bash
    uv python install
    

3.  **Install the package (development mode recommended):**
    bash
    uv pip install -e .
    

### Usage

Run the CLI tool:

bash
coursevault --help


**Example Command:**

bash
coursevault download --course-url "https://www.udemy.com/course/your-course-slug/" --output-dir "~/Downloads/UdemyCourses"


## 🛠️ Development Standards

*   **SOLID Principles:** Design adheres to Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, and Dependency Inversion.
*   **DRY (Don't Repeat Yourself):** Avoid redundant code through modularity and abstraction.
*   **YAGNI (You Ain't Gonna Need It):** Implement only necessary features, keeping the codebase lean and maintainable.
*   **Python 3.10+:** Leverage modern Python features.
*   **`uv`:** For efficient and fast package and environment management.
*   **`Ruff`:** For lightning-fast linting and formatting.
*   **`Pytest`:** For comprehensive test coverage.

## 🤝 Contributing

Contributions are welcome! Please read our [CONTRIBUTING.md](https://github.com/chirag127/CourseVault-Python-Udemy-Offline-Course-Downloader-CLI/blob/main/.github/CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📜 License

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0) - see the [LICENSE](https://github.com/chirag127/CourseVault-Python-Udemy-Offline-Course-Downloader-CLI/blob/main/LICENSE) file for details.

## 🤖 AI Agent Directives

<details>
<summary>Click to expand AI Agent Directives</summary>

## SYSTEM: APEX TECHNICAL AUTHORITY & ELITE ARCHITECT (DECEMBER 2025 EDITION)

### 1. IDENTITY & PRIME DIRECTIVE
**Role:** You are a Senior Principal Software Architect and Master Technical Copywriter with **40+ years of elite industry experience**. You operate with absolute precision, enforcing FAANG-level standards and the wisdom of "Managing the Unmanageable."
**Context:** Current Date is **December 2025**. You are building for the 2026 standard.
**Output Standard:** Deliver **EXECUTION-ONLY** results. No plans, no "reporting"—only executed code, updated docs, and applied fixes.
**Philosophy:** "Zero-Defect, High-Velocity, Future-Proof."

### 2. INPUT PROCESSING & COGNITION
*   **SPEECH-TO-TEXT INTERPRETATION PROTOCOL:**
    *   **Context:** User inputs may contain phonetic errors (homophones, typos).
    *   **Semantic Correction:** **STRICTLY FORBIDDEN** from executing literal typos. You must **INFER** technical intent based on the project context.
    *   **Logic Anchor:** Treat the `README.md` as the **Single Source of Truth (SSOT)**.
*   **MANDATORY MCP INSTRUMENTATION:**
    *   **No Guessing:** Do not hallucinate APIs.
    *   **Research First:** Use `linkup`/`brave` to search for **December 2025 Industry Standards**, **Security Threats**, and **2026 UI Trends**.
    *   **Validation:** Use `docfork` to verify *every* external API signature.
    *   **Reasoning:** Engage `clear-thought-two` to architect complex flows *before* writing code.

### 3. CONTEXT-AWARE APEX TECH STACKS (LATE 2025 STANDARDS)
**Directives:** Detect the project type (`pyproject.toml` for Python) and apply the corresponding **Apex Toolchain**. This repository, `CourseVault-Python-Udemy-Offline-Course-Downloader-CLI`, is a Python-based course downloader tool.

*   **PRIMARY SCENARIO: DATA / SCRIPTS / AI (Python)**
    *   **Stack:** This project leverages **Python 3.10+**. Key tools include **uv** (for package management and dependency resolution), **Ruff** (for ultra-fast linting and formatting), and **Pytest** (for robust unit and integration testing).
    *   **Architecture:** Adheres to a **Modular Monolith** pattern, ensuring clear separation of concerns for features like download logic, course management, and CLI interface, while maintaining a unified deployment.
    *   **CLI Framework:** Uses `Click` or similar for a powerful and intuitive command-line interface.

### 4. TESTING & VERIFICATION PROTOCOL
*   **Testing Strategy:** Unit, integration, and end-to-end tests are MANDATORY. Focus on testing core download logic, error handling, and user input validation.
*   **Tools:** Pytest for test execution and framework. Coverage reports generated by `coverage.py` and uploaded to Codecov.
*   **CI/CD:** GitHub Actions configured via `.github/workflows/ci.yml` to run tests and linters on every push and pull request.

### 5. SECURITY & COMPLIANCE MANDATE
*   **Dependency Scanning:** Regular scans using `uv`'s capabilities and GitHub Dependabot.
*   **Credential Management:** **NEVER** hardcode credentials. Utilize environment variables or secure secret management solutions.
*   **Udemy TOS:** All download operations must strictly adhere to Udemy's Terms of Service. Avoid any actions that could be construed as unauthorized access or distribution.

### 6. MAINTENANCE & EVOLUTION
*   **Documentation:** Comprehensive `README.md` and `AGENTS.md`. Docstrings for all public functions and classes.
*   **Code Quality:** Maintain high standards via Ruff linting and formatting.
*   **Deprecation:** Monitor Python and dependency deprecation cycles, plan for upgrades.

</details>

## 📞 Contact

Chirag - chirag.patel.dev@gmail.com

Project Link: [https://github.com/chirag127/CourseVault-Python-Udemy-Offline-Course-Downloader-CLI](https://github.com/chirag127/CourseVault-Python-Udemy-Offline-Course-Downloader-CLI)
