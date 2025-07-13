# P4wnP1-HID-Tools
Basic Python-based toolset for converting and appending HID scripts compatible with P4wnP1 A.L.O.A.

## Overview


This utility provides two core functionalities:

- **Converter**: Translates standard Ducky Script into P4wnP1-compatible JavaScript HID payloads.
- **Appender**: Allows users to select and concatenate multiple script fragments into a single output file for deployment.

It streamlines payload creation for use via SSH on P4wnP1 A.L.O.A., particularly for placing scripts under `/usr/local/P4wnP1/HIDScripts` to be reflected in the web UI.

## Requirements


- Python 3.x
- Works on Windows (default paths) but easily adaptable to Linux-based P4wnP1 systems

## Usage


Run the script and choose between the converter or appender tool:


```bash
python3 hid_tool.py
