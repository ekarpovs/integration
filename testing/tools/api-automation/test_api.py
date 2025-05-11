import schemathesis
import pytest
import requests

# Load the schema from the YAML file
schema = schemathesis.from_path("data/openapi_schemas/api_schema.yaml")

# API Base URL (Update this to match your actual API)
BASE_URL = "http://localhost:8051"

@schema.parametrize()
def test_api(case):
    # Exclude specific cases (e.g., based on path)
    if case.path.startswith("/feed-records"):
        pytest.skip("Skipping /feed-records endpoint")
    if case.path.startswith("/upload"):
        pytest.skip("Skipping /upload endpoint")
    # Or, exclude based on method
    if case.method == "DELETE":
        pytest.skip("Skipping DELETE method")
    if case.method == "POST":
        pytest.skip("Skipping POST method")

    response = case.call(base_url=BASE_URL)
    case.validate_response(response)

# Use a single test
# @pytest.mark.parametrize("case", schema["/users"]["post"])
# def test_create_user(case):
#     # Execute the test case
#     response = case.call(base_url=BASE_URL)
#     # Validate the response
#     case.validate_response(response)

# @pytest.mark.parametrize("case", schema["/users/{user_id}"]["get"])
# def test_get_user(case):
#     # Generate a valid user ID, or use a fixture
#     # For simplicity, assume ID=1 exists
#     case.replace_path_parameter("user_id", 1)
#     response = case.call(base_url=BASE_URL)
#     case.validate_response(response)
