# DownloadFlow-Automated-File-Manager-Python-Lib

## 💡 Project Synthesis & Value Proposition

**DownloadFlow** is a high-performance, production-grade Python library designed to automate the entire lifecycle of file acquisition and organization from disparate sources. It replaces manual download routines with intelligent, policy-driven workflows, ensuring zero-defect asset management and immediate categorization.

This repository serves as the definitive blueprint for maintaining, verifying, and evolving this core infrastructure component, adhering strictly to the **Apex Technical Authority (ATA) directives** for 2026 compatibility.

---

## 🏛️ Architectural Blueprint (Modular Monolith - Late 2025 Standard)

The system is structured as a **Modular Monolith**, leveraging Python's capabilities for robust separation of concerns. The CLI interface acts as the entry point, orchestrating dedicated modules for source integration, policy engine execution, and final storage.

mermaid
graph TD
    A[User CLI Interface (Click)] --> B(Orchestration Layer);
    B --> C{Source Adapters: HTTP, FTP, S3};
    B --> D(Policy Engine: Categorization/Tagging);
    D --> E[File System Manager: Move/Rename/Cleanup];
    C --> F(External Download Engine);
    F --> D;
    E --> G(Logging & Metrics);

    subgraph Core Principles
        P1(SOLID Compliance) --> P2(DRY Adherence);
    end

    B -.-> P1;
    D -.-> P2;


## 📚 Table of Contents

1.  [💡 Project Synthesis & Value Proposition](#-project-synthesis--value-proposition)
2.  [🏛️ Architectural Blueprint (Modular Monolith - Late 2025 Standard)](#-architectural-blueprint-modular-monolith---late-2025-standard)
3.  [📚 Table of Contents](#-table-of-contents)
4.  [🤖 AI Agent Directives (Critical Compliance)](#-ai-agent-directives-critical-compliance)
5.  [🛠️ Apex Toolchain & Standards](#-apex-toolchain--standards)
6.  [🚀 Getting Started](#-getting-started)
7.  [🧪 Verification & Testing](#-verification--testing)
8.  [🤝 Contribution & Governance](#-contribution--governance)

---

## 🤖 AI Agent Directives (Critical Compliance)

<details>
<summary>▶️ Execute Apex Agent Verification Protocol</summary>

This section contains the non-negotiable mandates for any automated or human agent interacting with this codebase, derived directly from the **Apex Technical Authority**. Agents must confirm alignment before any modification.

### **I. Technical Stack Confirmation (Python 2025 Standard)**

*   **Language:** Python 3.10+ (Strict Type Hinting Mandatory).
*   **Package Manager:** `uv` (All dependency updates must use `uv sync` or `uv add`).
*   **Linting/Formatting:** `Ruff` (Strict configuration enforcing PEP 8 compliance, maximum line length 100, and immediate formatting on save/commit).
*   **Testing Framework:** `Pytest` (Minimum 90% unit test coverage required for all new features).
*   **AI/ML Integration:** None specified for this version (Pure automation focus). If AI is introduced, Google Gemini API must be used (`gemini-3-pro` or higher).

### **II. Architectural & Quality Mandates**

1.  **SOLID Compliance:** All modules must exhibit strong Single Responsibility (S) and Interface Segregation (I). Dependency Injection (DI) is preferred over global state.
2.  **DRY Principle:** Avoid redundant file handling logic. Abstract all disk I/O operations into an `io_adapters` module.
3.  **YAGNI:** Do not implement features not currently required by the core download/categorization loop. Future-proofing must be achieved through abstraction, not premature complexity.

### **III. Verification Commands (Bootstrap Phase)**

Agents must execute the following sequence to validate the environment setup before proceeding:

bash
# 1. Clone Repository (Replace URL if necessary)
cd $PROJECT_ROOT
git checkout main

# 2. Environment Initialization using uv
python3 -m venv .venv
source .venv/bin/activate
# Install dependencies from a locked file (e.g., requirements.lock)
"$PWD/.venv/bin/uv" sync --locked

# 3. Format Check (Ruff)
ruff check .
ruff format . --check

# 4. Run Unit Tests (Pytest)
pytest --cov=./ --cov-report=term-missing

# 5. Final Success Signal
echo "// APEX AGENT VERIFICATION SUCCESSFUL. PROCEED WITH TASK EXECUTION. //"


</details>

## 🛠️ Apex Toolchain & Standards

| Component | Tool / Standard | Justification (2026 Alignment) |
| :--- | :--- | :--- |
| **Language** | Python 3.11+ | Enhanced performance and modern syntax features. |
| **Dependency Mgmt** | `uv` | Superior speed over traditional pip/Poetry for CI/CD environments. |
| **Code Quality** | `Ruff` | Mandatory ultra-fast linting/formatting enforcement. |
| **Testing** | `Pytest` + `pytest-cov` | Industry standard for flexible, readable, and exhaustive testing. |
| **Architecture** | Modular Monolith | Optimal balance of maintainability and deployment simplicity for infrastructure libraries. |
| **License** | CC BY-NC 4.0 | Preserves academic and commercial use distinction. |

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.11 or newer installed.

### Local Environment Setup

Follow the verification commands in the **AI Agent Directives** section, or use the following simplified path:

bash
# 1. Clone Repository
git clone https://github.com/chirag127/DownloadFlow-Automated-File-Manager-Python-Lib.git
cd DownloadFlow-Automated-File-Manager-Python-Lib

# 2. Create and Activate Virtual Environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install Dependencies (Using uv for speed)
# Assuming dependencies are specified in a base configuration file (e.g., requirements.txt or pyproject.toml setup)
"$PWD/.venv/bin/uv" sync

# 4. Run Linter/Formatter Check
ruff check src/
ruff format src/ --check


### Execution Scripts

| Script Name | Command | Description |
| :--- | :--- | :--- |
| **Format & Lint** | `uv run lint` | Runs Ruff formatter and linter checks across the codebase. |
| **Test Suite** | `uv run test` | Executes full Pytest suite with coverage reporting. |
| **Build CLI** | `uv run build` | Generates distributable artifacts (e.g., wheel/sdist). |
| **Run Main** | `uv run main -- <args>` | Executes the primary CLI entry point for demonstration. |

## 🧪 Verification & Testing

Verification is mandatory upon every interaction. The system relies on **Pytest** to validate every adapter and policy transformation.

1.  **Unit Tests:** Located in `tests/unit/`. Focus on testing individual functions in isolation, especially configuration loading and path manipulation.
2.  **Integration Tests:** Located in `tests/integration/`. These tests simulate a full download cycle, verifying disk write locations and renaming conventions against mock file systems.
3.  **Coverage Target:** Maintain a minimum of **90% coverage**. Any PR falling below 90% will fail CI automatically.

bash
# Execute comprehensive test suite
pytest --strict-markers --cov=./ --cov-report=xml:coverage.xml


## 🤝 Contribution & Governance

Contributions are welcome, provided they adhere to the **Apex Technical Authority** standards outlined herein and within the `.github/` directory.

*   All code must pass static analysis checks defined in `badges.yml`.
*   Pull Requests require 1 approval from a maintainer.
*   Security vulnerability disclosures must follow the process outlined in `.github/SECURITY.md`.

**License:** This project is licensed under the **CC BY-NC 4.0** license. See the `LICENSE` file for details.