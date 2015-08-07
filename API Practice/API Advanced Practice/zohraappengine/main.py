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

class Kindergartener(ndb.Model):
  name=ndb.StringProperty(required = True)
  birthday = ndb.DateProperty()
  fav_food=ndb.StringProperty()

class Lunchbox(ndb.Model):

  beverage = ndb.StringProperty()
  sandwich = ndb.StringProperty()
  owner = ndb.KeyProperty(Kindergartener)


kinder2 = Kindergartener(name='Jaqueline')
kinder2_key = kinder2.put()
sandwich_box = Lunchbox(sandwich='Pasta', owner = kinder2_key)
sandwich_box.put()

print sandwich_box.owner

class Player(ndb.Model):
  name = ndb.StringProperty()
  position = ndb.StringProperty()

class Team(ndb.Model):
  city = ndb.StringProperty()
  name = ndb.StringProperty()
  player = ndb.KeyProperty(Player, repeated = True)


player1 = Player(name = 'Rachel', position = 'lineman')
player1.put()
player2 = Player(name = 'Andrew', position = 'quarterback')
player2.put()
players = [player1.key, player2.key]
team1 = Team(city = 'Chicago', name = 'Bears', player = [players])
team1.put()


print team1


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
