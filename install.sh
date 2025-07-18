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
