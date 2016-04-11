#!/usr/bin/env python3


# Copyright 2016 Udey Rishi
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#    http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
    arg_parser.add_argument('-f', '--file', help='The path to the output file. If not provided, printed to stdout.')
    args = arg_parser.parse_args()

    client = pymongo.MongoClient(args.mongo_uri)
    db = client[args.mongo_db][args.collection]
    signal.signal(signal.SIGINT, lambda sig, frame: sigint_handler(sig, frame, client))
    print("Starting runner...")
    query_runner = TagQueryRunner(db, args.file)
    query_runner.run()


if __name__ == '__main__':
    main()
