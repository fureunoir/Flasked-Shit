from flask import Flask

app = Flask(__name__, static_url_path='/static')


@app.route('/home/')
def home():
    return '''<body background="static/img/bgimg.gif">

    </body>'''




if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
