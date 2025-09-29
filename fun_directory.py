def sandwich(*topping):
    print(topping)


def build_profile(fname , lname , **aditional_info):
    profile = {}
    profile["first_name"] = fname
    profile["last_name"] = lname
    for key , value in aditional_info.items():
        profile[key] = value

    print(profile)
