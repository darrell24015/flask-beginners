from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <html>
            <head>
            <title>Index Page</title>
            </head>
                <body>
                    <h1>Hello, welcome to my Flask App</h1> 
                    <p><a href="/">Home</a> | <a href="/about">About</a></p>
                </body>
        </html>
    '''


@app.route('/about')
def about():
    return '''
        <html>
            <head>
            <title>About Page</title>
            </head>
                <body>
                    <h1>About this App</h1> 
                    <p><a href="/">Home</a> | <a href="/about">About</a></p>
                </body>
        </html>
    '''
