## Install all necessary packages
import os, requests, json, csv, datetime, calendar, time
from dotenv import load_dotenv
from datetime import timedelta

## Collect user zipcode 
#> In the future, user can unsubscribe from zipcode and subscribe to a new one via an override
my_zip = input("Please input your zipcode: ") # Need to validate zipcode format & length
#country_code = "us" #> This is the default, may expand this to other countries later if time permits

## Get weather from OpenWeatherMap, while ensuring that personal API key is not exposed
load_dotenv() #> loads contents of the .env file into the script's environment
api_key = os.environ.get("OpenWeatherMap_API_KEY")

# format for current weather: api.openweathermap.org/data/2.5/weather?q=London,uk&APPID={api_key}
# format for forecasted weather: api.openweathermap.org/data/2.5/forecast?zip={my_zip},{country_code}&APPID={api_key}
# api.openweathermap.org/data/2.5/forecast/daily?zip={zip code},{country code}
# request_url = f"https://api.openweathermap.org/data/2.5/weather?zip={my_zip}&APPID={api_key}"
request_url = f"https://api.openweathermap.org/data/2.5/forecast?zip={my_zip}&APPID={api_key}"

response = requests.get(request_url)
parsed_response = json.loads(response.text)
# print(parsed_response)
my_city = parsed_response["city"]["name"]
print("The location you inputted is", my_city)


filepath = os.path.join(os.path.dirname(__file__), "data", "test_data.json") # Write this to the data folder

step_in_date = parsed_response["list"]
## Go into List and make sure "dt_time" matches today's date, this should need a loop 

## Create a main weather list, with ["Weather"][#]["main"] where # should be different values

## Create a weather description list, with ["weather"][#]["description"]

# for n in parsed_response["list"]:
#     if 



# json.dump(parsed_response, filepath)


# #get all the UTCs in order to decipher
# all_utc = []
# for d_utc in parsed_response["list"]:
#     # print(d_utc["dt"])
#     all_utc.append(d_utc["dt"])
# # print(all_utc)
# print(len(all_utc))


# # TODO: FIND THE UTC range for days 1-3:
# # Import calendar, time; calendar.timegm(time.strptime('2000-01-01 12:34:00', '%Y-%m-%d %H:%M:%S'))
# # print(datetime.datetime.now())
# print(datetime.datetime.now()+timedelta(days=1))
# # print(datetime.datetime.now()+timedelta(days=2))
# print(datetime.datetime.now()+timedelta(days=3))
# request_time = ""+datetime.datetime.now().strftime("%Y-%m-%d")
# request_start = ""+(datetime.datetime.now()+timedelta(days=1)).strftime("%Y-%m-%d")
# request_end = ""+(datetime.datetime.now()+timedelta(days=3)).strftime("%Y-%m-%d")
# print(request_time)
# print(request_start)
# print(request_end)
# t_utc = calendar.timegm(time.strptime(request_time, '%Y-%m-%d'))
# t_utc_start = calendar.timegm(time.strptime(request_start, '%Y-%m-%d'))
# t_utc_end = calendar.timegm(time.strptime(request_end, '%Y-%m-%d'))

# print(t_utc)
# print(t_utc_start)
# print(t_utc_end)

# TODO: 