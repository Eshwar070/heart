from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/janagam')
def janagam():
    return render_template('janagam.html')

@app.route('/warangal')
def warangal():
    return render_template('warangal.html')

@app.route('/hyderabad')
def hyderabad():
    return render_template('hyderabad.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

@app.route('/danger')
def danger():
    return render_template('danger.html')

@app.route('/safe')
def safe():
    return render_template('safe.html')

#login

@app.route('/check', methods = ["POST"])
def check():
    if request.method == "POST":
        n = request.form['name']
        p = request.form['password']
     
    if( n == "admin"  and  p == "admin"):
        return redirect(url_for("prediction"))
    return render_template("index.html")

#prediction 

@app.route('/pre', methods = ["POST"])
def pre():
    if request.method == "POST":
        h = int(request.form['heart'])
        bp = int(request.form['bp'])
        spo2 = int(request.form['spo2'])
        pulse=int(request.form['pulse'])
        print(h+bp+spo2+pulse)
    if(h >= 72 and bp >= 80 and bp <= 120 and spo2 >=95 and pulse<=100):
        return redirect(url_for("safe"))
    else:
        return redirect(url_for("danger"))
     
    return render_template("index.html")

@app.route('/hospital', methods = ["POST"])
def hospital():
    if request.method == "POST":
        n = request.form['town']
     
    if( n == "janagam"):
        return redirect(url_for("janagam"))
    elif( n == "warangal"):
        return redirect(url_for("warangal"))
    elif( n == "hyderabad"):
        return redirect(url_for("hyderabad"))
    return render_template("index.html")

if __name__ == '__main__':
    app.run(port=5000,debug=True)