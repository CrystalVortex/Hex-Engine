import os

import shutil

import time

import logging

import subprocess

import os.path

import glob

import re

import sys

import time

from pathlib import Path

import requests

from ursina import *

import tkinter

import customtkinter

import tkinter.messagebox

import platform

import logging

import wget

from tkinter import *



def unknown_error():
   tkinter.messagebox.showwarning('Hex Engine:Error','An unknown error occurred!')

def close_error():
   tkinter.messagebox.showwarning('Hex Engine:Error','An unknown error occurred when closing!')

def update_error():
   tkinter.messagebox.showwarning('Hex Engine:Error','An unknown error occurred: Your game is not up to date!')
   exit()
   
def confirm():
   tkinter.messagebox.showwarning('Hex Engine:Confirmation','Press ok to continue!')
   exit()

def close():
   exit()

def console_execute_bat():
   subprocess.Popen('main.bat', shell=True)

def console_execute_sh():
   subprocess.Popen('main.sh', shell=True)
   
def console_execute_ps1():
   subprocess.Popen('main.ps1', shell=True)
   

def console_execute_otherexe():
   subprocess.Popen('other.exe', shell=True)
   
def pyconsole(pyconsole):
   exec(pyconsole)

def launch(app):
   subprocess.Popen(app, shell=True)
   
def console(ccommand):
   os.system(ccommand)

def make_folder_existsfine(foldername):
   Path(foldername).mkdir(parents=True, exist_ok=True)

def make_folder_exists_not_fine(foldername):
   Path(foldername).mkdir(parents=True, exist_ok=False)
   
def optionalmodules():
   import os
   import shutil
   import time
   import logging
   import subprocess
   import os.path
   import glob
   import re
   import sys
   import time
   from pathlib import Path
   import requests
   import tkinter.messagebox
   import platform
   import logging
   


def get_file(link, saveto):
   wget.download(link, saveto)
   

def deletefile(filename):
   os.remove(filename)
   
def deletefolder(folderlocation):
   os.remove(folderlocation)

def logo_splash_hex():
   
   
   splash_root = Tk()
      
   
   splash_root.geometry("500x500")
   
   splash_root.wm_attributes('-fullscreen', 'True')
   
   
   splash_label = Label(splash_root,text="Hex Engine: Loading...",font=18)
   splash_label.pack()
   
   
   def main(): 
      
      splash_root.destroy()
      
   
   
   splash_root.after(2000,main)
   
   
   mainloop()

def logo_splash_custom(text):

   splash_root = Tk()
      

   splash_root.geometry("500x500")
   

   splash_label = Label(splash_root,text=text,font=18)
   splash_label.pack()
   

   def main(): 

      splash_root.destroy()
      
   

   splash_root.after(2000,main)
   

   mainloop()
   
def logo_splash_custom_fullscreen(text):

   splash_root = Tk()
      

   splash_root.geometry("500x500")
   
   splash_root.wm_attributes('-fullscreen', 'True')
   

   splash_label = Label(splash_root,text=text,font=18)
   splash_label.pack()
   

   def main(): 
      
      splash_root.destroy()
      
   
   
   splash_root.after(2000,main)
   
   
   mainloop()
