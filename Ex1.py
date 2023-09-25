from flask import Flask, request, make_response, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = '5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'


@app.route('/')
def index():
    if request.cookies.get('username'):
        return render_template('main.html', name=request.cookies.get('username'))
    else:
        return redirect(url_for('login'))


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        response = make_response(redirect(url_for('index')))
        response.set_cookie('username', request.form.get('username'))
        response.set_cookie('mail', request.form.get('mail'))
        # return redirect(url_for('index'))
        return response
        return render_template('main.html', name=request.cookies.get('username'))
    return render_template('login.html')


@app.route('/logout/')
def logout():
    response = make_response(redirect(url_for('index')))
    response.set_cookie('username', "")
    response.set_cookie('mail', "")
    return response


if __name__ == '__main__':
    app.run(debug=True)
