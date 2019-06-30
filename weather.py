## Install all necessary packages
import os, requests, json, csv, datetime, calendar, time, dateutil, zipcodes, pprint, emoji
from dotenv import load_dotenv
from datetime import timedelta
from dateutil import tz
from twilio.rest import Client

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
    ## TODO: Create a today's temperature list, making sure that Kelvin is converted to Fahrenheit
    def to_fahrenheit(temp_kelvin):
        return int(((9/5)*(temp_kelvin-273)+32))

    ## TODO: Create a today's main weather list, with ["Weather"][#]["main"] where # should be different values
    weather_main = []
    weather_temp = []
    for l in parsed_response["list"]:
        # print(l["dt_txt"])
        if l["dt"] < t_utc_end:
            # for m in l["weather"]:
            # print(l["dt_txt"],l["weather"][0]["main"])
            weather_main.append(l["weather"][0]["main"])
            weather_temp.append(to_fahrenheit(l["main"]["temp"]))
    # print(weather_main)
    high_temp = str(max(weather_temp))
    low_temp = str(min(weather_temp))

    # Remove duplicates from weather_main
    weather_main = list(set(weather_main))
    # print(weather_main)

    ## TODO: Create recommendation logic based on weather_main and weather_temp
    # Weather Conditions Documentation: <https://openweathermap.org/weather-conditions>
    gear = []
    def recommendation(weather_description,high,low):
        # TEMPERATURES
        if int(high) > 80:
            gear.append(emoji.emojize(":sweat_drops: it's shorts weather", use_aliases=True))
        elif int(low) < 49:
            gear.append(emoji.emojize("brrrrr, wear a jacket :grimacing:", use_aliases=True))
        else:
            gear.append(emoji.emojize(":raised_hands: it's a perfect day for :shirt::jeans:", use_aliases=True))
        # SNOW
        if "Snow" in weather_description:
            gear.append(emoji.emojize("it's a snowy day! Wear your snow gear :snowboarder:", use_aliases=True))
        # DRIZZLE
        elif "Drizzle" in weather_description:
            gear.append(emoji.emojize("it might drizzle, so might want to bring your :umbrella:", use_aliases=True))
        # RAIN
        elif "Rain" in weather_description:
            gear.append(emoji.emojize("it's a rainy day! Bring your :umbrella:, ella, ella, ey, ey, ey", use_aliases=True))
        # THUNDERSTORM
        elif "Thunderstorm" in weather_description:
            gear.append(emoji.emojize("it's going to thunder :zap: , stay in or bring your umbrella", use_aliases=True))
        elif "Clouds" in weather_description:
            gear.append(emoji.emojize("it's a cloudy day :cloud:", use_aliases=True))
        return gear
        
    
    recommendation(weather_main,high_temp,low_temp)

    content = ""
    if len(gear) == 1:
        content = "Weather for tomorrow suggests that " + str(gear) + f", with a high of {high_temp}F and a low of {low_temp}F"
    else:
        content = "Weather for tomorrow suggests that " + " and ".join(gear) + f", with a high of {high_temp}F and a low of {low_temp}F"
    print(content)
    
    ## TODO: Integrate TWilio to send SMS
    # Your Account SID from <twilio.com/console>
    TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID", "OOPS, please specify env var called 'TWILIO_ACCOUNT_SID'")
    # Your Auth Token from <twilio.com/console>
    TWILIO_AUTH_TOKEN  = os.environ.get("TWILIO_AUTH_TOKEN", "OOPS, please specify env var called 'TWILIO_AUTH_TOKEN'")
    # Your SMS capable phone number from <twilio.com/console/phone-numbers/incoming>
    SENDER_SMS  = os.environ.get("SENDER_SMS", "OOPS, please specify env var called 'SENDER_SMS'")
    # Your Verified phone number that can receive Twilio SMS message from <twilio.com/console/phone-numbers/verified>
    RECIPIENT_SMS  = os.environ.get("RECIPIENT_SMS", "OOPS, please specify env var called 'RECIPIENT_SMS'")

    # AUTHENTICATE

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    # COMPILE REQUEST PARAMETERS (PREPARE THE MESSAGE)

    contents = content

    # ISSUE REQUEST (SEND SMS)

    message = client.messages.create(
        to=RECIPIENT_SMS, 
        from_=SENDER_SMS, 
        body=contents)

    # PARSE RESPONSE

    pp = pprint.PrettyPrinter(indent=4)

    print("----------------------")
    print("SMS")
    print("----------------------")
    print("RESPONSE: ", type(message))
    print("FROM:", message.from_)
    print("TO:", message.to)
    print("BODY:", message.body)
    print("PROPERTIES:")
    pp.pprint(dict(message._properties))


    break