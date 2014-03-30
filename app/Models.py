from google.appengine.ext import ndb


class Contacto(ndb.Model):
	tel_country_code = ndb.IntegerProperty()
	tel = ndb.IntegerProperty()
	face_info = ndb.StringProperty()
    

class UserInfo(ndb.Model):
    user = ndb.UserProperty()
    tel_country_code = ndb.IntegerProperty()
    tel = ndb.IntegerProperty()
    face_info = ndb.StringProperty()
    whats_app_info = ndb.StringProperty()
    contactos = ndb.StructuredProperty(Contacto, repeated=True)


