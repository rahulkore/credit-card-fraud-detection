from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy.orm import sessionmaker
from createuser import *
from createaccount import *
engine = create_engine('sqlite:///tutorial.db', echo=True)
app = Flask(__name__)

@app.route('/')
def home():
        if not session.get('logged_in'):
                return render_template('login.html')
        else:
                return "Hello Boss!"

@app.route('/login', methods=['POST'])
def do_admin_login():
        POST_USERNAME = str(request.form['username'])
        POST_PASSWORD = str(request.form['password'])

        Session = sessionmaker(bind=engine)
        s = Session()
        query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
        result = query.first()
        if result:
            session['logged_in'] = True
            return render_template("credit.html")
        else:
            flash('wrong password!')
            return home()
@app.route('/amount',methods=['POST'])
def credit_process():
    POST_CREDITCARD_NUMBER = str(request.form['creditcard_number'])
    POST_CVV = str(request.form['cvv'])
    POST_AMOUNT = str(request.form['amount'])

    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(Account).filter(Account.creditcard_number.in_([POST_CREDITCARD_NUMBER]), Account.cvv.in_([POST_CVV]) )
    result = query.first()
    if result:
        #session['logged_in'] = True
        #return render_template("credit.html")
        return "completed Transaction"
    else:
        flash('wrong credentials!')
        return home()
if __name__ == "__main__":
        app.secret_key = os.urandom(12)
        app.run(debug=True,host='0.0.0.0', port=4000)
