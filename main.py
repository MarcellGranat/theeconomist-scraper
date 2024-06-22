from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
from scrape_edition import last_edition, download_edition
from time import sleep
import notification

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

def main() -> None:
    filename = last_edition().strftime("%Y-%m-%d")
    filename = "economist" + filename + ".pdf"

    os.system(f"quarto render template.qmd --to pdf --output {filename}")

    sleep(5)

    file = drive.CreateFile()
    file.SetContentFile(filename)
    file.Upload()

    sleep(5)

    new_filename = last_edition().strftime("%Y-%m-%d") + "/edition.pdf"
    os.rename(filename, new_filename)
    notification.notification("Your new edition is exported")

if __name__ == "__main__":
    main()