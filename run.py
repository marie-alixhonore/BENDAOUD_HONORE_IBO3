from flask import Flask, render_template, request 
import pickle
import json
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method =='POST' :
        model = pickle.load(open('svc_model.pkl', 'rb'))
        
        Nscore = request.form.get('Nscore')
        Escore = request.form.get('Escore')
        Oscore = request.form.get('Oscore')
        Ascore = request.form.get('Ascore')
        Cscore = request.form.get('Cscore')
        Impulsive = request.form.get('Impulsive')
        SensationSeeking = request.form.get('SensationSeeking')
        
        prediction = model.predict([[float(Nscore), float(Escore), float(Oscore), float(Ascore), float(Cscore), float(Impulsive), float(SensationSeeking)]])
        #print(prediction)
        if prediction == 1 :
            resultat = "User :/"
        else : 
            resultat ="Non-User :)"
    return render_template('api.html', prediction = resultat)


if __name__=='__main__':
    app.run(debug=True)