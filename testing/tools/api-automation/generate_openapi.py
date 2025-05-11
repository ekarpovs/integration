import requests
import yaml
import json
import os

# Configuration
API_URL = "http://localhost:8051/openapi.json"  # Adjust if needed
OUTPUT_DIR = "data/openapi_schemas"

# Ensure the output directory exists
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def download_openapi_json(url, output_path):
    """Downloads OpenAPI JSON from URL and saves to file."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

        data = response.json()

        with open(output_path, "w") as f:
            json.dump(data, f, indent=2)  # Save with indentation for readability

        print(f"OpenAPI JSON downloaded successfully to {output_path}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading OpenAPI JSON: {e}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def convert_json_to_yaml(json_path, yaml_path):
    """Converts JSON to YAML and saves to file."""
    try:
        with open(json_path, "r") as json_file:
            data = json.load(json_file)

        with open(yaml_path, "w") as yaml_file:
            yaml.dump(data, yaml_file, indent=2)

        print(f"JSON converted to YAML successfully. Saved to {yaml_path}")

    except FileNotFoundError:
        print(f"Error: JSON file not found at {json_path}")
    except yaml.YAMLError as e:
        print(f"Error converting JSON to YAML: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Paths for output files
    json_output_path = os.path.join(OUTPUT_DIR, "openapi.json")
    yaml_output_path = os.path.join(OUTPUT_DIR, "api_schema.yaml")

    # 1. Download OpenAPI JSON
    download_openapi_json(API_URL, json_output_path)

    # 2. Convert JSON to YAML
    convert_json_to_yaml(json_output_path, yaml_output_path)
