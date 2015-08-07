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
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):

        self.response.write(
        '<html>'
        '<body>'
        '<h1>Hello world!</h1>'
        '</body>'
        '</html>')

class ImageHandler(webapp2.RequestHandler)
    def get(self):
        template=
        template=jinja_environment.get_template('template/template.html')
        self.response.out.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler,
    '/image', imageHandler)
], debug=True)
