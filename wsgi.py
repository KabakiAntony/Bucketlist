from app import create_app

app = create_app()

@app.route('/')
def root():
    """This is the root of this application"""
    return '<h2 style="color:white;text-align:center;background:black;">Hello and welcome to Bucketlist\
        done by <a style="color:white;" href="https://twitter.com/kabakikiarie">Kabaki Kiarie</a></h2>\
        <h3 style="text-align:center;">To access resources use the endpoint /lists</h3>'

if __name__ == "__main__":
    app.run(debug=True,port=8080)

