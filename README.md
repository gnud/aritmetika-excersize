## Goal

Implement a calculator with operations:
- +, plus (addition)
- −, minus (subtraction)
- ÷, obelus (division)
- ×, times (multiplication)

Rules:
- inputs are:
  - operator type enum
  - two inputs (assumption made due to unspecified requirements) as operands.

# Project Dependencies

Tested on:
- python 3.11.0
- node v18.12.1

System:
- virtualenv to be installed.
- docker to be installed and ready for deployment (optional)

# Deployment Docker

### Initial setup
```bash
docker-compose build
```

### Run

Use this .env:
```dotenv
REACT_APP_API_URL=
REACT_APP_API_BASE=/api
API_URL=http://web:8000
API_REWRITE=/api
```

```bash
docker-compose up -d
```

## Usage

Open url: http://localhost:3060/

# Deployment Dev

## Front
![front_screenshot.png](docs%2Ffront_screenshot.png)

### Initial setup

Use this .env:
```dotenv
REACT_APP_API_URL=http://localhost:3000
REACT_APP_API_BASE=/api
API_URL=http://localhost:5000
API_REWRITE=/api
```

```bash
cd front/calculator_react
nvm use
npm install
```

### Run
```bash
cd front/calculator_react
nvm use
npm start
```

## Usage

Open url: http://localhost:3000 # or the url in the terminal output


## Backend

![Calculate endpoint](docs%2Fback_api_calculate.png)
![Operations endpoint](docs%2Fback_api_operations.png)

### Initial setup

```bash
cd back
virtualenv -p python3 venv
. venv/bin/activate
pip install -r requirements.txt
````

Test by opening http://127.0.0.1:5023/operations
or executing

```bash
curl -v http://127.0.0.1:5023/operations
````

Sample output

```bash
*   Trying 127.0.0.1:5023...
* Connected to 127.0.0.1 (127.0.0.1) port 5023 (#0)
> GET /operations HTTP/1.1
> Host: 127.0.0.1:5023
> User-Agent: curl/7.81.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Server: Werkzeug/3.0.1 Python/3.10.12
< Date: Wed, 29 Nov 2023 11:22:56 GMT
< Content-Type: application/json
< Content-Length: 39
< Connection: close
< 
{"result":["+","-","/","*","^","log"]}
```

### Run

```bash
. venv/bin/activate
FLASK_RUN_PORT=5023 python -m flask run
```

## Usage

Open url: http://127.0.0.1:5000 # or the url in the terminal output
