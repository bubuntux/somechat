from google.appengine.ext import ndb


class Contacto(ndb.Model):
    tel_country_code = ndb.IntegerProperty()
    tel = ndb.IntegerProperty()
    face_id = ndb.StringProperty()


class UserInfo(ndb.Model):
    user = ndb.UserProperty()
    fb_user = ndb.StringProperty()
    fb_app = ndb.StringProperty()
    whats_app_info = ndb.StringProperty()
    contacto = ndb.StructuredProperty(Contacto)
    contactos = ndb.StructuredProperty(Contacto, repeated=True)
