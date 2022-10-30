
from flask import Flask,render_template,jsonify,request
import config
from models.utils import Bengaluru


app = Flask(__name__)

@app.route("/")
def hello():
    print("hello , how are you....?")
    return render_template("index.html")

@app.route("/predict_price",methods=["POST","GET"])
def predicted_price():

    if request.method == "POST":

        availability = request.form.get("availability")
        size = request.form.get("size")
        total_sqft = eval(request.form.get("total_sqft"))
        bath = eval(request.form.get("bath"))
        balcony = eval(request.form.get("balcony"))
        area_type = request.form.get("area_type")


        obj = Bengaluru(availability, size, total_sqft, bath, balcony,area_type)

        price = obj.predicted_price()
        print(price)
        return render_template("index.html",prediction=price)

if __name__ =="__main__":
    app.run(host="0.0.0.0",port=config.PORT_NUM,debug=True)
    