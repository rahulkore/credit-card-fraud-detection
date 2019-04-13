from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import confusion_matrix, precision_score ,auc, roc_curve
from sklearn import svm, tree, linear_model, neighbors, naive_bayes, ensemble, discriminant_analysis, neural_network
from imblearn.over_sampling import SMOTE


app = Flask(__name__)

@app.route('/')
def processing():


    df = pd.read_csv('creditcard.csv')

    df = df.drop(['V28','V27','V26','V25','V24','V23','V22','V20','V15','V13','V8'], axis =1)

    df['Amount_Stand'] = StandardScaler().fit_transform(df['Amount'].values.reshape(-1, 1))

    df = df.drop(['Time', 'Amount'], axis=1)

    y=df["Class"].dropna().astype('int64')

    X = df.drop('Class', axis=1)

    X=X.dropna()

    X_resample, y_resample = SMOTE().fit_sample(X, y)

    X_train, X_test, y_train, y_test = train_test_split(X_resample, y_resample, test_size=0.2, random_state=3)

    predicted = neural_network.MLPClassifier(alpha=1).fit(X_train, y_train).predict(X_test)

    if predicted[len(predicted)-2]==1:
        from flask_mail import Mail, Message

        mail=Mail(app)

        app.config['MAIL_SERVER']='smtp.gmail.com'
        app.config['MAIL_PORT'] = 465
        app.config['MAIL_USERNAME'] = 'rahulkore976@gmail.com'
        app.config['MAIL_PASSWORD'] = 'rahulkore976'
        app.config['MAIL_USE_TLS'] = False
        app.config['MAIL_USE_SSL'] = True
        mail = Mail(app)
        msg = Message('Fraud', sender = 'rahulkore976@gmail.com', recipients = ['rahulkore976@gmail.com'])
        msg.body = "Fraud has been detected in your credit card"
        mail.send(msg)
        return "Fraud detected"
    else:
        return "no fraud"

if __name__ == "__main__":
        app.secret_key = os.urandom(12)
        app.run(debug=True,host='0.0.0.0', port=5000)
