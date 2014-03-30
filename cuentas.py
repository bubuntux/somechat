import cgi
import os

from google.appengine.ext.webapp import template
from google.appengine.api import users
import webapp2
		
class Cuentas(webapp2.RequestHandler):
    def get(self):

        user = users.get_current_user()
        if user:
            template_values = {
                'titulo': 'Cuentas',
                'encabezado': 'Agrega :3'
            }

            path = os.path.join(os.path.dirname(__file__), 'templates','cuentas.html')

            self.response.out.write(template.render(path, template_values))
            
        else:
            greeting = ('<a href="%s">Sign in or register</a>.' % users.create_login_url('/'))
            self.response.out.write('<html><body>%s</body></html>' % greeting)
        

app = webapp2.WSGIApplication([('/cuentas/?', Cuentas)], debug=True)