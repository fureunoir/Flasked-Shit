from flask import Flask
from flask import request
from flask import url_for
import time

app = Flask(__name__)


@app.route('/yuck/', methods=['POST', 'GET'])
def yuck():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                            integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                            crossorigin="anonymous">
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <div id="background-image-container">
                                <img id="background-image" src="/static/img/bgimg.gif" style="opacity: 1; display: block;" width="1440" height="1024">
                            </div>
                            <h1>Auction ends in -timer-</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Ur e-mail here" name="email">
                                    <div class="sugstn">
                                        <textarea class="form-control" id="sgstn" aria-describedby="int" placeholder=">the last price" rows="1" name="about"></textarea>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="accept" name="accept">
                                        <label class="form-check-label" for="accept">captcha will be here</label>
                                    </div>
                                    <button type="submission" class="btn btn-primary">put da price</button>
                                </form>
                            </div>
                          </body>
                        </html>'''

    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['sgstn'])
        return "fckn received"


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
