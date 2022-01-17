This project is a job interview test.

"Exercise: Write a simple fizz-buzz REST server.

The original fizz-buzz consists in writing all numbers from 1 to 100, and just replacing all multiples of 3 by "fizz", all multiples of 5 by "buzz", and all multiples of 15 by "fizzbuzz". The output would look like this: "1,2,fizz,4,buzz,fizz,7,8,fizz,buzz,11,fizz,13,14,fizzbuzz,16,...".

Your goal is to implement a web server that will expose a REST API endpoint that:

Accepts five parameters : three integers int1, int2 and limit, and two strings str1 and str2.

Returns a list of strings with numbers from 1 to limit, where: all multiples of int1 are replaced by str1, all multiples of int2 are replaced by str2, all multiples of int1 and int2 are replaced by str1str2.

The server needs to be:

Ready for production

Easy to maintain by other developers

- Add a statistics endpoint allowing users to know what the most frequent request has been.

This endpoint should:

- Accept no parameter

- Return the parameters corresponding to the most used request, as well as the number of hits for this request"

Many versions of this exercice are available

The API document is in `doc/api.json` and can be opened with OpenAPI ui.  
The folder Webserver contains all source code to run the server.

# Version 1: Simple version (Tag : v1)

(To get this version : `git checkout v1`)
This version is a simple implementation, only with a web server written with Python and Flask. There is no database, the statistic is stored during the run. Restart the webserver will reset the statistic values.

## How to run

You need Python 3 and Flask library. You can create a virtual environment for Python. You can download Python in : https://www.python.org/downloads/
This code was tested with Python3.8 on Mac

To make a virtual environment:

```sh
cd [ROOT_PATH]
python3 -m venv myenv
source myenv/bin/activate
```

To install all python requirements, use this command:

```sh
cd [ROOT_PATH]
pip3 install -r requirements.txt
```

To run the webserver:

```sh
cd [ROOT_PATH]
cd webserver
python main.py
```

You can change the IP Address and port of webserver by setting IP_ADDRESS and PORT, 2 environment variables, the default values are 0.0.0.0 and 8080:

```sh
cd [ROOT_PATH]
cd webserver
IP_ADDRESS=127.0.0.1 PORT=8088 python main.py
```

To test (suppose IP_ADDRESS = 127.0.0.1 or 0.0.0.0 and PORT = 8080):

```sh
curl http://127.0.0.1:8080/fizzbuzz/5/fizz/7/buzz/150
curl http://127.0.0.1:8080/fizzbuzz/7/hi/15/hello/200
curl http://127.0.0.1:8080/fizzbuzz/5/fizz/7/buzz/150

curl http://127.0.0.1:8080/statistic
```

# Version 2: Use docker to get MongoDB, webserver in docker and use swagger-ui to get API documentation

(To get this version: `git checkout v2`)
This version can be production-like. I use Docker to create a webserver container and use mongodb and swagger-ui. It is more like you can find in production.

## What you need:

- Docker
- Internet
- Port 8081 and 8082 free

## How to run:

You only need to use the command `docker-compose up -d` to download containers (mongodb and swagger-ui) and to build the webserver container.

```sh
cd [ROOT_PATH]
docker-compose up -d
```

Be sure all services is set to "starting"

After that, you can test the API with curl:

```sh
curl http://127.0.0.1:8082/fizzbuzz/5/fizz/7/buzz/150
curl http://127.0.0.1:8082/fizzbuzz/7/hi/15/hello/200
curl http://127.0.0.1:8082/fizzbuzz/5/fizz/7/buzz/150

curl http://127.0.0.1:8082/statistic
```

You also can see the API documentation, in a web browser, open the link: http://127.0.0.1:8081
In this page, you can see the documentation of all API and you can try the API. Click on "Try it out" to send a request to webserver.  
If you restart your computer, data are not lost, all your data is stored in mongodb container.

# Limitation

- I didn't use https because I need to generate an Authority certificate and use it to generate a SSL certificate. You need to install the Authority certificate on your computer to recognize my own generated certificate.

- Mongodb docker does not use authentification. It is better to use authentification by setting environment variable in database service and webserver service.
