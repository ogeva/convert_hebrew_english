# Hebrew-English Keyboard Converter

A small Python script to convert text between English and Hebrew keyboard layouts (macOS Hebrew keyboard mapping).

## Table of Contents
- [Overview](#overview)
- [Features](#features)  
- [Prerequisites](#prerequisites)  
- [Installation](#installation)
  - [Method 1: Command Line Usage](#method-1-command-line-usage)
  - [Method 2: macOS Automator Integration](#method-2-macos-automator-integration)
  - [Method 3: Installer Package](#method-3-installer-package)
- [Usage](#usage)
  - [Command Line](#command-line)
  - [macOS Keyboard Shortcut](#macos-keyboard-shortcut)
- [Examples](#examples)  
- [Keyboard Mapping Details](#keyboard-mapping-details)  
- [Troubleshooting](#troubleshooting)
- [Compatibility](#compatibility)
- [Contributing](#contributing)  
- [License](#license)  

## Overview

This tool lets you convert text between English and Hebrew keyboard layouts. It's perfect for:

- Typing in the wrong keyboard layout and needing to convert it
- Working with mixed-language documents
- Quickly transliterating text without changing your keyboard layout

## Features

- Automatically detects whether the input is primarily English or Hebrew
- Converts each character according to the macOS Hebrew keyboard layout
- System-wide keyboard shortcut (when set up with Automator)
- Works in any application that supports text selection
- Toggle between original and converted text
- Preserves digits, punctuation, whitespace, and unsupported characters

## Prerequisites

- Python 3.6 or later (pre-installed on modern macOS)
- macOS 10.13 (High Sierra) or later (for Automator integration)

## Installation

### Method 1: Command Line Usage

1. Clone the repo (or download the single script):
   ```bash
   git clone https://github.com/your-username/convert_hebrew_english.git
   cd convert_hebrew_english
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Make the script executable:
   ```bash
   chmod +x convert_hebrew_english.py
   ```

### Method 2: macOS Automator Integration

1. **Download the script**
   - Save `convert_hebrew_english.py` to your home directory (`~/convert_hebrew_english.py`)
   - Make it executable by running in Terminal: `chmod +x ~/convert_hebrew_english.py`

2. **Create the Automator Service**
   - Open Automator (found in Applications)
   - Create a new document and select "Quick Action" (or "Service" in older macOS versions)
   - Configure the workflow:
     - Workflow receives "text" in "any application"
     - Input is "selected text"
   - Add a "Run Shell Script" action from the library
   - Configure it:
     - Shell: `/bin/zsh`
     - Pass input: "as stdin"
     - Script: `~/convert_hebrew_english.py`
   - Save the workflow as "Convert English-Hebrew"

3. **Set up the keyboard shortcut**
   - Open System Settings/Preferences
   - Go to Keyboard → Keyboard Shortcuts → Services
   - Find "Convert English-Hebrew" under Text services
   - Assign a keyboard shortcut (e.g., ⌥⌘H or ⌃⇧H)

### Method 3: Installer Package

1. Download the installer package (HebrewEnglishConverter.pkg) if available
2. Double-click to open and follow installation instructions
3. Set up the keyboard shortcut as described in step 3 above

## Usage

### Command Line

Read from stdin and write to stdout, so you can pipe or redirect:

```bash
# Pipe echo'd text
echo "hello world" | python3 convert_hebrew_english.py

# Convert a file
python3 convert_hebrew_english.py < input.txt > output.txt

# If the script is executable
./convert_hebrew_english.py < hebrew_text.txt > english_out.txt
```

### macOS Keyboard Shortcut

If you've set up the Automator service:

1. Select text in any application
2. Press your assigned keyboard shortcut (e.g., ⌥⌘H)
3. The text will be converted between English and Hebrew keyboard layouts
4. To convert back, select the text again and press the same shortcut

## Examples

```bash
$ echo "shalom" | python3 convert_hebrew_english.py
שלום

$ echo "שלום" | python3 convert_hebrew_english.py
shalv
```

When using the keyboard shortcut in applications like TextEdit:
- Type "akuo" with English keyboard → Select text and use shortcut → "שלום"
- Type "שלום" with Hebrew keyboard → Select text and use shortcut → "akuo"

## Keyboard Mapping Details

This script uses the standard macOS Hebrew keyboard mapping:

```
English: q w e r t y u i o p [ ]
Hebrew:  / ' ק ר א ט ו ן ם פ ] [

English: a s d f g h j k l ; '
Hebrew:  ש ד ג כ ע י ח ל ך ף ,

English: z x c v b n m , . /
Hebrew:  ז ס ב ה נ מ צ ת ץ .
```

Here's a reference table for some common characters:

| English key | Hebrew character |
|-------------|------------------|
| a           | ש                |
| s           | ד                |
| t           | א                |
| y           | ט                |
| , (comma)   | ת                |
| . (period)  | ץ                |

Digits, whitespace, and punctuation are preserved or swapped according to the layout.
You can inspect the full mapping in `convert_hebrew_english.py` under `eng_to_heb` and `heb_to_eng`.

## Troubleshooting

- **Text isn't converting**: Make sure you've selected the text completely before using the shortcut
- **Shortcut isn't working**: Check if your keyboard shortcut conflicts with another application
- **Incorrect conversions**: The script maps based on the standard Hebrew keyboard layout. If you're using a different layout, the mapping may not match
- **Permission errors**: If the script won't run, check permissions with `chmod +x ~/convert_hebrew_english.py`
- **Service not appearing**: Try logging out and back in, or restarting your Mac

## Compatibility

- Requires macOS 10.13 (High Sierra) or later for Automator integration
- Works with any macOS application that supports text selection
- The command line version should work on any system with Python 3.6+, including Linux and Windows

## Contributing

Feel free to open issues or pull requests if you notice any missing mappings or bugs.

1. Fork the repo  
2. Create a feature branch (`git checkout -b feat-awesome`)  
3. Commit your changes (`git commit -m "Add awesome feature"`)  
4. Push to your branch (`git push origin feat-awesome`)  
5. Open a Pull Request  

## License

This project is released under the MIT License. See [LICENSE](LICENSE) for details.

---

Created with ❤️ for Hebrew speakers and language enthusiasts