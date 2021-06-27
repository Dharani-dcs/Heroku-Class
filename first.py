#an object of wsgi application
from flask import Flask,redirect,url_for,render_template
from flask import *

app=Flask(__name__)
#which url i want to access
@app.route('/')
def hello():
    return render_template('index.html')
@app.route("/course")
def course():
    return '<h1> flask basic tutorial</h1>'
@app.route('/<name>')
def user(name):       
    return f'<h1> hello {name}! welcom!!</h1>'


@app.route('/submit',methods=['POST','GET'])
def submit():
    marks=0
    if request.method=='POST':
        phy=float(request.form['physics'])
        ch=float(request.form['chemistry'])
        math=float(request.form['maths'])
        total=(ch+math+phy)/3
    result=total
    return redirect(url_for('success',marks=result)) 
        


@app.route('/about')
def about(): 
    return render_template('about.html')

@app.route('/result/<int:marks>')
def results(marks):
    
    return redirect(url_for('success',marks=marks))     
@app.route('/successs/<int:marks>') 
def success(marks):
    final=""      
    if marks<45:
        final='Fail'
    else:
        final='pass'
    exp={'number':marks,'result':final}    
    return render_template('result.html',result=exp)    
    
#asking the application to run the program    
if __name__=='__main__':
    app.run(debug=True)    