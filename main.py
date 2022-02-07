from datetime import  date
import connect_twitter_endpoint
import process_tweets
import time
import connection
import pandas


def main():
    #we use recent search api of twitter and it provides data only from the first of the current month
    search_url = "https://api.twitter.com/2/tweets/search/recent"
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    currDate = d1.split('/')
    countAllTweets = 0                  #saves all tweets consumed
    countMusicTweets = 0                #saves tweets related to music
    twitterData = []

    #since number of requests are limited per quarter hour, we loop our requests and add a waiting time for 429 response code
    for i in range(1, int(currDate[0])+1):
        for j in range(0, 24):
            for k in range(0, 60, 5):
                dateFormatter = str(i)
                if len(dateFormatter) == 1:
                    dateFormatter = '0' + dateFormatter
                hourFormatter = str(j)
                if len(hourFormatter) == 1:
                    hourFormatter = '0' + hourFormatter
                minuteFormatter = str(k)
                endMinuteFormatter = str(k + 4)
                if len(minuteFormatter) == 1:
                    minuteFormatter = '0' + minuteFormatter
                    if len(endMinuteFormatter) == 1:
                        endMinuteFormatter = '0' + endMinuteFormatter

                #querying what we need- justin bieber related tweets
                query_params = {'query': '("Justin Bieber" OR "justinbieber") -is:retweet',
                                'tweet.fields': 'context_annotations,author_id,created_at,lang',
                                'max_results': '100', 'start_time': currDate[2] + '-' + currDate[
                        1] + '-' + dateFormatter + 'T' + hourFormatter + ':' + minuteFormatter + ':00.00Z',
                                'end_time': currDate[2] + '-' + currDate[
                                    1] + '-' + dateFormatter + 'T' + hourFormatter + ':' + endMinuteFormatter + ':59.00Z'}

                try:
                    json_response,status_code = connect_twitter_endpoint.connect_to_endpoint(search_url, query_params)
                    if status_code==429:
                        a, b = process_tweets.process_tweets(twitterData)
                        countAllTweets += b
                        countMusicTweets += a
                        print("Sleeping for 15 minutes to accomodated too many requests", countMusicTweets,countAllTweets)
                        twitterData=[]
                        k-=5
                        time.sleep(900)
                        print('restarting the requests')
                    else:
                        twitterData.append(json_response['data'])
                except Exception as e:
                    pass

    a, b = process_tweets.process_tweets(twitterData)
    countAllTweets += b
    countMusicTweets += a

    print("Count of all tweets consumed= " + str(countAllTweets))
    print("Count of music tweets consumed= " + str(countMusicTweets))

    #converting data in db into csv
    query= 'SELECT * from twitter_data;'
    results = pandas.read_sql_query(query, connection.get_connection())
    results.to_csv("output.csv", index=False)

if __name__ == "__main__":
    main()
