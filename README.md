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

Finally, make sure '.env' is added to the '.gitignore' file.


# Create & Activate new anaconda virtual environment
```sh
conda create -n weather-env python=3.7 # (first time only)
conda activate weather-env
```


# Install the required packages
```sh
pip install python-dotenv
pip install requests
pip install python-dateutil
```