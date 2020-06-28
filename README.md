# flask-beginners

My personal repo for building web applications with Flask. Nothing fancy - just teaching myself something new.

Following along the courses provided by Anthony H. located [here](https://prettyprinted.com/) 

Code and tutorials also on [GitHub](https://github.com/PrettyPrinted) and [YouTube](https://www.youtube.com/c/prettyprintedtutorials) - highly recommended!

## Virtual Environment

This Flask project was built on Windows 10 using a virtual environment. See the following guides:

[Pipenv & Virtual Environments](https://docs.python-guide.org/dev/virtualenvs/) - see Lower level: virtualenv

[Creation of virtual environments](https://docs.python.org/3/library/venv.html) - see instructions for Windows

Of course, you can do the same in MacOS or Linux following instructions for those platforms.  Also, pipevn if you prefer.

### Commands

Initialize virtual environment
``` Python
c:\>python -m venv c:\path\to\env
```
Activate virtual environment
``` Python
C:\Users\SomeUser\project_folder> env\Scripts\activate
```

To stop the virtual environment
```Python
deactivate
```

Launch Flask - see [Flask Quick Start](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
``` Python
flask run
```
Tip: If there are .env or .flaskenv files present (as in the "Flask for Beginners" tutorial), run command "pip install python-dotenv" to use them.

### Adding HTML to a Page
For your first time with Flask, most tutorials start with Hello World like this:

```Python
@app.route('/')
def index():
    return 'Hello World!'
```

Beyond returning a line of text, your next step is to add proper HTML to each page.

``` Python
@app.route('/')
def index():
    return '''
        <html>
            <body>
                <p>Welcome to My Flask App</p>
                <form>
                    <p><input name="number1" /></p>
                    <p><input name="number2" /></p>
                    <p><input type="submit" value="Do calculation" /></p>
                </form>
            </body>
        </html>
    '''
```

