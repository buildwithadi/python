from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return '<h1>Welcome to the flask course</h1>'

@app.route('/index', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f"My name is {name}"
    return render_template('form.html')



if __name__ == '__main__':
    app.run(debug=True)