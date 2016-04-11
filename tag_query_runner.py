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


from bson import Regex
import bson.json_util
import re


class TagQueryRunner:
    def __init__(self, db):
        self.db = db

    def run(self):

        while True:
            tag = self.__get_string('Tag')
            relevance = self.__get_float("Min relevance")
            sentiment = self.__get_float("Min sentiment")

            results = self.do_query(tag, relevance, sentiment)
            if len(results) == 0:
                print('No documents found matching query')
            else:
                print('Result count: ' + str(len(results)))
                for r in results:
                    print(r)

    def do_query(self, tag_part, min_sentiment, min_relevance):
        results = self.db.find({
            'tags': {
                '$elemMatch': {
                    'tag': Regex.from_native(re.compile('.*{0}.*'.format(tag_part))),
                    'sentiment': {'$gte': min_sentiment},
                    'relevance': {'$gte': min_relevance},
                }
            }
        })

        bson_results = []
        for r in results:
            bson_results.append(bson.json_util.dumps(r, sort_keys=True, indent=4))

        return bson_results

    @staticmethod
    def __get_float(msg):
        while True:
            try:
                return float(input(msg + ">> "))
            except ValueError:
                print(msg + ' needs to be a float value')

    @staticmethod
    def __get_string(msg):
        while True:
            result = input(msg + ">> ").strip()
            if result == '':
                print(msg + " can't be empty")
            else:
                return result
