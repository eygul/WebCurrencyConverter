# WebCurrencyConverter

## Description
* WebCurrencyConverter, also known as DollarToLira, is an online web app powered by Python, Flask, and Jinja that renders real-time currency values in an accessible way. 
* It currently supports US Dollar, Turkish Lira, Euro, and British Pound with a lot more to come.
* The website is currently powered by a third-party API called Freecurrencyapi, however, it will soon be replaced by an API integrated to the web app.

## Setup Guide
* Fork the project.
* Clone the forked repository.
* Enter your own secret key for app.config in server.py. You can do this by following:
    * Open a Python terminal.
    * Type "import secrets".
    * Type "secrets.token_hex(16)".
    * Copy the random combination of letters and numbers.
    * Replace the "your secret key" in app.config['SECRET_KEY'] = "your secret key" with the string you just copied.
*  Enter your own API endpoint URLs in server.py to connect to the third-party API (until the native API gets released.) You can do this by following:
    * Obtain the necessary API endpoint URLs from your favorite third party API provider.
    * Paste the API endpoint URLs into appropriate places in the server.py
* Run the server.py file.
* Enjoy!

## Contribution Guide
* Same steps as Setup Guide.
* Check the issues posted in the original repo.
* Choose an issue and fix it.
* Post a pull request on that issue. Please make sure you link the issue with the pull request by including the issue number in the pull request. Example: fix issue #26
* If there is an issue you would like to add, please feel free!

