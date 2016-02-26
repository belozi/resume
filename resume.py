import webapp2
import cgi

resume = open('resume.html').read()
extras = open('extras.html').read()
cover_letter = open('cover_letter.html').read()
apps = open('apps.html').read()
work_exp = open('work_experience.html').read()

class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(resume)

class Extras(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(extras)

class CoverLetter(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(cover_letter)

class Apps(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(apps)

class Experience(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(work_exp)

app = webapp2.WSGIApplication([
            ('/', MainPage),
            ('/extras', Extras),
            ('/cover_letter', CoverLetter),
            ('/apps', Apps),
            ('/experience', Experience),
], debug=True)
