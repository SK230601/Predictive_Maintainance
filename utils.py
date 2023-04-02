import config
import json
import pickle
import numpy as np

class PREDICTIVE_MAINTAINANCE():
    def __init__(self,Type,Air_temperature,Rotational_speed,Torque,Tool_wear):
        self.Type = Type
        self.Air_temperature = Air_temperature
        self.Rotational_speed = Rotational_speed
        self.Torque = Torque
        self.Tool_wear = Tool_wear

    def load_model(self):
        with open(config.MODEL_PATH_DT,"rb") as f:
            self.model = pickle.load(f)
        with open(config.SCALING_PATH,"rb") as f1:
            self.scaling = pickle.load(f1)
        with open(config.JSON_PATH,"r") as f2:
            self.json_data = json.load(f2)   

    def get_Predict_maintainance(self):
        self.load_model()
        array = np.zeros(len(self.json_data["columns"]),dtype=float) 
        array[0] = self.Air_temperature
        array[1] = self.Rotational_speed
        array[2] = self.Torque
        array[3] = self.Tool_wear

        Type_index = self.json_data["columns"].index(self.Type)
        array[Type_index] = 1

        array1 = self.scaling.transform([array])
        print("Input Array for Model = ",array1)
        pred_default = self.model.predict(array1)[0]
        return pred_default

if __name__ == "__main__":
    Type                  = "L"
    Air_temperature       = 298.9
    Rotational_speed      = 2861.0
    Torque                = 4.6
    Tool_wear             = 143
    obj = PREDICTIVE_MAINTAINANCE(Type,Air_temperature,Rotational_speed,Torque,Tool_wear)
    res = obj.get_Predict_maintainance()
    print("Predicted Maintainance - ",res)