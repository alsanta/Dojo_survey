from flask import Flask, render_template, redirect, request, session
import dojo


app = Flask(__name__)
app.secret_key = '11113235'

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def result():
    if not dojo.Dojo.validate_name(request.form):
        return redirect('/')
    new_ninja = dojo.Dojo.new_ninja(request.form)
    return redirect(f'/results/{new_ninja}')

@app.route('/results/<int:ninja_id>')
def results(ninja_id):
    data = {
        'id':ninja_id
    }
    new_ninja = dojo.Dojo.get_ninja_by_id(data)
    return render_template('result.html', new_ninja = new_ninja)

if __name__=="__main__":
    app.run(debug=True)