import subprocess
import os
import shutil
import git

si = subprocess.STARTUPINFO()
si.dwFlags |= subprocess.STARTF_USESHOWWINDOW

#si.wShowWindow = subprocess.SW_HIDE # default

s = os.path.abspath(__file__)
c = s.replace(os.path.basename(os.path.abspath(__file__)), '')

    
def Updater():
    git.Repo.clone_from("https://github.com/TestSoulja/TeSoulLauncher", "_internal")

Updater()

subprocess.run(["python", c+"TeSoulLaunch.py"])

path = os.path.join(c+"_internal")

# startupinfo=si