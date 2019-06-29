## Install all necessary packages
import os, requests, json, csv, datetime, calendar, time, dateutil, zipcodes
from dotenv import load_dotenv
from datetime import timedelta
from dateutil import tz

## TODO: Implement Zipcode Validator 
# Source: <https://pypi.org/project/zipcodes>
while True:
    ## TODO: Collect user zipcode 
    my_zip = input("Please input your zipcode: ")
    #country_code = "us" #> This is the default, may expand this to other countries later if time permits
    try:
        zipcodes.matching(str(my_zip))
    except ValueError as error:
        print(error)
        continue

    ## TODO: Get weather from OpenWeatherMap, while ensuring that personal API key is not exposed
    load_dotenv() #> loads contents of the .env file into the script's environment
    api_key = os.environ.get("OpenWeatherMap_API_KEY")

    ## TODO: Download data and get city name
    request_url = f"https://api.openweathermap.org/data/2.5/forecast?zip={my_zip}&APPID={api_key}"
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    try:
        my_city = parsed_response["city"]["name"]
    except KeyError as error:
        print("This is not a valid zipcode. Please try again!")
        continue
    # print(response)
    # print(parsed_response)
    print("The location you inputted is", my_city)


    filepath = os.path.join(os.path.dirname(__file__), "data", "test_data.json") # Write this to the data folder

    step_in_date = parsed_response["list"]

    ## TODO: FIND THE UTC range from now until end of day tomorrow to get the forecast range for tomorrow:
    # Source 1: <https://stackoverflow.com/questions/79797/how-to-convert-local-time-string-to-utc>
    request_time = ""+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    request_end = ""+(datetime.datetime.now()+timedelta(days=2)).strftime("%Y-%m-%d 00:00:00")
        # print("Request Time is " + request_time)
        # print("Request End Time is " + request_end)

    t_utc = calendar.timegm(time.strptime(request_time, '%Y-%m-%d %H:%M:%S'))
    t_utc_end = calendar.timegm(time.strptime(request_end, '%Y-%m-%d %H:%M:%S'))
        # print("UTC Request Time is " + str(t_utc))
        # print("UTC Request End Time is " + str(t_utc_end))

    ## TODO: Create a today's main weather list, with ["Weather"][#]["main"] where # should be different values
    weather_main = []
    for l in parsed_response["list"]:
        # print(l["dt_txt"])
        if l["dt"] < t_utc_end:
            # for m in l["weather"]:
            print(l["dt_txt"] + l["weather"][0]["main"])
            weather_main.append(l["weather"][0]["main"])
    print(weather_main)
    break
    ## TODO: Create a today's temperature list, making sure that Kelvin is converted to Fahrenheit


    ## Create a weather description list, with ["weather"][#]["description"]

    # for n in parsed_response["list"]:
    #     if 



    # #get all the UTCs in order to decipher
    # all_utc = []
    # for d_utc in parsed_response["list"]:
    #     # print(d_utc["dt"])
    #     all_utc.append(d_utc["dt"])
    # # print(all_utc)
    # print(len(all_utc))


