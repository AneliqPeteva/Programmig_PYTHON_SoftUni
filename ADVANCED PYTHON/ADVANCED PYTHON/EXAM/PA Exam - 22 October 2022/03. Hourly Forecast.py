def forecast(*args):
    weathers = {
        "Sunny": [],
        "Cloudy": [],
        "Rainy": [],
}
    result = ""
    for location, weather in args:
        weathers[weather].append(location)

    for weather, location in weathers.items():
        sorted_location = sorted(location)
        for current_location in sorted_location:
            result += f"{current_location} - {weather}\n"

    return result[:-1]



print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
