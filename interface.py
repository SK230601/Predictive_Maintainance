from flask import Flask,render_template,request
import config
from utils import PREDICTIVE_MAINTAINANCE

app = Flask(__name__)

@app.route("/")
def get_home():
    return render_template("index.html")

@app.route('/Predict', methods=['POST'])
def home():
    Type = request.form['Type']
    Air_temperature = float(request.form['Air_temperature'])
    Rotational_speed = float(request.form['Rotational_speed'])
    Torque = float(request.form['Torque'])
    Tool_wear = int(request.form['Tool_wear'])
    obj = PREDICTIVE_MAINTAINANCE(Type,Air_temperature,Rotational_speed,Torque,Tool_wear)
    res1 = obj.get_Predict_maintainance()
    return render_template("Final.html",data=res1)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=config.PORT_NUM)