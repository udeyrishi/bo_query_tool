import argparse
import signal

import pymongo

from tag_query_runner import TagQueryRunner


def sigint_handler(sig, frame, client):
    client.close()
    print("\nNow quitting")
    exit(0)


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('mongo_uri', help='The URI to the Mongo DB')
    arg_parser.add_argument('mongo_db', help='The DB name')
    arg_parser.add_argument('collection', help='The collection name')
    args = arg_parser.parse_args()

    client = pymongo.MongoClient(args.mongo_uri)
    db = client[args.mongo_db][args.collection]
    signal.signal(signal.SIGINT, lambda sig, frame: sigint_handler(sig, frame, client))
    print("Starting runner...")
    query_runner = TagQueryRunner(db)
    query_runner.run()


if __name__ == '__main__':
    main()
