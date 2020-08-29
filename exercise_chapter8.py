def describe_city(city, country="USA"):
    print(f"{city.title()} is in the {country.title()}!")

describe_city("minsk", "belarus")
describe_city("brooklyn")
describe_city(country="UK", city="london")