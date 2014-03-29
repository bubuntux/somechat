from google.appengine.ext import ndb


class User(ndb.Model):
    user_id = ndb.IntegerProperty()
    pss = ndb.StringProperty()
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    tel_country_code = ndb.IntegerProperty()
    tel = ndb.IntegerProperty()
    supInfo = WhatsupInfo()
    faceInfo = FacebookInfo()
    contacts = Contacts()


class WhatsupInfo(ndb.Model):
    pss = ndb.StringProperty()


class FacebookInfo(ndb.Model):
    pss = ndb.StringProperty()


class Contacts(ndb.Model):
    users = ndb.StructuredProperty(User, repeated=True)
