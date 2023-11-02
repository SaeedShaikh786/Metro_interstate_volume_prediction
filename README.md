# Metro Interstate Volume prediction

## Data set Description:
- holiday: |Categorical| US National holidays plus regional holiday, Minnesota State Fair
- temp :|Numeric| Average temp in kelvin
- rain_1h :|Numeric| Amount in mm of rain that occurred in the hour
- snow_1h :|Numeric| Amount in mm of snow that occurred in the hour
- clouds_all :|Numeric| Percentage of cloud cover
- weather_main :|Categorical| Short textual description of the current weather
- weather_description: |Categorical| Longer textual description of the current weather
- date_time :|DateTime| Hour of the data collected in local CST time
- traffic_volume : |Numeric| Hourly I-94 ATR 301 reported westbound traffic volume
- - Dataset link : https://archive.ics.uci.edu/ml/datasets/Metro+Interstate+Traffic+Volume

## docker deployment 
- Docker build checked
- Github workflows ( yaml file)
- Im user in AWS

## Docker Setup In EC2 commands to be Executed
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker

## Configure EC2 as self-hosted runner:
### Setup github secrets:
AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI = demo>> 566373416292.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME = metro_project


## Dagshub mlflow Experiment Tracking :
MLFLOW_TRACKING_URI=https://dagshub.com/saeedshaikh313/Metro_interstate_volume_prediction.mlflow \
MLFLOW_TRACKING_USERNAME=saeedshaikh313 \
MLFLOW_TRACKING_PASSWORD=***** \
python script.py


