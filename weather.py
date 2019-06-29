## Install all necessary packages
import os, requests, json, csv, datetime, calendar, time, dateutil
from dotenv import load_dotenv
from datetime import timedelta
from dateutil import tz

## TODO: Collect user zipcode 
#> In the future, user can unsubscribe from zipcode and subscribe to a new one via an override
my_zip = input("Please input your zipcode: ") # Need to validate zipcode format & length
#country_code = "us" #> This is the default, may expand this to other countries later if time permits

## TODO: Get weather from OpenWeatherMap, while ensuring that personal API key is not exposed
load_dotenv() #> loads contents of the .env file into the script's environment
api_key = os.environ.get("OpenWeatherMap_API_KEY")

## TODO: Download data and get city name
request_url = f"https://api.openweathermap.org/data/2.5/forecast?zip={my_zip}&APPID={api_key}"
response = requests.get(request_url)
parsed_response = json.loads(response.text)
my_city = parsed_response["city"]["name"]
print("The location you inputted is", my_city)


filepath = os.path.join(os.path.dirname(__file__), "data", "test_data.json") # Write this to the data folder

step_in_date = parsed_response["list"]

## TODO: FIND THE UTC range from now until end of day:
# Source: <https://stackoverflow.com/questions/79797/how-to-convert-local-time-string-to-utc>
request_time = ""+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
request_end = ""+(datetime.datetime.now()+timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
formatted_request_end = ""+(datetime.datetime.now()+timedelta(days=1)).strftime("%B %d, %Y")

print("Request Time is " + request_time)
print("Request End Time is " + request_end)
print("Request Formatted End Time is " + formatted_request_end)
t_utc = calendar.timegm(time.strptime(request_time, '%Y-%m-%d %H:%M:%S'))
t_utc_end = calendar.timegm(time.strptime(request_end, '%Y-%m-%d %H:%M:%S'))
t_utc_end_formatted = calendar.timegm(time.strptime(formatted_request_end, '%B %d, %Y'))


print("UTC Request Time is " + str(t_utc))
print("UTC Request End Time is " + str(t_utc_end))
print("UTC Formatted Request End Time is "+ str(t_utc_end_formatted))


## Create a main weather list, with ["Weather"][#]["main"] where # should be different values

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


