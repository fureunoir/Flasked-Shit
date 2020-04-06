from flask import Flask

app = Flask(__name__, static_url_path='/static')


@app.route('/home/')
def home():
    return '''<!DOCTYPE html>
<html>
<head>
</head>
<body>
<div id="background-image-container">
<img id="background-image" src="static/img/bgimg.gif" style="opacity: 1; display: block;" width="1440" height="1024">
</div>
</body>
</html>'''



if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
