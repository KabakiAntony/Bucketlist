from app import create_app
from flask import render_template

the_configuration = "production"
app = create_app(the_configuration)

@app.route('/')
def root():
    """This is the root of this application"""
    return render_template('index.html')

@app.route('/u/signin')
def user_signin():
    """Return the user sign in page"""
    return render_template('signin.html')

@app.route('/contact')
def contact():
    """Return the contact us page"""
    return render_template('contact.html')



if __name__ == "__main__":
    app.run()

