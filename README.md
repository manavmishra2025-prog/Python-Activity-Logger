This modular Python surveillance tool captures endpoint telemetry for cybersecurity research. It runs concurrent listeners for keystrokes, mouse activity, and window context using pynput and win32gui. Data is aggregated and automatically exfiltrated via email, demonstrating effective red-teaming and data extraction techniques.

For the tool to work, the attacker has to download and store all the python scripts in the same working directory, and edit the email_from, email_list and passwd variables in the main.py script as per his/her convenience.
Python 3.14.2 was used to write this tool.
