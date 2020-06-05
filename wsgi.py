from app import create_app
from flask import render_template

the_configuration = "production"
app = create_app(the_configuration)

@app.route('/')
def root():
    """This is the root of this application"""
    return render_template('index.html')


if __name__ == "__main__":
    app.run()

