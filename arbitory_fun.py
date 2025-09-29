def details(ft_name , lt_name, **info ):
    profile = {}
    profile["fname"] = ft_name
    profile["lname"] = lt_name
    for key , value in info.items():
        profile[key] = value

    print(profile)





first_name = "Nusrat"
last_name = "Ali"

details(first_name, last_name, age = 18, profession = "student")
