#!/bin/bash

echo "\U0001f4e6 Installing AI CMD..."
read -p "\U0001f511 Enter your OpenRouter API key (leave blank to use default): " api_key

# this is my free api key, so it has limit
# using your own key is recommended :)) Link in ReadMe.md file! 
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
echo "\u2705 Installed successfully! Run it using: aicmd ask \"your command question\""
echo "\U0001f9fd If you want to uninstall later, run: ./uninstall.sh"
