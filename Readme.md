##Bo Query Tool
A simple proof of concept sample app for querying [Bo's](https://github.com/udeyrishi/bo) processed results (stored in MongoDB).

##Dependencies
Python 3 and PyMongo. Install PyMongo using:

```sh
pip install -r requirements.txt
```

##Running
```sh
./main.py <mongo_url> <mongo_db_name> <mongo_collection_name>
Tag >> <enter_tagname_here>
s
Min relevance >> <enter_min_relevance_here>
Min sentiment >> <enter_min_sentiment_here>

<results printed>
```

The results are all the documents (i.e., Bo web page processing results) with one or more tags containing the entered tagname as a substring, such that the relevance value >= min\_relevance and sentiment value >= min\_sentiment.

See [Bo's Readme](https://github.com/udeyrishi/bo) for the details.
