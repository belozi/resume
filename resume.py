import webapp2
import cgi
import os
import jinja2

JE = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__) + "/templates"))

class MainPage(webapp2.RequestHandler):

    def get(self):
        title = "Robert Belozi Lee"
        tag = ''
        template_vars = {
            'title' : title,
            'tag' : tag
        }
        template = JE.get_template('resume.html')
        self.response.out.write(template.render(template_vars))

class Extras(webapp2.RequestHandler):

    def get(self):
        title = "Robert Belozi Lee"
        tag = 'extra'
        template_vars = {
            'title' : title,
            'tag' : tag
        }
        template = JE.get_template('extras.html')
        self.response.out.write(template.render(template_vars))

class CoverLetter(webapp2.RequestHandler):

    def get(self):
        title = "Robert Belozi Lee"
        tag = 'cover'
        template_vars = {
            'title' : title,
            'tag' : tag
        }
        template = JE.get_template('cover_letter.html')
        self.response.out.write(template.render(template_vars))

class Apps(webapp2.RequestHandler):

    def get(self):
        title = "Robert Belozi Lee"
        tag = "apps"
        template_vars = {
            'title' : title,
            'tag' : tag
        }
        template = JE.get_template('apps.html')
        self.response.out.write(template.render(template_vars))

class Experience(webapp2.RequestHandler):

    def get(self):
        title = "Robert Belozi Lee"
        tag = "experience"
        template_vars = {
            'title' : title,
            'tag' : tag
        }
        template = JE.get_template('work_experience.html')
        self.response.out.write(template.render(template_vars))

app = webapp2.WSGIApplication([
            ('/', MainPage),
            ('/extras', Extras),
            ('/cover_letter', CoverLetter),
            ('/apps', Apps),
            ('/experience', Experience),
], debug=True)
