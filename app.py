from flask import Flask,render_template,request,jsonify
import pickle
import pandas


#from flask_cors import CORS, cross_origin
import numpy as np

app=Flask(__name__,template_folder='template')
#CORS(app)

model=pickle.load(open('xgb1.pkl','rb'))

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/predict',methods = ['POST'])
def predict():
    feature_1 = np.int64(request.form['Type'])
    feature_2=np.float64(request.form['AT'])
    feature_3=np.float64(request.form['PT'])
    feature_4=np.int64(request.form['RS'])
    feature_5=np.float64(request.form['T'])
    feature_6=np.int64(request.form['TW'])
    temp=pandas.DataFrame({'Type': [feature_1], 'AT': [feature_2],'PT':[feature_3],'RS':[feature_4],'T':[feature_5],'TW':[feature_6]})
    pred=model.predict(temp)
    
    return render_template("predict.html",f1=feature_1,f2=feature_2,f3=feature_3,f4=feature_4,f5=feature_5,f6=feature_6,pred_1=pred)

    


if __name__ =="__main__":
    app.run(debug =True)