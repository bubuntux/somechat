# !/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import endpoints
from protorpc import messages
from protorpc import remote
from endpoints.api_config import AUTH_LEVEL
from google.appengine.api import users

from app.Models import *

from Yowsup.Common.utilities import Utilities
from Yowsup.Registration.v2.regrequest import WARegRequest as WARegRequestV2
from Yowsup.Registration.v2.coderequest import WACodeRequest as WACodeRequestV2

package = 'Whatsapp'


class CodeReqResponse(messages.Message):
    price_expiration = messages.StringField(1)
    pw = messages.StringField(2)
    login = messages.StringField(3)
    currency = messages.StringField(4)
    status = messages.StringField(5)
    cost = messages.StringField(6)
    length = messages.StringField(7)
    method = messages.StringField(8)
    type = messages.StringField(9)
    retry_after = messages.StringField(10)
    price = messages.StringField(11)
    expiration = messages.StringField(12)
    reason = messages.StringField(13)
    param = messages.StringField(14)
    code = messages.StringField(15)
    kind = messages.StringField(16)


class CodeRegResponse(messages.Message):
    price = messages.StringField(1)
    pw = messages.StringField(2)
    retry_after = messages.StringField(3)
    expiration = messages.StringField(4)
    reason = messages.StringField(5)
    status = messages.StringField(6)
    price_expiration = messages.StringField(7)
    login = messages.StringField(8)
    cost = messages.StringField(9)
    kind = messages.StringField(10)
    currency = messages.StringField(11)
    type = messages.StringField(12)


@endpoints.api(name='whatsapp', version='v1')
class WhatsAppApi(remote.Service):
    @endpoints.method(endpoints.ResourceContainer(cc=messages.IntegerField(1, variant=messages.Variant.INT32, required=True),
                                                  number=messages.IntegerField(2, variant=messages.Variant.INT32, required=True)), CodeReqResponse,
                      path='authCode/req', http_method='POST', name='authCode.request', auth_level=AUTH_LEVEL.REQUIRED)
    def authCode_request(self, request):
        user = users.get_current_user()
        if user:
            cc = request.cc
            number = request.number

            key = ndb.Key(UserInfo, user.email()) ## TODO how to get the same

            userInfo = key.get()

            if not userInfo:
                userInfo = UserInfo(tel=number, tel_country_code=cc)

            identity = Utilities.processIdentity('')
            cc = str(cc)
            number = str(number)
            wc = WACodeRequestV2(cc, number, identity, 'sms')
            result = wc.send()
            response = CodeReqResponse()
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
            return CodeReqResponse(reason='Invalid user')

    @endpoints.method(endpoints.ResourceContainer(cc=messages.IntegerField(1, variant=messages.Variant.INT32, required=True),
                                                  number=messages.IntegerField(2, variant=messages.Variant.INT32, required=True),
                                                  code=messages.IntegerField(3, variant=messages.Variant.INT32, required=True)), CodeRegResponse,
                      path='authCode/reg', http_method='POST', name='authCode.register', auth_level=AUTH_LEVEL.REQUIRED)
    def authCode_register(self, request):
        identity = Utilities.processIdentity('')
        wr = WARegRequestV2(str(request.cc), str(request.number), str(request.code), identity)
        result = wr.send()
        response = CodeRegResponse()
        response.price = str(result['price'])
        response.pw = str(result['pw'])
        response.retry_after = str(result['retry_after'])
        response.expiration = str(result['expiration'])
        response.reason = str(result['reason'])
        response.status = str(result['status'])
        response.price_expiration = str(result['price_expiration'])
        response.login = result['login']
        response.cost = str(result['cost'])
        response.kind = str(result['kind'])
        response.currency = str(result['currency'])
        response.type = str(result['type'])
        return response


APPLICATION = endpoints.api_server([WhatsAppApi])