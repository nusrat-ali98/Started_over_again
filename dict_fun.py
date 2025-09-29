def album(artist, album , track = ""):
    album_dict = {"Artist" : artist, "Album" : album, "Track" : track}
    return album_dict


var_album = (album("yoyo" , "honey"))
print(var_album)
