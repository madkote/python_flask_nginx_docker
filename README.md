## Python Flask + Nginx + Docker ##
The example provides the minimal setup to deploy a Flask app by Docker with Zero-Down-Time.
Nginx is used as load balancer and proxy.

## Install and test ##
```
cd app
python -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python app/test_api.py
python app/main.py
deactivate
```

## Deployment ##
```
docker build -t flask-app:latest app/
docker build -t nginx-app:latest nginx/
docker run -d -p 5000  --name flask-app1 flask-app
docker run -d -p 5000  --name flask-app2 flask-app
docker run -d -p 5000  --name flask-app3 flask-app
docker run -d -p 80:80 --name nginx_app1 --link flask-app1:app1 --link flask-app2:app2 --link flask-app3:app3 nginx-app
```
Now access
```
http://192.168.122.1
http://192.168.122.1/api/v1.0/data
curl -i -X GET http://192.168.122.1/api/v1.0/data
```

## Update ##
Update the API version and build docker images. And then replace image by image. Note the serves is up!
```
# update app1
docker build -t flask-app:latest app/
docker stop flask-app1
docker rename flask-app1 flask-app1_old
docker run -d -p 5000  --name flask-app1 flask-app
docker rm flask-app1_old
# update app2
docker stop flask-app2
docker rename flask-app2 flask-app2_old
docker run -d -p 5000  --name flask-app2 flask-app
docker rm flask-app2_old
# update app3
docker stop flask-app3
docker rename flask-app3 flask-app3_old
docker run -d -p 5000  --name flask-app3 flask-app
docker rm flask-app3_old
```
Automate it!

## Automation ##
There is "docker-compose" which allows to automate many things, also scaling. Stay tuned!

