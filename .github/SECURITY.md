# Security Policy

## Supported Versions

| Version | Supported |
| ------- | --------- |
| Main branch (develop) | ✅ |
| Other branches | ❌ |

## Reporting a Vulnerability

We take security seriously. If you find a vulnerability in `FileFlow-Automated-Asset-Synchronization-Python-CLI`, please follow these steps to report it:

1.  **DO NOT** open a public issue. This could expose the vulnerability to malicious actors before it can be fixed.
2.  Send a detailed email to `chirag.agarwal127@gmail.com` with the subject line `Security Vulnerability Report: FileFlow-Automated-Asset-Synchronization-Python-CLI`.
3.  In your email, please include:
    *   A clear description of the vulnerability.
    *   The affected version(s) (e.g., specific commit hash or branch name if applicable).
    *   Steps to reproduce the vulnerability.
    *   Any proof-of-concept (PoC) code or detailed information that can help us understand and fix the issue.
    *   Your contact information so we can follow up.

## Disclosure Timeline

We aim to address all reported security vulnerabilities as quickly as possible. Upon receiving a report, we will:

1.  Acknowledge receipt of your report within **48 hours**.
2.  Assess the severity and impact of the vulnerability.
3.  Work on a fix and release it in a timely manner.
4.  Once a fix is deployed, we will work with you to coordinate a public disclosure, if appropriate.

## Best Practices

To help prevent security issues, we encourage users and contributors to follow these best practices:

*   **Keep Dependencies Updated:** Regularly update the project's dependencies to their latest secure versions. This repository uses `uv` for dependency management.
*   **Use Virtual Environments:** Always use Python virtual environments to isolate project dependencies.
*   **Avoid Hardcoding Secrets:** Never hardcode sensitive information such as API keys or passwords directly into the codebase. Utilize environment variables or secure secret management solutions.
*   **Review Code Changes:** Carefully review all incoming code changes, especially those from external contributors.

Thank you for helping keep `FileFlow-Automated-Asset-Synchronization-Python-CLI` secure!