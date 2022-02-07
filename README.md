# Search-tweets-from-twitter-api

This project extracts the tweets from the twitter recent search api based for keyword searches of "Justin Bieber" or "JustinBieber". The results are case-insensitive and the code filters tweets based on music.

Steps-

I created a developer account on twitter to gain access to their API. However, I only have elevated access which means that I can only request for maximum 180 times per 15 minutes and the response would always contain a maximum of 100 tweets. Also, there is a limitation to search for only the tweets that have been posted since the start of the current month.

This modular code defines a proper pipeline process to extract, filter and insert the tweets in a database (MySQL).

I used the twitter-recent-search api (https://api.twitter.com/2/tweets/search/recent) and extracted all tweets with the keyword search "Justin Bieber" or "JustinBieber".

The extracted tweets were then filtered based on twitter's context annotations key that helped us to filter the tweets that were marked as music related by the twitter api itself.

Since I could only request 180 times per 15 mins, a sleep timer was set everytime I received a 429 error code (which means too many requests).

A database and table was created in the MySQL with the following query which will hold all of our data after insertion.

create table twitter_data
(id varchar(255) primary key,
tweet TEXT,
author_id TEXT,
created_at TEXT,
lang TEXT
);

I set id as primary key to avoid duplicates and handled the exceptions in our code.

The filtered data was then ingested into the database.

Once the ingestion was complete, conversion of the database records into a csv file was done for easier access and readability.

Output- 
Count of all tweets consumed= 61325

Count of music tweets consumed= 48383
