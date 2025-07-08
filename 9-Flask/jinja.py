### Building URL Dynamically
### Variable Rule
### Jinja 2 Template Engine

'''
{{   }} expressions to print output in html
{%   %} conditions, for loops
{#   #} this is for comments
'''

from flask import Flask, render_template, request, redirect, url_for

### WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Welcome to the flask course</h1></html>"

# ## Variable Rule
# @app.route('success/<int:score>')
# def success(score):
#     res = ""
#     if score>=50:
#         res = "PASSED"
#     else:
#         res = "FAILED"

#     return render_template('result.html', result=res)

@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"

    exp={'score':score,'res':res}

    return render_template('result.html',results=exp)


## if condition
# @app.route('/successif/<int:score>')
# def successif(score):
#     return render_template('result.html',results=score)

# @app.route('/fail/<int:score>')
# def fail(score):
#     return render_template('result.html',results=score)

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method == 'POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])

        total_score=(science+maths+c+data_science)/4
    else:
        return render_template('getresult.html')  # first this line will be excute when we hit the url .../submit
    
    return redirect(url_for('success',score=total_score))

if __name__=="__main__":
    app.run(debug=True)