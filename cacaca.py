import logging

import sleekxmpp

logging.basicConfig(level=logging.DEBUG)


class SendMsgBot(sleekxmpp.ClientXMPP):
    """
    A basic SleekXMPP bot that will log in, send a message,
    and then log out.
    """

    def __init__(self, jid, password, recipient, message):
        sleekxmpp.ClientXMPP.__init__(self, jid, password)

        # The message we wish to send, and the JID that
        # will receive it.
        self.recipient = recipient
        self.msg = message

        # The session_start event will be triggered when
        # the bot establishes its connection with the server
        # and the XML streams are ready for use. We want to
        # listen for this event so that we we can initialize
        # our roster.
        self.add_event_handler("session_start", self.start, threaded=True)

    def start(self, event):
        self.send_presence()
        self.get_roster()

        self.make_message(self.recipient, self.msg, None, 'chat').send(now=True)

        # Using wait=True ensures that the send queue will be
        # emptied before ending the session.
        self.disconnect()


xmpp = SendMsgBot('bubuntux@chat.facebook.com', '', '-100001710572665@chat.facebook.com', '654')
xmpp.register_plugin('xep_0030')  # Service Discovery
xmpp.register_plugin('xep_0199')  # XMPP Ping
# xmpp.credentials['api_key'] = '1421120408139538'
# xmpp.credentials['access_token'] = 'YdOJUMWShDJaBobmoHnpmVWeHDM'
if xmpp.connect(('chat.facebook.com', 5222)):
    xmpp.process(threaded=False)
    print("Done")
else:
    print("Unable to connect.")