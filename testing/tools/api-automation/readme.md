## Workflow with Schemathesis

### Prerequisites
```bash
pip install schemathesis
```

### Prepare Your OpenAPI Schema
```bash
 python generate_openapi.py
```

### Change the OpenAPI Schema version
    - Open the api_schema.yaml  
    - Find the property "openapi:"  
    - Change its value from 3.1.0 to  3.0.3  

### Write the Pytest Test with Schemathesis

### Run the Tests
```bash
pytest test_api.py
```

### Run the Tests with the HTML report
```bash
pytest test_api.py --html=data/report.html
```

### Run the Tests with the allure report
```bash
pytest test_api.py --alluredir=data/allure-results
```

### Serve the Allure report using Docker:
#### 1. Start the Service:
Run the Docker image in detached mode. This will start the Allure Docker service in the background.
```bash
docker run --name allure-service -d -p 5050:5050 \
    -v $(pwd)/data/allure-results:/app/allure-results \
    frankescobar/allure-docker-service
```
#### 2. Generate Report:
Use the container's API to generate the report.
```bash
docker exec allure-service allure generate --clean /app/allure-results
```
#### 3. Open Allure Report
Open your web browser and navigate to http://localhost:5050 to view the Allure report.

#### 4. Stop the service:
```bash
docker stop allure-service && docker rm allure-service
```

### Extend and Automate
    - Add more scenarios: Schemathesis can generate a wide variety of payloads based on your schema, including edge cases.   
    - Use hooks or fixtures: To set up preconditions (e.g., create a user before testing retrieval).   
    - Integrate into CI pipeline for continuous testing.   

### Summary
    - Define your API behavior with an OpenAPI schema.  
    - Use Schemathesis to generate test cases automatically.  
    - Call the tests within pytest, validating responses against your schema.  
    - Extend tests easily by parameterizing or customizing the generated scenarios.  

###  Automatically create the api_schema.yaml from the swagger doc

### If you have the Swagger doc in JSON or YAML:
    - Use it directly as your schema file (api_schema.yaml).  
    - If your doc is in OpenAPI format, no conversion needed.  

### Generate an OpenAPI schema from API (Reverse Engineering)
    - FastAPI / Flask / Other Frameworks with Swagger Support  
    -  Swagger/OpenAPI Generators for Existing APIs  
    - OpenAPI Generator CLI (Generate an OpenAPI spec from an existing server with 
    the right adapters or by defining the API in code.)
```bash
npm install @openapitools/generator-cli -g
```  


# REST API Testing with Model Context Protocol (MCP), Pytest, and Schemathesis

This guide demonstrates how to implement Model Context Protocol (MCP) for REST API testing, integrated with Pytest and Schemathesis. It includes steps for creating OpenAPI schemas, generating tests, and automating the process.

## 1. Introduction to MCP, Pytest, and Schemathesis

- **Model Context Protocol (MCP)**: A framework for defining and managing test scenarios based on model-driven testing approaches.
- **Pytest**: A popular Python testing framework.
- **Schemathesis**: A tool that generates property-based tests from OpenAPI/Swagger schemas, integrates with pytest, and provides automated fuzz testing and response validation.

## 2. Setting Up Your Environment

1.  **Install Python Dependencies**:
```bash
pip install fastapi uvicorn schemathesis pytest requests pyyaml
```

## 3. Creating an OpenAPI Schema

### 3.1. Generating the Schema from a FastAPI Application

If you're using FastAPI, you can automatically generate an OpenAPI schema:

    1.  Access the schema in JSON format: `http://<your-server>:8000/openapi.json`

    2.  Download the schema:
```bash
curl http://localhost:8000/openapi.json -o openapi.json
```

    3.  Convert the JSON schema to YAML format (optional):
```bash
pip install pyyaml
python -c "import sys, yaml; yaml.safe_dump(yaml.safe_load(open('openapi.json')), sys.stdout)" > api_schema.yaml
```

## 4. Writing Test Cases with Schemathesis

1.  **Create a Test File** (`test_api.py`):

```python
import schemathesis
import pytest
import requests

# Load the schema from the YAML file
schema = schemathesis.from_path("openapi_schemas/api_schema.yaml")

# API Base URL
BASE_URL = "http://localhost:8000"

@schema.parametrize()
def test_api(case):
    response = case.call(base_url=BASE_URL)
    case.validate_response(response)
```

## 5. Running Tests

1.  Execute the tests with Pytest:
```bash
pytest test_api.py
```

## 6. Excluding Tests

To exclude specific tests or parts of your API, you can use several options:

### 6.1. Exclude Based on Path Regex

```bash
pytest test_api.py --filter-path="/admin" # Exclude all paths starting with /admin
```

### 6.2. Exclude Based on HTTP Method
```bash
pytest test_api.py --filter-method=GET
```

### 6.3. Conditionally Skip Cases
```python
import schemathesis
import pytest
import requests

schema = schemathesis.from_path("openapi_schemas/api_schema.yaml")
BASE_URL = "http://localhost:8000"

@schema.parametrize()
def test_api(case):
    # Exclude specific cases (e.g., based on path)
    if case.path.startswith("/admin"):
        pytest.skip("Skipping /admin endpoint")
    # Or, exclude based on method
    if case.method == "DELETE":
        pytest.skip("Skipping DELETE method")

    response = case.call(base_url=BASE_URL)
    case.validate_response(response)
```
