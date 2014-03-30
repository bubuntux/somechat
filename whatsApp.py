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
import base64
import sys

import webapp2
from google.appengine.ext import ndb

from Yowsup.examples.EchoClient import WhatsappEchoClient

if sys.version_info >= (3, 0):
    raw_input = input

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('<html><body>')
        self.response.out.write("""
          <form action="/send" method="post">
            <div><textarea name="content" rows="3" cols="60"></textarea></div>
            <div><input type="submit" value="Sign Guestbook"></div>
          </form>
        </body>
      </html>""")


class SendMessage(webapp2.RequestHandler):
    def post(self):
        wa = WhatsappEchoClient('5212281301632', self.request.get('content'))
        pss = base64.b64decode(bytes('tlu5MSojcuXy13AbquA3SUV5e/0='.encode('utf-8')))
        wa.login(5218112813034, pss)
        self.redirect('/whatsapp')


app = webapp2.WSGIApplication([('/whatsapp', MainPage), ('/send', SendMessage)], debug=True)