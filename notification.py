import os
from dotenv import load_dotenv
from mac_notifications import client
import sys
import requests
from rich import print

load_dotenv(".env")

try:
    api_key = os.environ["pushover_api"]
    user_key = os.environ["pushover_user"]
except:
    print("You have to provide your api key and user key first!")


def pushover_notification(message, title=None):
    if title == None:
        title = "The Economist scrape"
    else: 
        title = "The Economist scrape - " + title

    try:
        # URL for the Pushover API
        url = "https://api.pushover.net/1/messages.json"

        data = {
            "token": api_key,
            "user": user_key,
            "device": "iphone", # might be different 4u
            "title": title,
            "message": message
        }

        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        # Make the POST request and capture the response
        response = requests.post(url, data=data, headers=headers)
    except Exception as e:
        Warning(e)

def mac_notification(message):
    client.create_notification(
        title="Hasznaltauto python scrape", 
        subtitle=message
    )

def notification(message, title):
    pushover_notification(message, title)
    
sys._excepthook = sys.excepthook

def error_notification(exc_type, exc_value, exc_traceback):
    notification(str(exc_value), title="Error")
    sys._excepthook(exc_type, exc_value, exc_traceback) # call original excepthoot. I do not why 

sys.excepthook = error_notification

if __name__ == "__main__":
    # check whether you are set correctly
    if api_key == None or user_key == None:
        print("You have to provide your api key and user key first!")
        # check whether you are set correctly
    
    notification("You get this notification on your phone.")
    sys.excepthook = error_notification
    # error triggers a notification
    2 / "a"

