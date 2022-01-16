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

Many version of this exercice is available

# Version 1: Simple version (Tag : v1)

This version is a simple implementation. Only a web server written with Python and Flask. There is no database, the statistic is stored during the run. Restart the webserver will reset the statistic values.

# How to run

You need Python 3 and Flask library. You can create a virtual environment for Python. You can download Python in : https://www.python.org/downloads/
This code was tested with Python3.8 on Mac

To make a virtual environment :

```sh
python3 -m venv myenv
source myenv/bin/activate
```

To install all python requirements, use this command :

```sh
pip3 install -r requirements.txt
```
