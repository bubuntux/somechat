from google.appengine.ext import ndb


class UserInfo(ndb.Model):
    user = ndb.UserProperty()
    tel_country_code = ndb.IntegerProperty()
    tel = ndb.IntegerProperty()
    face_info = ndb.StringProperty()
    whats_app_info = ndb.StringProperty()
    #contacts = Contacts()

class Contacts(ndb.Model):
    users = ndb.StructuredProperty(UserInfo, repeated=True)
