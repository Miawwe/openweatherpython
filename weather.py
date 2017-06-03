import requests

for i in range(10):
    city = input("Type city/country: ")
    r = requests.get("http://api.openweathermap.org/data/2.5/weather?q={" + city + "}&APPID=eb1e743f272ce2de2ebb5a0bed188722")
    json_object = r.json()
    temp_c = float(json_object["main"]["temp"])-273.15
    pressure = float(json_object["main"]["pressure"])
    wind_speed = float(json_object["wind"]["speed"])
    wind_dir = int(float(json_object["wind"]["deg"]))

    if wind_dir >= 348 and wind_dir <= 11:
        cardinal = "N"
    elif wind_dir >= 11 and wind_dir <= 78:
        cardinal = "NE"
    elif wind_dir >= 78 and wind_dir <= 101:
        cardinal = "E"
    elif wind_dir >= 101 and wind_dir <= 168:
        cardinal = "SE"
    elif wind_dir >= 168 and wind_dir <= 191:
        cardinal = "S"
    elif wind_dir >= 191 and wind_dir <= 258:
        cardinal = "SW"
    elif wind_dir >= 258 and wind_dir <= 281:
        cardinal = "W"
    elif wind_dir >= 281 and wind_dir <= 348:
        cardinal = "NW"

    print("Its " + str("%.1f" % temp_c) + " celsius")
    print("The pressure is " + str(pressure) + " hectopascal")
    print("Wind\'s speed is " + str(wind_speed) + " m/s and his direction is " + cardinal)
