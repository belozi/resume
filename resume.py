import webapp2

resume = open('resume.html').read()
extras = open('extras.html').read()
cover_letter = open('cover_letter.html').read()

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

app = webapp2.WSGIApplication([
            ('/', MainPage),
            ('/extras', Extras),
            ('/cover_letter', CoverLetter),
], debug=True)
