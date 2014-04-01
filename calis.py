import base64
import sys

if sys.version_info >= (3, 0):
    raw_input = input

from Yowsup.examples.EchoClient import WhatsappEchoClient

wa = WhatsappEchoClient('5212281301632', 'asdfasdf')
pss = base64.b64decode(bytes('tlu5MSojcuXy13AbquA3SUV5e/0='.encode('utf-8')))
wa.login(5218112813034, pss)







import sleekxmpp


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