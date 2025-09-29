def city_country(city, country):
    print("IF you want to exit input \' q \'")
    return ("\'"+ city + "," +country +"\'")




while True:
    name_city = input("Enter city name: ")
    name_country = input("Enter country name: ")
    if name_city == 'q' :
        break
    elif name_country == 'q' :
        break

    city = city_country(name_city, name_country)
    print(city)

