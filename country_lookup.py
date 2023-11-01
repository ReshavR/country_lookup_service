import requests
import argparse
import json

# API URL
API_URL = "https://www.travel-advisory.info/api"

# Data file to store API response
DATA_FILE = "data.json"

def lookup_country_name(country_code):
    try:
        with open(DATA_FILE, 'r') as data_file:
            data = json.load(data_file)

        if data.get(country_code):
            country_name = data[country_code].get("name", "Country name not found")
            return country_name
        else:
            return "Country code not found"

    except FileNotFoundError:
        return "Data file not found. Please run the program with '--update' to fetch data."

def update_data_file():
    try:
        response = requests.get(API_URL)
        data = response.json()

        if data.get("data"):
            with open(DATA_FILE, 'w') as data_file:
                json.dump(data["data"], data_file, indent=4)
            print(f"Data saved to '{DATA_FILE}'")

        else:
            print("Data not found in the API response.")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Country Code Lookup Tool")
    parser.add_argument("--countryCodes", nargs='+', required=True, help="Country codes to lookup")
    parser.add_argument("--update", action="store_true", help="Update data file from API")

    args = parser.parse_args()

    if args.update:
        update_data_file()

    for country_code in args.countryCodes:
        country_name = lookup_country_name(country_code)
        print(f"Country Name for '{country_code}': {country_name}")

if __name__ == "__main__":
    main()
