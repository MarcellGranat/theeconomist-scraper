# The Economist Scraper

This is a simple web scraper that scrapes the economist website for articles and export that into your.

## Installation

```
pip3 install -r requirements.txt
```

## Setup

You need to create a `.env` file in the root directory and add the following variables:

```
pushover_api=your_api_key
pushover_user=your_user_key
```

You need to login for the website first in your browser and then export the cookies to a file called `cookies.json` in the root directory. You can do this by running the following command:

```
python3 export_cookies.py
```

## Usage

```
python3 main.py
```

For the first time, it will require to login to your google account and
authenticate the app. After that, it will scrape all the articles and send you to your google drive. Modify the `main.py` file to change the folder name in which you want to save the articles or avoid notification.