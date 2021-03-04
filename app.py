from flask import Flask, render_template, request
from sklearn.ensemble import RandomForestRegressor
import gunicorn
import pickle

# initiate flask
app = Flask(__name__)

# load model
model = pickle.load(open("model.pkl", "rb"))

# routing
@app.route("/")
def root():
    return render_template("home.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/prediction", methods=["GET", "POST"])
def predict():
    if request.method == "POST":

        transmission = request.form['transmission']
        power = request.form['power']
        gap = request.form['gap']
        fuel = request.form['fuel']
        
        res = round(model.predict([[transmission,power,gap,fuel]])[0], 3)

        result = 'Predicted Price is {} Lakh'.format(res) 
        return render_template('result.html', results = result)
        
    else : 
        return render_template('prediction.html')

if __name__ == '__main__':
    app.run(debug=True)