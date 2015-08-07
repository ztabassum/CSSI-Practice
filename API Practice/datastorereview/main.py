#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from google.appengine.ext import ndb

class Answer(ndb.Model):
    question = ndb.StringProperty(required = True)
    answer = ndb.StringProperty(required = True)

class AddHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello')
        user_question = "Will I be Happy"
        our_answer = "Maybe"
        answer_to_store = Answer(
                        question=user_question,
                        answer=our_answer
                       )
        answer_to_store.put()
        self.response.write(answer_to_store.put())

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class SearchHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Search them All!<br>')
        user_question = "Will I be happy tomorrow"
        filtered_search = Answer.query().filter(
                          Answer.question == user_question
                          ).fetch()
        self.response.write(filtered_search)
        for answer in filtered_search:
            self.response.write(string(answer) + "<br>")

class DeleteHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Delete them All!<br>')
        user_question = "Will I be happy tomorrow"
        filtered_search = Answer.query().filter(
                          Answer.question == user_question
                          ).fetch()
        self.response.write(filtered_search)
        for answer in filtered_search:
            answer.key.delete()

class UpdateHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Update them all! <br>")


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/add', AddHandler),
    ('/search', SearchHandler),
    ('/delete', DeleteHandler),
    ('/update', UpdateHandler)
], debug=True)
