# Docker Demo
This is quick work through to build &amp; containerize web application using docker &amp; python 

Before going start our practical below requirements need to present on machine.

1. docker
2. python3
3. pip3
4. virtualenv
5. docker hub account. (You can create docker hub account by registering this site.)

You can check above mention requirments are present on your machine by running below commands in your terminal.

```
docker --version
python3 --version
pip3 --version
virtualenv --version
```
## Let's build our web application

Go to your terminal create a directory & locate to that directory.

```
mkdir project && cd project
```

First we will need to create a virtual environment & activate virtual environment.

```
virtualenv venv
source venv/bin/activate
```

Let's install our packeges using pip3. In this case we are use only flask.

```
pip3 install flask
```

Now let's create app.py file & copy below program code in to your app.py

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello GPEL"

if __name__ == "__main__":
    app.run()
```
Now let's run our web app on localy. Type below command on your terminal.

```
python3 -m flask run --host=0.0.0.0 --port=8080
```
 Now you'll see ip address along with 8080 port number. Open that in your web browser. You will see our web application is running on smoothly.

 ## Now let's create our container along with the dependancies.

 Firstly, We need to identify our dependancie/libries. Using below command we can export libries in 1 file.

 ```
pip3 freeze > requirements.txt
```

Deactivate virtual environment.

 ```
deactivate
```

In order to containerize our application we need to create Dockerfile. Using below command we can create Dockerfile & open it with any code editing tool.

 ```
touch Dockerfile
```

Copy pase below code in to your Dockerfile.

 ```docker
#Base image
FROM python:3.10.0b3-alpine3.14

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY app.py app.py

EXPOSE 8080

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8080"]
```

Let's build our docker image.

 ```
docker build -t yourname/webapp .
```

Let's run our docker image

 ```
docker run -dp 80:8080 yourname/webapp
```

Go to your browser & hit below addess in the addess bar.

 ```
localhost
```

## Let's push docker image into dockerhub


First of all need to login dockerhub account. After fireing below you'll have to put your docker hub credentials.
 ```
docker login
```

Push local image to dockerhub(Public repo)
 ```
docker push dockerusername/webapp 
```

