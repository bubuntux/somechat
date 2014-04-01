import logging

import endpoints
from protorpc import remote
from protorpc import messages
from google.appengine.api import users

import sleekxmpp
from app.Models import *

package = 'Facebook'

logging.basicConfig(level=logging.DEBUG)


class SimpleResponse(messages.Message):
    message = messages.StringField(1)


@endpoints.api(name='facebook', version='v1')
class FacebookApi(remote.Service):
    @endpoints.method(endpoints.ResourceContainer(fb_user=messages.StringField(1, required=True), fb_pss=messages.StringField(2, required=True)),
                      SimpleResponse, path='auth/req', http_method='POST', name='auth.request')
    def auth_request(self, request):
        user = users.get_current_user()
        if user:
            fb_user = request.fb_user
            fb_pss = request.fb_pss

            xmpp = sleekxmpp.ClientXMPP(fb_user + '@chat.facebook.com', fb_pss)
            xmpp.register_plugin('xep_0199')  # XMPP Ping
            if xmpp.connect(('chat.facebook.com', 5222)):
                userInfo = UserInfo.query(UserInfo.user == user).get()

                if not userInfo:
                    userInfo = UserInfo(fb_user=fb_user, fb_app=fb_pss)
                else:
                    userInfo.fb_user = fb_user
                    userInfo.fb_app = fb_pss

                userInfo.user = user

                userInfo.put()
                return SimpleResponse(message='Ok')

        return SimpleResponse(message='Invalid user')


APPLICATION = endpoints.api_server([FacebookApi])

