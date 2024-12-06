"""
https://peps.python.org/pep-0008/

3 hardest things in computer sciences:
    - Naming things
    - Cache invalidation
    - N+1 errors
"""

# Avoid "useless" comments but do the code documentation.
# Comments can lie, code cannot
def is_even(number):
    # return True if the number is odd
    return number % 2
# ChatGPT will often fails at explainning this (wrong comments and/or name)

# When you feel like you need a comment, it often means
# you can find a better name or need encapsulation
height = 15
width = 30
if height * width > 100:
    print("is big")

is_big = height * width > 100
if is_big:
    print("is big")

# Early returns / avoid nesting
def is_good_weather(month, temperature):
    if month == "august":
        if temperature > 15:
            return True
        else:
            return False
    return False

def is_good_weather(month, temperature):
    return month == "august" and temperature > 15



# https://developers.google.com/maps/documentation/places/web-service/overview
# Google places python API (Need API Key)
# https://cloud.google.com/speech-to-text/docs/speech-to-text-client-libraries#client-libraries-install-python
class Restaurant:
    def __init__(self, price_min, price_max, city=None, location=None):
        if not (city or location):
            raise ValueError("Need a city or a location")

        self.price_min = price_min
        self.price_max = price_max
        self.city = city
        self.location = location

    def save():
        ...

    @classmethod
    def get_by_city(cls, city):
        f"""SELECT * from restaurant WHERE city = {city}"""

    @classmethod
    def get_by_price_range(cls, price_min, price_max):
        return


def get_closest_open_restaurant(price_range, city=None, coordinates=None):
    return Restaurant()

def speech_to_text(): ... # Google SpeechRecognition

def get_price_range_and_city_from_text(text):
    price_range = [
        float(word) for word in text if text.isnumeric()].sort()
    city = "your logic"
    return price_range, city

def get_values_from_speech():
    text = speech_to_text()
    price_range, city = (
        get_price_range_and_city_from_text(text))
    return price_range, city

def get_closest_open_restaurant_from_speech():
    price_range, city = get_values_from_speech()
    get_closest_open_restaurant(price_range, city)


class String:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        # ord() / chr() -> ascii to str / str to ascii
        # map() / zip() / "".join([list comprehension])
        return String()


assert(String("a") + String("b") == String("c"))
assert(String("abc") + String("abc") == String("bef"))
assert(String("z") + String("a") == String("a"))
