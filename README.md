
# SSH Login Tester in Python

This project demonstrates a simple Python script for testing SSH login credentials. Using the `paramiko` library, the script attempts to connect to a target IP address using a provided username and password, and prints the result directly to the terminal.

---

## What is SSH?

SSH (Secure Shell) is a cryptographic network protocol used for securely accessing remote machines. It allows users to execute commands, manage files, and perform administrative tasks on servers from a local terminal.

This script uses `paramiko`, a Python implementation of SSHv2, to initiate and test SSH logins from a local system.

---

## How It Works

The script prompts the user to input:

- The target IP address  
- A valid SSH username  
- The corresponding password  

It then tries to open an SSH connection to the target using those credentials:

- If the login is successful, it prints a confirmation message.  
- If authentication fails or an error occurs (e.g., unreachable host), it prints an appropriate error message.  
- Unknown host keys are automatically accepted using Paramiko’s `AutoAddPolicy`.

---

## Getting Started

### Requirements

To run this project, you’ll need:

- Python 3 installed on your computer  
- The `paramiko` package (`pip install paramiko`)  
- A code editor or terminal  
- A reachable SSH server (for testing your login)

If Python isn’t installed, you can download it here:  
https://www.python.org/downloads/

---

## Installation

1. Download or clone this repository to your local machine  
2. Open the script file in a code editor  
3. Install the required package:  
   ```bash
   pip install paramiko
   ```

---

## Running the Program

1. Open your terminal  
2. Navigate to the script’s directory  
3. Run the script with:  
   ```bash
   python ssh_connect.py
   ```

4. When prompted, enter:

- The target IP address  
- The SSH username  
- The password  

5. View the result printed in the terminal.

