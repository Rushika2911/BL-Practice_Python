
cities = {
    "mumbai": (19.0760, 72.8777),
    "bangalore": (12.9716, 77.5946),
    "chennai": (13.0827, 80.2707),
    "pune": (18.5204, 73.8567),
    "hyderabad": (17.3850, 78.4867)
}



def check_city(city_name):
    city_name = city_name.lower()

    if city_name in cities:
        latitude, longitude = cities[city_name]
        return f"{city_name.title()}: Latitude = {latitude}, Longitude = {longitude}"
    else:
        return "City not found in the dictionary."


while True:
    city = input("Enter a city name (or type 'exit' to quit): ")

    if city.lower() == "exit":
        print("Exiting the program.")
        break

    print(check_city(city))