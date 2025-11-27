# Banknote Authentication Flask API

## Overview

This project is an end-to-end machine learning API that predicts the authenticity of banknotes using statistical features. It uses a pre-trained scikit-learn model and exposes prediction endpoints via a Flask REST API. Interactive documentation is provided via Swagger UI at `/apidocs`.

## Features

- Predict single or batch banknote authenticity
- Swagger/OpenAPI documentation (`/apidocs`)
- Can be run locally or via Docker

## Requirements

- Python 3.7+
- See `requirements.txt` for Python package dependencies

## Setup

### 1. Clone the repo (or use your own repo link)

```bash
git clone https://github.com/HarithaMihimal/Banknote-Authentication-Flask-API.git
```

### 2. Create and activate a virtual environment (recommended)

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Put the pre-trained `classifier.pkl` file in the root directory

### 5. Run the API

```bash
python flask_api_copy.py
```

The app will be available at http://127.0.0.1:5000
Swagger UI docs: http://127.0.0.1:5000/apidocs

## API Endpoints

### `GET /predict`

Query params:

- `variance` (number, required)
- `skewness` (number, required)
- `curtosis` (number, required)
- `entropy` (number, required)

**Example:**

```
GET http://127.0.0.1:5000/predict?variance=0.5&skewness=-3&curtosis=2&entropy=1
```

### `POST /predict_file`

Form data:

- `file`: CSV file (comma-separated, columns: variance, skewness, curtosis, entropy)

**Example using curl:**

```
curl -X POST -F "file=@BankNote_Authentication.csv" http://127.0.0.1:5000/predict_file
```

## Docker (optional)

Build the docker image:

```bash
docker build -t banknote-api .
```

Run the API in a container:

```bash
docker run -p 5000:5000 banknote-api
```

## Notes & Best Practices

- Always use a virtual environment for development
- `classifier.pkl` should be generated/trained using the same scikit-learn version as the deployed environment
- Swagger UI is available at `/apidocs` for easy testing

## Contributing

Pull requests and issues are welcome!

## License

[MIT](LICENSE)
