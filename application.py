from flask import Flask,request,render_template
#import flask_cors
from src.pipeline.prediction_pipeline import CustomeData,PredictionPipeline

application = Flask(__name__)
app = application
app.static_folder="static"
app.template_folder="static/templates"



@app.route("/")
def Home():
    return render_template("home.html")

@app.route("/predict",methods=["GET","POST"])
def predict():
    if request.method=="GET":
        return render_template("home.html")
    else:
        data=CustomeData(holiday=str(request.form.get("holiday")),temp=int(request.form.get("temp")),
        clouds_all=int(request.form.get("clouds_all")),weather_main=str(request.form.get("weather_main")
        ),hour=int(request.form.get("hour")),weekday=str(request.form.get("weekday")))

        df=data.get_data_as_dataframe()

        pred_pipeline=PredictionPipeline()
        pred=pred_pipeline.predict(data=df)[0]

        if pred < 0:
            prediction=0
        else :
            prediction =pred

        return render_template("home.html",results=prediction)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080)