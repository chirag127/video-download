# CourseVault: Python Udemy Offline Course Downloader

[![Build Status](https://img.shields.io/github/actions/workflow/ci.yml?style=flat-square&logo=github&label=Build&user=chirag127&repo=CourseVault-Python-Udemy-Offline-Course-Downloader-CLI)](https://github.com/chirag127/CourseVault-Python-Udemy-Offline-Course-Downloader-CLI/actions/workflows/ci.yml)
[![Code Coverage](https://img.shields.io/codecov/c/github/chirag127/CourseVault-Python-Udemy-Offline-Course-Downloader-CLI?style=flat-square&logo=codecov&label=Coverage)](https://app.codecov.io/gh/chirag127/CourseVault-Python-Udemy-Offline-Course-Downloader-CLI)
[![Tech Stack](https://img.shields.io/badge/Tech%20Stack-Python%20%7C%20Click-blue?style=flat-square&logo=python)](https://github.com/chirag127/CourseVault-Python-Udemy-Offline-Course-Downloader-CLI)
[![License](https://img.shields.io/github/license/chirag127/CourseVault-Python-Udemy-Offline-Course-Downloader-CLI?style=flat-square&label=License)](https://github.com/chirag127/CourseVault-Python-Udemy-Offline-Course-Downloader-CLI/blob/main/LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/chirag127/CourseVault-Python-Udemy-Offline-Course-Downloader-CLI?style=flat-square&logo=github)](https://github.com/chirag127/CourseVault-Python-Udemy-Offline-Course-Downloader-CLI/stargazers)


⭐ Star this Repo

## BLUF
CourseVault is a Python CLI tool designed to download Udemy courses for offline access, providing a convenient way to manage and organize your Udemy learning library. This tool enables you to download courses, manage the downloaded content, and organize the course material locally.


## Architecture
ascii
CourseVault
├── course_vault.py (Entry Point)
├── udemy_downloader.py (Downloads courses)
├── course_manager.py (Manages downloads)
├── config.py (Configuration)
├── utils.py (Utility functions)
├── requirements.txt (Dependencies)
└── LICENSE


## Table of Contents

*   [Installation](#installation)
*   [Usage](#usage)
*   [Configuration](#configuration)
*   [Contributing](#contributing)
*   [License](#license)

## Installation

1.  **Clone the repository:**

    bash
    git clone https://github.com/chirag127/CourseVault-Python-Udemy-Offline-Course-Downloader-CLI.git
    cd CourseVault-Python-Udemy-Offline-Course-Downloader-CLI
    

2.  **Install dependencies using uv:**

    bash
    uv pip install -r requirements.txt
    

## Usage

bash
python course_vault.py --help


Follow the on-screen instructions.

## Configuration

Set your Udemy credentials and download preferences in `config.py`. Make sure to read and adhere to Udemy's terms of service.

## Contributing

Contributions are welcome! Please see the [CONTRIBUTING.md](.github/CONTRIBUTING.md) file for details.

## License

This project is licensed under the CC BY-NC license - see the [LICENSE](LICENSE) file for details.

<details>
<summary>🤖 AI Agent Directives</summary>

This section defines guidelines for AI agents interacting with this repository.

### Tech Stack Definition

*   **Language:** Python 3.10+
*   **Package Management:** `uv` (preferred)
*   **Linting & Formatting:** `ruff` (integrated via pre-commit)
*   **Testing:** `pytest` (unit and integration tests)
*   **CLI Framework:** `Click` or similar.

### Architectural Patterns

*   **SOLID Principles:** Adherence to SOLID principles for maintainable and scalable code.
*   **DRY (Don't Repeat Yourself):** Minimize code duplication.
*   **YAGNI (You Ain't Gonna Need It):** Avoid implementing features unless strictly necessary.

### Verification Commands

*   **Linting:** `ruff .`
*   **Formatting:** `ruff . --fix`
*   **Testing:** `pytest`
*   **Coverage:** `pytest --cov=course_vault --cov-report term-missing --cov-report html`

These commands MUST be executed before any commits to ensure code quality.

</details>
