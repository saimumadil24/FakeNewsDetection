#importing libraries
from flask import Flask,render_template,request
import pickle as pk

#creating the app
app=Flask(__name__)

#Loading the model
with open('best_model.pkl','rb') as modfile:
    model,tfdf=pk.load(modfile)

#Defining the route for model prediction
@app.route('/',methods=['POST','GET'])

#creating main function
def main():
    if request.method=='POST':
        text=request.form.get('text')
        if text:
            fin_text=tfdf.transform([text])
            prediction=model.predict(fin_text)
            if prediction=='REAL':
                result='This is a Real News'
            else:
                result='This is a Fake News'
        else:
            result='Paste here a news from your Suspicious news'
    else:
        result=''
    return render_template('home.html',output=result)

#running the python app
if __name__=='__main__':
    app.run(debug=True)