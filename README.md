# JESSICA'S TOMORROW FORECAST REMINDER (TFR) 

Thank you for your interest in Jessica's TFR program! In order to utilize my program, please read and follow the instructions below: 

    + FORK this repository to your GitHub account
    + CLONE this repository to your localhost
    + Open/Navigate to this repository on your GitHub Desktop
    + Acquire your own OpenWeatherMap_API_KEY on <OpenWeatherMap.org>
    + Create and activate your own TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, SENDER_SMS, and RECIPIENT_SMS credentials on <Twilio.com>
    + Follow the rest of the instructions below and you'll be all set!

## Software Requirements

The following software are required to execute and run this TFR program:

    + Python 3.7
    + Anaconda Version 3.7
    + Visual Studio Code text editor
    + GitHub Desktop
    + Git Bash (Windows)

For more information on installation, please use the instructions on my professor's GitHub: <https://github.com/prof-rossetti/nyu-info-2335-201905/blob/master/units/unit-0.md>

## Setup

Navigate to the repository using either Terminal or Git Bash
```sh
cd ~/weather-reminder
```

## Create & Activate new anaconda virtual environment

Run the following from your command line:
```sh
conda create -n weather-env python=3.7 # (first time only)
conda activate weather-env
```

## Install the required packages

Run the following from your command line:
```sh
pip install -r requirements.txt
```

## Security Requirements

If you haven't done so already, make sure to get your own API Key for OpenWeatherMap.org

1. Go to https://home.openweathermap.org/users/sign_up
2. Fill in your own information: Username, E-mail Address, and Password
3. Find your API key on the 'API Key' tab in your account
4. Create an .env file to store personal credentials, such as API Key

On VS Code, place your secret API key in the '.env' file:
```sh
OpenWeatherMap_API_KEY="abc123"
```

Finally, double check to make sure '.env' is added to the '.gitignore' file.

## Setting up Twilio SMS Capabilities

(CREDIT ATTRIBUTION: The following Twiliio setup instruction was provided by my professor: https://github.com/prof-rossetti/nyu-info-2335-201905/blob/master/notes/python/packages/twilio.md)

Create a Twilio account on <https://www.twilio.com/try-twilio>

Then create a new project with "Programmable SMS" capabilities. And from the console, view that project's Account SID and Auth Token. Update the contents of the ".env" file to specify these values as environment variables called TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN, respectively.

You'll also need to obtain a Twilio phone number to send the messages from. After doing so, update the contents of the ".env" file to specify this value (including the plus sign at the beginning) as an environment variable called SENDER_SMS. If you have trouble finding your SENDR_SMS number, you can go <https://www.twilio.com/console/phone-numbers/incoming>

Finally, set an environment variable called RECIPIENT_SMS to specify the recipient's phone number (including the plus sign at the beginning). If you have trouble sending to a verified number, you can add a new verified number here so that this number can receive SMS message from Twilio <https://www.twilio.com/console/phone-numbers/verified>

At the end of this setup, your ".env" file should have the following additional information:
```sh
TWILIO_ACCOUNT_SID = "AC____"
TWILIO_AUTH_TOKEN = "abc123"
SENDER_SMS = "+11234567890"
RECIPIENT_SMS = "+11234567890"
```

NOTE: The SMS capability can be expanded by purchasing the full version of the Twilio Programmable SMS capability, including purchasing your own phone number and paying per SMS message. 

## RUN THE PROGRAM

Once all of the steps above is completed and successful, run the following from the command line:
```sh
python weather.py
```


### (If you wish...) Run PYTEST on command line

Run the following from your command line:
```sh
pytest
```