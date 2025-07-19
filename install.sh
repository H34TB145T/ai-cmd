#!/bin/bash

echo "📦 Installing AI CMD..."
read -p "🔑 Enter your OpenRouter API key (leave blank to use default): " api_key
default_key="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"
final_key=${api_key:-$default_key}
echo "Installing xclip..."
sudo apt install xclip
# Save to ~/.aicmdkey
echo "$final_key" > ~/.aicmdkey
chmod 600 ~/.aicmdkey
sudo cp aicmd.py /usr/local/bin/aicmd
sudo chmod +x /usr/local/bin/aicmd

python3 -m pip install requests

# Make it executable
sudo chmod +x uninstall.sh
echo "✅ Installed successfully! Run it using: aicmd ask \"your command question\""
echo "🧽 If you want to uninstall later, run: ./uninstall.sh"
