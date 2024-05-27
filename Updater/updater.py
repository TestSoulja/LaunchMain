import os
import requests
from urllib.parse import urlencode
import zipfile
import psutil,os
import shutil

s = os.path.abspath(__file__)
c = s.replace(os.path.basename(os.path.abspath(__file__)), '')
path = c

base_url = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?'
public_key = "https://disk.yandex.ru/d/hvqNgSF5GEwbRA"
final_url = base_url + urlencode(dict(public_key=public_key))
response = requests.get(final_url)
download_url = response.json()['href']
download_response = requests.get(download_url)
p1 = path.replace("_internal", "")
with open(p1+'TeSoulLaunchq.zip', 'wb') as f:
    f.write(download_response.content)
with zipfile.ZipFile(p1 + 'TeSoulLaunchq.zip', 'r') as zip_ref:
    zip_ref.extractall(p1)

os.remove(p1+'TeSoulLaunchq.zip')

for process in (process for process in psutil.process_iter() if process.name()=="TeSoulLaunch.exe"):
    process.kill()

p2 = p1.replace("updater\\updater", "")
print(p2)

os.remove(p2 + "TeSoulLaunch.exe")
shutil.rmtree(p2 + "_internal")
shutil.move(p1 + "TeSoulLaunch\\TeSoulLaunch.exe", p2 + "TeSoulLaunch.exe")
shutil.move(p1 + "TeSoulLaunch\\_internal", p2 + "_internal")

os.system(p2 + "TeSoulLaunch.exe")