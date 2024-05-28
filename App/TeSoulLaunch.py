import customtkinter
import os
from PIL import Image
import wget
import time
import zipfile
import configparser
from urllib.parse import urlencode
from os import getcwd
import urllib
from CTkMessagebox import CTkMessagebox
import git
import requests
import shutil
import json
import zipfile


customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")
s = os.path.abspath(__file__)
c = s.replace(os.path.basename(os.path.abspath(__file__)), '')
path = c
p1 = path.replace("_internal", "")


config = configparser.ConfigParser()
config.read(c + 'config.ini', encoding='UTF-8')

version = 1

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("TeSoulLauncher")
        self.geometry("700x450")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        
        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(5, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(
            self.navigation_frame, 
            text="  Image Example",compound="left", 
            font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(
            self.navigation_frame, 
            corner_radius=0, height=40, 
            border_spacing=10, 
            text="Home", 
            fg_color="transparent", 
            text_color=("gray10", "gray90"), 
            hover_color=("gray70", "gray30"),
            command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(
            self.navigation_frame, 
            corner_radius=0, height=40, 
            border_spacing=10, 
            text="Frame 2", 
            fg_color="transparent", 
            text_color=("gray10", "gray90"), 
            hover_color=("gray70", "gray30"), 
            command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(
            self.navigation_frame, 
            corner_radius=0, height=40, 
            border_spacing=10, 
            text="Frame 3", 
            fg_color="transparent", 
            text_color=("gray10", "gray90"), 
            hover_color=("gray70", "gray30"), 
            command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")
        
        # self.update_button = customtkinter.CTkButton(
        #     self.navigation_frame, 
        #     corner_radius=0, height=40, 
        #     border_spacing=10, 
        #     text="Check for update", 
        #     fg_color="transparent", 
        #     text_color=("gray10", "gray90"), 
        #     hover_color=("gray70", "gray30"), 
        #     command=self.update_button_event)
        # self.update_button.grid(row=10, column=0, sticky="ew")


        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        # self.home_frame_button_1 = customtkinter.CTkButton(
        #     self.home_frame,
        #     text="Download",
        #     command=self.home_frame_button_1_event)
        # self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)

        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")
    
        
    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")
    
    def update_button_event(self):
        def ask_question():
            msg = CTkMessagebox(title="Update?", message="Do you want to Update the program?",
                                icon="question", option_1="Yes", option_2="No")
            response = msg.get()
            print(os.path.abspath(__file__))
            if response=="Yes":
                p1 = path.replace("_internal", "")
                try:
                    shutil.rmtree(p1 + "updater")
                except:
                    pass
                print("ok")
                
                base_url = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?'
                public_key = "https://disk.yandex.ru/d/QoVVMrmyIbEOSg"
                final_url = base_url + urlencode(dict(public_key=public_key))
                response = requests.get(final_url)
                download_url = response.json()['href']

                download_response = requests.get(download_url)
                p1 = path.replace("_internal", "")
                with open(p1+'updater.zip', 'wb') as f:
                    f.write(download_response.content)

                with zipfile.ZipFile(p1 + 'updater.zip', 'r') as zip_ref:
                    zip_ref.extractall(p1+"updater")
                
                os.remove(p1+'updater.zip')
                
                os.system(p1+"updater/updater/updater.exe")

                # app.destroy()
            else:
                print("Click 'Yes' to exit!")
        
        print(path.replace("_internal", ""))
        base_url = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?'
        public_key = "https://disk.yandex.ru/d/WlZRPNs-L0GCvA"
        final_url = base_url + urlencode(dict(public_key=public_key))
        response = requests.get(final_url)

        download_url = response.json()['href']

        download_response = requests.get(download_url)
        ver = download_response.text.replace("version-", "")
        if int(ver) > version:
            ask_question()
            

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()

# pyinstaller -F --onefile --noconsole Launcher.py
# pyinstaller -F --onefile --noconsole --add-data "TeSoulLaunch.py;." Launcher.py
# pyinstaller Launcher.spec

# pyinstaller --noconsole Launcher.py
# pyinstaller --noconsole --add-data "TeSoulLaunch.py;." Launcher.py

# pyinstaller TeSoulLaunch.spec

# pyinstaller -F --onefile TeSoulLaunch.py
# pyinstaller TeSoulLaunch.py
# pyinstaller --add-data "updater.py;." TeSoulLaunch.py

# pyinstaller --noconsole updater.py
# pyinstaller --noconsole TeSoulLaunch.py