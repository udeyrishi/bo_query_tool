import argparse

import pymongo

from tag_query_runner import TagQueryRunner


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('mongo_uri', help='The URI to the Mongo DB')
    arg_parser.add_argument('mongo_db', help='The DB name')
    arg_parser.add_argument('collection', help='The collection name')
    args = arg_parser.parse_args()

    client = pymongo.MongoClient(args.mongo_uri)
    db = client[args.mongo_db][args.collection]
    print("Starting runner...")
    query_runner = TagQueryRunner(db)
    query_runner.run()
    client.close()
    print("Now quitting")

if __name__ == '__main__':
    main()
