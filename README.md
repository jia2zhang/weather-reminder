# weather-reminder 

# Make sure to get your own API Key

1. Go to https://home.openweathermap.org/users/sign_up
2. Fill in your own information: Username, E-mail Address, and Password
3. Find your API key on the 'API Key' tab in your account


# Create an .env file to store personal credentials, such as API Key

Place your secret API key in the '.env' file:
```sh
OpenWeatherMap_API_KEY="abc123"
```

Finally, double check to make sure '.env' is added to the '.gitignore' file.


# Create & Activate new anaconda virtual environment
```sh
conda create -n weather-env python=3.7 # (first time only)
conda activate weather-env
```


# Install the required packages
```sh
pip install -r requirements.txt
```

# Setting up Twilio SMS Capabilities

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
