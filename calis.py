import base64
import sys

if sys.version_info >= (3, 0):
    raw_input = input

from Yowsup.examples.EchoClient import WhatsappEchoClient

wa = WhatsappEchoClient('5212281301632', 'asdfasdf')
pss = base64.b64decode(bytes('tlu5MSojcuXy13AbquA3SUV5e/0='.encode('utf-8')))
wa.login(5218112813034, pss)