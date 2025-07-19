# 🧠 AI Command (aicmd)

**`aicmd`** is a smart command-line assistant powered by OpenRouter's free DeepSeek AI API. Ask natural-language questions and instantly get detailed Linux command suggestions — with bullet-point explanations for every part of the command!

For the API key, you can generate a free DeepSeek API key here --> https://openrouter.ai/deepseek/deepseek-chat-v3-0324:free

---

## 📦 Features

- 💬 Ask: `aicmd ask "How do I list all files ending in .exe?"`
- 📋 AI-generated command with full explanation
- 🧠 Optional **Lab Mode** for using offensive tools (e.g., `hydra`)
- 🗝️ API key stored securely in `~/.aicmdkey`
- 🔧 Installs to `/usr/local/bin/aicmd` for global access

---

## 🚀 Installation

```bash
git clone https://github.com/H34TB145T/ai-cmd.git
cd ai-cmd
chmod +x install.sh
./install.sh
```

- You will be asked to enter your OpenRouter API key.
- If you leave it blank, a default key will be used (but not recommended).

✅ After install, you can run:
```bash
aicmd ask "your question here"
```

---

## 🧪 Lab Mode

If you're working in an ethical hacking or CTF environment:

```bash
aicmd --lab ask "how to use hydra for ftp brute force"
```

This mode relaxes filtering to allow explanations for offensive/security tools.

---

## 🔑 API Key

Your key is stored in a hidden file:
```bash
~/.aicmdkey
```
To update it:
```bash
nano ~/.aicmdkey
```

---

## ❌ Uninstallation

To remove the tool:
```bash
./uninstall.sh
```

This removes:
- `/usr/local/bin/aicmd`
- `~/.aicmdkey`

---

## 🛠 Dependencies

Only two dependency is required:
```bash
pip install requests
apt install xclip
```

This is handled automatically by `install.sh`.

---

## 📎 Example

```bash
aicmd ask "how to find and delete all .log files older than 7 days"
```

**Output:**
```
💡 Command: find /path/to/search -name "*.log" -type f -mtime +7 -delete
📘 Explanation: Explanation: This command finds all files (-type f) with the .log extension (-name "*.log") in the specified directory (replace /path/to/search) that were modified more than 7 days ago (-mtime +7) and deletes them (-delete).
📋 Command copied to clipboard!
```

---

## 🧠 Built With

- [OpenRouter API](https://openrouter.ai/)
- Bash + Python 3

---
