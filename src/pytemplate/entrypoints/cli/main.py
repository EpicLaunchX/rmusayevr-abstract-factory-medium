def get_city_input() -> dict:
    name = input("Enter city name: ")
    country = input("Enter country: ")
    population = int(input("Enter population: "))
    return {"name": name, "country": country, "population": population}
