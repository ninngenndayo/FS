import subprocess

result = subprocess.run(['python','markdown/mdparser.py'], capture_output=True, text=True)