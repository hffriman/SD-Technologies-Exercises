import urllib.request
import json

# WRITTEN AND COMMENTED BY HENRY FRIMAN 2021

# THIS LINE USES urrlib.request LIBRARY'S FUNCTION,
# WHICH OPENS THE URL ADDRESS WRITTEN AS THE FUNCTION'S PARAMETER
# -----> THE FUNCTIONALITY IS STORED INSIDE A VARIABLE NAMED response
with urllib.request.urlopen('https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json') as response:

    # FIRST THE CONTENT OF response VARIABLE IS READ BY urllib's READ FUNCTION,
    # THEN THE CONTENT IS PARSED BY json LIBRARY'S loads FUNCTION
    # ---> FINALLY THE RESULT IS STORED INSIDE A cleanlist VARIABLE
    cleanlist = json.loads(response.read())

# THIS LINE STORES THE USER INPUT INTO VARIABLE pos
pos = input('Kirjoita postinumero: ')

# AFTER THE INPUT IS DONE, THE pos VARIABLE GETS CHECKED:
# ----> IF pos VARIBLE'S CONTENT HAS NO KEY VALUE IN THE cleanlist JSON DATA,
#       THE PROGRAM PRINTS A TEXT WHICH MENTIONS THE INCORRECT INPUT
#-----> OTHERWISE THE pos VARIABLE'S CONTENT'S KEY VALUE IS PRINTED
if pos not in cleanlist:
    print('Postinumeroa ei ole olemassa')
else:
    print(cleanlist[pos])
