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
cd front
nvm use
npm install
```

### Run
```bash
nvm use
npm run
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

### Run

```bash
. venv/bin/activate
FLASK_RUN_PORT=5023 python -m flask run
```

## Usage

Open url: http://127.0.0.1:5000 # or the url in the terminal output
