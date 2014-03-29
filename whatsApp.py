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


import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir)
import datetime, sys

if sys.version_info >= (3, 0):
    raw_input = input

from Yowsup.connectionmanager import YowsupConnectionManager

from app.Models import *
from google.appengine.ext import ndb
from google.appengine.api import users



user_key = ndb.Key('UserInfo', '1', 'tel_country_code', '52', 'tel', '18112813034', 'whats_app_info', 'tlu5MSojcuXy13AbquA3SUV5e/0=')


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('<html><body>')


        self.response.out.write("""
          <form action="/sign" method="post">
            <div><textarea name="content" rows="3" cols="60"></textarea></div>
            <div><input type="submit" value="Sign Guestbook"></div>
          </form>
        </body>
      </html>""")


class SendMessage(webapp2.RequestHandler):
    def post(self):
        user_info = user_key.get()
        user_info.
        if users.get_current_user():
            greeting.author = users.get_current_user()

        greeting.content = self.request.get('content')
        greeting.put()
        self.redirect('/whatsapp')


app = webapp2.WSGIApplication([
                                  ('/whatsapp', MainPage), ('/send', SendMessage)], debug=True)
