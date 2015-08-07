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
from google.appengine.api import urlfetch
import json

class MainHandler(webapp2.RequestHandler):
    def get(self):
        my_data=urlfetch.fetch('https://en.wikipedia.org/w/api.php?action=query&list=allimages&ailimit=5&aifrom=Albert&aiprop=url%7Cmime&format=json')
        opened_data=my_data.content
        my_loaded_data=json.loads(opened_data)
        my_url=my_loaded_data['query']["allimages"][0]['url']
        self.response.write(my_url)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
