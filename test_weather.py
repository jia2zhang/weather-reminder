import emoji
from weather import recommendation, to_fahrenheit


def test_recommendation_snow():
    result = recommendation("Snow", 70, 60,[])
    assert result == [emoji.emojize(":raised_hands: it's a perfect day for :shirt::jeans:", use_aliases=True), emoji.emojize("it's a snowy day, so wear your snow gear :snowboarder:", use_aliases=True)]

def test_recommendation_drizzle():
    result = recommendation("Drizzle", 70, 60,[])
    assert result == [emoji.emojize(":raised_hands: it's a perfect day for :shirt::jeans:", use_aliases=True), emoji.emojize("it might drizzle, so might want to bring your :umbrella:", use_aliases=True)]

def test_recommendation_rain():
    result = recommendation("Rain", 70, 60,[])
    assert result == [emoji.emojize(":raised_hands: it's a perfect day for :shirt::jeans:", use_aliases=True), emoji.emojize("it's a rainy day, so bring an :umbrella:", use_aliases=True)]

def test_recommendation_thunderstorm():
    result = recommendation("Thunderstorm", 70, 60,[])
    assert result == [emoji.emojize(":raised_hands: it's a perfect day for :shirt::jeans:", use_aliases=True), emoji.emojize("it's going to thunder :zap: , stay in or bring your :umbrella:", use_aliases=True)]

def test_recommendation_clouds():
    result = recommendation("Clouds", 70, 60,[])
    assert result == [emoji.emojize(":raised_hands: it's a perfect day for :shirt::jeans:", use_aliases=True), emoji.emojize("it's a cloudy day :cloud:", use_aliases=True)]

def test_recommendation_snow_low():
    result = recommendation("Snow", 70, 10,[])
    assert result == [emoji.emojize("brrrrr, wear a jacket :grimacing:", use_aliases=True), emoji.emojize("it's a snowy day, so wear your snow gear :snowboarder:", use_aliases=True)]

def test_recommendation_drizzle_high():
    result = recommendation("Drizzle", 90, 60,[])
    assert result == [emoji.emojize(":sweat_drops: it's shorts weather", use_aliases=True), emoji.emojize("it might drizzle, so might want to bring your :umbrella:", use_aliases=True)]

def test_recommendation_clear():
    result = recommendation("Clear", 70, 60,[])
    assert result == [emoji.emojize(":raised_hands: it's a perfect day for :shirt::jeans:", use_aliases=True)]

# def to_fahrenheit(temp_kelvin):
#     return int(((9/5)*(temp_kelvin-273)+32))

def test_fahrenheit():
    result = to_fahrenheit(298)
    assert result == 77
    result2 = to_fahrenheit("298")
    assert result2 == "Please put a valid integer or float."
