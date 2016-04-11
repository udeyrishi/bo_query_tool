##Bo Query Tool
A proof of concept sample app for querying [Bo's](https://github.com/udeyrishi/bo) processed results (stored in MongoDB).

##Dependencies
Python 3 and PyMongo. Install PyMongo using:

```sh
pip install -r requirements.txt
```

##Running
```sh
# Usage
./main.py -h
usage: main.py [-h] [-f FILE] mongo_uri mongo_db collection

positional arguments:
  mongo_uri             The URI to the Mongo DB
  mongo_db              The DB name
  collection            The collection name

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  The path to the output file. If not provided, printed
                        to stdout.

# Example:
./main.py mongodb://localhost:27017/ bo_db bo_items
                        
Min relevance >> <enter_min_relevance_here>
Min sentiment >> <enter_min_sentiment_here>

<results printed>
```

The results are all the documents (i.e., Bo web page processing results) such that:

1. At least one tag contains the passed tagname as a substring, and
2. The relevance value for that tag >= min\_relevance, and 
3. The sentiment value for that tag >= min\_sentiment.

See [Bo's Readme](https://github.com/udeyrishi/bo) for the details.
