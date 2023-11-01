# country_lookup_service
This repository consists of the python code that is used to provide the country name based on the country code provided by the user. This helps the user to avoid the manual and tedious process of obtaining the country name manually.

Below are the key elements of this repo.

1. app.py: Code as a Rest Service
2. country_lookup.py: Initial craft code that provides the country names based on country codes, option to update the data file from the API, supports multiple country codes as input.
3. data.json: Data from the API URL https://www.travel-advisory.info/api is stored into this file.

In order to run this service, below are steps to be followed.

1. Clone this repository into your local: git clone -b main https://github.com/ReshavR/country_lookup_service.git
2. For executing the country_lookup.py script to lookup country name without the Rest service, below are the steps:- 

      2.1. Run the script in your terminal, passing country codes as arguments. For example:
      
      _python country_lookup.py --countryCodes AU US CA_
   
      This will look up and display the country names for the specified country codes.
      
      2.2. To update the data from the API, use the --update flag:
      
      _python country_lookup.py --update_

      This will fetch the latest data from the API and store it in the data.json file.
   
4. For executing the app.py script to run the service as REST, we can follow below steps:


      3.1. Install Flask: To install Flask, run the following command:
        
      _pip install Flask_

      3.2. Run the Service: In your terminal, navigate to the directory where app.py is located and run the Python script using the following command:

      _python app.py_
   
      This will start the Flask application, and you should see output indicating that the service is running.

      3.3. Access the Service:
      
      To access the /health route, open a web browser or use a tool like curl and visit http://localhost:5000/health.
      
      To access the /diag route, visit http://localhost:5000/diag.
      
      To access the /convert route with a specific country code (e.g., AU), visit http://localhost:5000/convert?countryCode=AU.
