from flask import Flask
import cgi
import os
import jinja2 

#directory/path to templates. This is needed to use template directory.
template_dir= os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

#rendering a login form
@app.route("/login")
def login():
    template = jinja_env.get_template('login.html')
    return template.render()
#rendering a sign upform
@app.route("/signup")
def signup():
    template = jinja_env.get_template('signup.html')
    return template.render()


#processing a login form
@app.route("/processlogin")
def loginprocessform():
    return 


app.run()