from google.appengine.ext import ndb


class User(ndb.Model):
    user_id = ndb.IntegerProperty()
    pss = ndb.StringProperty()
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    tel_country_code = ndb.IntegerProperty()
    tel = ndb.IntegerProperty()
    face_info = ndb.StringProperty()
    whatsup_info = ndb.StringProperty()
    contacts = Contacts()

class Contacts(ndb.Model):
    users = ndb.StructuredProperty(User, repeated=True)