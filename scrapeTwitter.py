import TwitterScraper

log.basicConfig(level=log.INFO)

search_query = "bitcoin"
rate_delay_seconds = 0
error_delay_seconds = 5

# Example of using TwitterSearch
twit = TwitterSearchImpl(rate_delay_seconds, error_delay_seconds, None)
twit.search(search_query)

# Example of using TwitterSlice
start = datetime.datetime.strptime("2018-05-02", '%Y-%m-%d')
stop = datetime.datetime.strptime("2018-05-03", '%Y-%m-%d')

twitSlice = TwitterSlicer(rate_delay_seconds, error_delay_seconds, start, stop)
twitSlice.search(search_query)

print("TwitterSearch collected %i" % twit.counter)
print("TwitterSlicer collected %i" % twitSlice.counter)
