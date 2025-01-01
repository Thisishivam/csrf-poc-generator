# CSRF PoC Generator

## Overview

The CSRF (Cross-Site Request Forgery) Proof of Concept (PoC) Generator is a Python script that allows users to generate and exploit CSRF vulnerabilities. This tool is designed for penetration testers and security researchers to demonstrate CSRF attacks on web applications.

The script performs the following key actions:

1. **User Input Collection**: Prompts the user for a target URL and necessary parameters for the POST request.
2. **CSRF PoC Generation**: Creates an HTML file containing a form that automatically submits a POST request with the given parameters to the target URL, simulating a CSRF attack.
3. **CSRF PoC Hosting**: Hosts the generated HTML file on a local server so it can be tested in a browser.
4. **Exploit Sending**: Sends the exploit directly to the target URL with the provided parameters using a POST request.

## Features

- **Dynamic Input**: You can specify any URL and parameters for the exploit.
- **Automatic Form Submission**: The generated PoC HTML file automatically submits the form when loaded in a browser.
- **Local Server Hosting**: A simple HTTP server is started to serve the PoC HTML file, making it easy to test in real-world scenarios.
- **Exploit Sending**: Optionally, the script can directly send the exploit to the target URL, demonstrating the attack in action.

## Prerequisites

- Python 3.x
- `requests` library (can be installed via `pip install requests`)

## How to Use

### 1. Clone the repository

Clone the repository to your local machine:

```bash
git clone https://github.com/Thisishivam/csrf-poc-generator.git
