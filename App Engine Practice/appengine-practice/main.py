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

jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))#this little bit sets jinja's relative directory to match the directory name(dirname) of the current __file__, in this case, helloworld.py


class MainHandler(webapp2.RequestHandler):
    def get(self):
        hello_template = jinja_environment.get_template('templates/hello.html')
        self.response.out.write(template.render())


# / count
# class countHandler(webapp2.RequestHandler):
#     def get(self):
#         for x in range(1,101,1):
#             self.response.write(x)
#             self.response.write(" ")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    # ('/count', countHandler)
], debug=True)
