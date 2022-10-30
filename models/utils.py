from flask import Flask,render_template,jsonify,request
import pandas as pd
import numpy as np
import pickle
import json 
try:
    import config
except:
    pass

class Bengaluru():
    def __init__(self,availability, size, total_sqft, bath, balcony,area_type):

        self.availability = availability
        self.size = size
        self.total_sqft = total_sqft
        self.bath = bath
        self.balcony = balcony
        self.area_type = "area_type_" + area_type

    def load_model(self):

        try:
            with open(config.MODEL_FILE_PATH,"rb")as f:
                self.model = pickle.load(f)

        except:
            with open("model.pkl","rb")as f:
                self.model = pickle.load(f)

        try:
            with open(config.JSON_FILE_PATH,"r")as f:
                self.data = json.load(f)
        except:
            with open("data.json","r")as f:
                self.data = json.load(f)


        return self.data,self.model

    def predicted_price(self):

        self.load_model()

        area_type_index = self.data["column_name"].index(self.area_type)

        array = np.zeros(len(self.data["column_name"]))

        array[0] = self.data["availability_dict"][self.availability]
        array[1] = self.data["size_dict"][self.size]
        array[2] = self.total_sqft
        array[3] = self.bath
        array[4] = self.balcony
        array[area_type_index] = 1

        predict = self.model.predict([array])[0]
        return np.around(predict,2)

if __name__ == "__main__":
    availability = '(14, 11)'
    size = '1 RK'
    total_sqft = 1056.00
    bath = 2.00
    balcony = 1.00

    area_type = "Built_up_Area"

    obj = Bengaluru(availability, size, total_sqft, bath, balcony,area_type)

    price = obj.predicted_price()
    print(price)
    print(f" Our Predicted house price is {price} Laks -/ ONLY")

