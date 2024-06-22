from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

from scrape_edition import last_edition, download_edition
from time import sleep

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

filename = last_edition().strftime("%Y-%m-%d")
filename = "economist" + filename + ".pdf"

os.system(f"quarto render template.qmd --to pdf --output {filename}")

sleep(5)

file2 = drive.CreateFile()
file2.SetContentFile(filename)
file2.Upload()

sleep(5)

new_filename = last_edition().strftime("%Y-%m-%d") + "/edition.pdf"
os.rename(filename, new_filename)