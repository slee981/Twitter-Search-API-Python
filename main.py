import TwitterScraper
import sys, os
import logging as log
from time import sleep
import datetime


def main(search_query, start, stop):
    log.basicConfig(level=log.INFO)

    print("searching between {} and {}".format(start, stop))

    # select_tweets_since = datetime.strptime(start, "%Y-%m-%d")
    # select_tweets_until = datetime.strptime(stop, "%Y-%m-%d")

    # set parameters
    rate_delay_seconds = 1  # per robots.txt - avoid getting IP address banned
    error_delay_seconds = 5
    threads = 1

    twitslice = TwitterScraper.TwitterSlicer(
        rate_delay_seconds, error_delay_seconds, start, stop, threads,
    )
    twitslice.search(search_query)
    return twitslice.df


if __name__ == "__main__":
    args = sys.argv
    search_query = args[1]

    # start date and end date
    stop = datetime.date.today()
    start = stop - datetime.timedelta(days=7)

    fname = os.path.join("data", "{}-{}.xlsx".format(search_query, stop))
    print("searching for {}".format(search_query))

    df = main(search_query, start, stop)
    df.to_excel(fname)
