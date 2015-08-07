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
import jinja2
import os

my_files = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__))
  extensions=['jinja2.ext.autoescape'],
  autoescape=true)#this little bit sets jinja's relative directory to match the directory name(dirname) of the current __file__, in this case, helloworld.py

class SearchHandler(webapp2.RequestHandler):
    search_template

class MainHandler(webapp2.RequestHandler):
    def get(self):
        cat_number=self.request.get("url_number")
        results_template=my_files.get_template('templates/results.html')
        self.response.out.write(results_template.render({"html_num":cat_number}))
        self.response.write('<br> My Kitten App!')



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/search', SearchHandler),
], debug=True)
