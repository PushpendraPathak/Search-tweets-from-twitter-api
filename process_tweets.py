import connection


def process_tweets(twitterData):
    #this method processes tweets for filtering of music related context annotations
    countAllTweets=0
    countMusicTweets=0
    print("processing tweets")
    con = connection.get_connection()
    cursor = con.cursor()
    for i in range(len(twitterData)):
        for j in range(len(twitterData[i])):
            countAllTweets+=1
            if 'context_annotations' in twitterData[i][j].keys():
                for k in twitterData[i][j]['context_annotations']:
                    if k['domain']['id']=='54' or k['domain']['id']=='89' or k['domain']['id']=='132' or k['domain']['id']=='114' or k['domain']['id']=='90':
                        if connection.save(cursor,twitterData[i][j]['id'],twitterData[i][j]['text'],twitterData[i][j]['author_id'],twitterData[i][j]['created_at'],twitterData[i][j]['lang']):
                            countMusicTweets += 1
                        break
    con.commit()
    cursor.close()
    con.close()
    return countMusicTweets,countAllTweets