import logging

import sleekxmpp

logging.basicConfig(level=logging.DEBUG)

import endpoints
from protorpc import remote
from protorpc import messages

from google.appengine.api import users

from app.Models import *

package = 'Facebook'


class SimpleResponse(messages.Message):
    message = messages.StringField(1)


@endpoints.api(name='whatsapp', version='v1')
class FacebookApi(remote.Service):
    @endpoints.method(endpoints.ResourceContainer(fb_user=messages.StringField(1, required=True), fb_pss=messages.StringField(2, required=True)),
                      SimpleResponse, path='auth/req', http_method='POST', name='auth.request')
    def auth_request(self, request):
        user = users.get_current_user()
        if user:
            cc = request.cc
            number = request.number

            userInfo = UserInfo.query(UserInfo.user == user).get()

            if not userInfo:
                userInfo = UserInfo(tel=number, tel_country_code=cc)
            else:
                userInfo.tel = number
                userInfo.tel_country_code = cc
            identity = Utilities.processIdentity('')
            cc = str(cc)
            number = str(number)
            wc = WACodeRequestV2(cc, number, identity, 'sms')
            result = wc.send()
            response = SimpleResponse()
            response.price_expiration = str(result['price_expiration'])
            response.pw = str(result['pw'])
            response.login = result['login']
            response.currency = str(result['currency'])
            response.status = str(result['status'])
            response.cost = str(result['cost'])
            response.length = str(result['length'])
            response.method = str(result['method'])
            response.type = str(result['type'])
            response.retry_after = str(result['retry_after'])
            response.price = str(result['price'])
            response.expiration = str(result['expiration'])
            response.reason = str(result['reason'])
            response.param = str(result['param'])
            response.code = str(result['code'])
            response.kind = str(result['kind'])

            if response.pw:
                userInfo.whats_app_info = response.pw

            userInfo.user = user

            userInfo.put()
            return response
        else:
            return SimpleResponse(reason='Invalid user')


xmpp = sleekxmpp.ClientXMPP('bubuntux@chat.facebook.com', '')
xmpp.register_plugin('xep_0030')  # Service Discovery
xmpp.register_plugin('xep_0199')  # XMPP Ping
# xmpp.credentials['api_key'] = '1421120408139538'
# xmpp.credentials['access_token'] = 'YdOJUMWShDJaBobmoHnpmVWeHDM'
if xmpp.connect(('chat.facebook.com', 5222)):
    xmpp.process(threaded=False)
    xmpp.send_presence()
    xmpp.get_roster()
    xmpp.make_message('-100001710572665@chat.facebook.com', '654', None, 'chat').send(now=True)
    xmpp.disconnect()
    print("Done")
else:
    print("Unable to connect.")