import urllib.request
import json

# WRITTEN AND COMMENTED BY HENRY FRIMAN 2021

# USING urllib.request LIBRARY TO OPEN AN URL ADDRESS
# ----> FUNCTION IS STORED INSIDE response VARIABLE
with urllib.request.urlopen('https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json') as response:

    # USING json LIBRARY TO PARSE THE CONTENT OF THE response VARIABLE,
    # WHICH IS BEING READ BY A METHOD FROM urllib.request LIBRARY
    # --> THE OUTCOME (CLEAN JSON DATA) IS STORED INSIDE cleanlist VARIABLE
    # --> THE cleanlist VARIABLE'S VALUES FROM THE KEY-VALUE JSON DATA
    #     IS STORED INSIDE postoffices VARIABLE
    cleanlist = json.loads(response.read())
    postoffices = cleanlist.values()


# THE USER IS ASKED TO WRITE A WORD,
# WHICH IS STORED INSIDE answer VARIABLE
answer = input('Kirjoita postitoimipaikka: ')

# IMMEDIATELY AFTER THE INPUT,
# THE answer VARIABLE'S VALUE
# IS REWRITTEN WITH UPPER-CASE LETTERS
# ---> NOW THE SYSTEM CAN NOT MISMATCH
#      THE USER'S INPUT WHEN COMPARING
#      IT TO THE clearlist's VALUES
answer = answer.upper()

# AFTER THE USER'S INPUT AND REWRITING,
# THE CONDITION CHECK STARTS:
#-----> IF THE answer VARIABLE'S VALUE IS NOT THE SAME
#       AS ANY VALUE IN THE postoffices LIST,
#       THE PROGRAM PRINTS A NOTIFICATION ABOUT THAT
if answer not in postoffices:
    print('Postitoimipaikkaa ei ole olemassa')

#-----> IF THE answer VARIABLE'S VALUE IS THE SAME
#       AS SOME VALUE IN THE postoffices LIST,
#       THE FOLLOWING HAPPENS:
#       1. THE valuelist IS CREATED
#       2. THE LOOP CHECKS EVERY KEY
#          FROM THE cleanlist LIST,
#          AND EACH TIME THE KEY HAS A VALUE
#          THAT IS THE SAME AS answer VARIABLE,
#          THE KEY IS STORED INSIDE THE valuelist 

else:
    valuelist = []
    for key in cleanlist:
        if cleanlist.get(key) == answer:
            valuelist.append(key)

    # WHEN THE LOOP IS OVER, ALL THE VARIABLES
    # FROM THE valuelist ARE PRINTED INTO THE SCREEN
    # ---> THE ANSWER IS WRITTEN IN THE SAME ROW
    #      BY USING join METHOD, WHICH CAN ADD
    #      THE WANTED SYMBOL (,) IN BETWEEN EACH
    #      VALUE IN THE valuelist LIST, WHILE ALSO
    #      IGNORING THE BRACKETS AND APOSTROPHES
    print('Postinumerot: ' + ', '.join(valuelist))
