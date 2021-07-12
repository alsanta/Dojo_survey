from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = '11113235'

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    session['savedName'] = request.form['name']
    session['savedLocation'] = request.form['location']
    session['savedLang'] = request.form['favLang']
    session['savedComments'] = request.form['comments']
    return render_template('result.html', savedName=session['savedName'], savedLocation=session['savedLocation'], savedLang=session['savedLang'], savedComments=session['savedComments'])


if __name__=="__main__":
    app.run(debug=True)