# TwitterSearchAPI
Adapted from https://github.com/tomkdickinson/Twitter-Search-API-Python.

## Required Libraries
Make sure Python 3 is installed on your path. 

* BeautifulSoup 4
* Requests

## Quick Use 

#### Clone and change directory 
```
$ git clone https://github.com/slee981/TwitterSearchAPI
$ cd TwitterSearchAPI 
```

#### Set up virtual environment
```
$ python3 -m venv .env && source .env/bin/activate 
$ pip install -r requirements.txt 
```

#### Scrape tweets 
```
$ python main.py "real-time payments" 
```

#### Check results 
This process scrapes the last seven (7) day's worth of tweets that contain the phrase "real-time payments" and save the results in a file called "./data/real-time payments-2020-11-06.xlsx" --- i.e. it saves a file titled with the search query and the date. 
