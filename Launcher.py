import subprocess
import os

si = subprocess.STARTUPINFO()
si.dwFlags |= subprocess.STARTF_USESHOWWINDOW

#si.wShowWindow = subprocess.SW_HIDE # default

s = os.path.abspath(__file__)
c = s.replace(os.path.basename(os.path.abspath(__file__)), '')

subprocess.run(["python", c+"TeSoulLaunch.py"], startupinfo=si)
