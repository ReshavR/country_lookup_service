import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

API_URL = "https://www.travel-advisory.info/api"
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

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

@app.route('/diag', methods=['GET'])
def diag():
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            return jsonify({"api_status": {"code": 200, "status": "ok"}})
        else:
            return jsonify({"api_status": {"code": response.status_code, "status": "error"}})
    except requests.exceptions.RequestException as e:
        return jsonify({"api_status": {"code": 500, "status": "error"}})

@app.route('/convert', methods=['GET'])
def convert():
    country_code = request.args.get('countryCode')
    country_name = lookup_country_name(country_code)
    return jsonify({"countryCode": country_code, "countryName": country_name})

if __name__ == "__main__":
    app.run()

