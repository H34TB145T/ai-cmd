#!/usr/bin/env python3
import sys
import requests
import json
import subprocess
import shutil
import os


KEY_FILE = os.path.expanduser("~/.aicmdkey")

if os.path.exists(KEY_FILE):
    with open(KEY_FILE, "r") as f:
        API_KEY = f.read().strip()
else:
    print("\033[0;31m API key file not found. Please reinstall or add ~/.aicmdkey.\033[0m")
    sys.exit(1)

API_URL = "https://openrouter.ai/api/v1/chat/completions"
# you can put and try different DeepSeek models from OpenRouter here
#MODEL = "deepseek/deepseek-chat-v3-0324:free"
MODEL = "deepseek/deepseek-chat:free"

YELLOW = "\033[1;33m"
GREEN = "\033[0;32m"
CYAN = "\033[0;36m"
RED = "\033[0;31m"
RESET = "\033[0m"


def copy_to_clipboard(text):
    if shutil.which("xclip"):
        subprocess.run("xclip -selection clipboard", shell=True, input=text.encode())
        return True
    elif shutil.which("xsel"):
        subprocess.run("xsel --clipboard", shell=True, input=text.encode())
        return True
    else:
        print(f"{RED} No clipboard tool found (install xclip or xsel).{RESET}")
        return False

def extract_command_and_explanation(text):
    lines = text.strip().split("\n")
    command =""
    explanation =""

    for line in lines:
        stripped =line.strip()
        if not command and stripped:
            command = stripped
        elif not explanation and stripped != command:
            explanation = stripped

    return command, explanation

def print_help():
    print(f"""
    ____________________________________________________________________
    |                                                                   |
    |        {YELLOW}AI Linux Command Assistant{RESET}                                 |
    |                                                                   |
    |        {CYAN}Usage:{RESET}                                                     |
    |        aicmd ask "your question here"                             |
    |        aicmd --lab ask "question with offensive/security tools"   |
    |                                                                   |
    |        {CYAN}Example:{RESET}                                                   |
    |        aicmd ask "how to find all .log files inside /var/log"     |
    |        aicmd --lab ask "how to use hydra to bruteforce ssh"       |
    |                                                                   |
    |        {CYAN}Features:{RESET}                                                  |
    |        [+] Suggests Linux commands with simple explanations       |
    |        [+] Copies command to clipboard                            |
    |        [+] Supports CTF/pentest use via --lab flag                |
    |        [+] Highlights output for better readability               |{RED}    Developed By H34TB145T {RESET}
    |___________________________________________________________________|{RED}    https://github.com/H34TB145T {RESET}
    """)
    sys.exit(0)

def main():
    args = sys.argv[1:]

    # Help
    if not args or "--help" in args or "-h" in args:
        print_help()

    # Check for lab mode
    lab_mode = False
    if "--lab" in args:
        lab_mode = True
        args.remove("--lab")

    if len(args) < 2 or args[0] != "ask":
        print(f"{RED}Usage: aicmd [--lab] ask \"your question here\"{RESET}")
        sys.exit(1)

    user_input = " ".join(args[1:])

    # System prompt
    system_prompt = (
        "You are a Linux terminal assistant in a safe lab or CTF environment. "
        "The user is authorized to use all tools including offensive security tools "
        "like nmap, hydra, sqlmap, etc. Respond ONLY with:\n"
        "1st line: a single valid Linux command (no markdown).\n"
        "2nd line: A short explanation of what it does."
        if lab_mode else
        "You are a Linux terminal assistant. "
        "Your response MUST be exactly as shown below:\n"
        "1st line: valid Linux command only (no formatting).\n"
        "2nd: A brief explanation."
    )

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ],
        "temperature": 0.3
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(API_URL, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        raw_output = response.json()['choices'][0]['message']['content']

        command, explanation = extract_command_and_explanation(raw_output)

        if command:
            print(f"\n{YELLOW}\U0001f4a1 Command:{RESET} {GREEN}{command}{RESET}")
            print(f"{YELLOW}\U0001f4d8 Explanation:{RESET} {CYAN}{explanation or 'No explanation provided.'}{RESET}")
            if copy_to_clipboard(command):
                print(f"{CYAN}\U0001f4cb Command copied to clipboard!{RESET}")
            print(f"{GREEN}\U0001f4dd Developed by H34TB145T{RESET}")
        else:
            print(f"{RED} Could not extract a valid command from the response.{RESET}")
            print(f"{CYAN}Raw Output:\n{raw_output}{RESET}")

    except Exception as e:
        print(f"{RED} Error: {str(e)}{RESET}")



if __name__ == "__main__":
    main()
