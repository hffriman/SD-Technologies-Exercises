import urllib.request
import json

# WRITTEN AND COMMENTED BY HENRY FRIMAN 2021

# THIS PROGRAM IS MODIFIED TO MAKE TESTING EASIER
# ----> THE MODIFICATED PARTS OF THIS PROGRAM ARE PARTLY
#       BASED ON THE EXAMPLE SOLUTION OF THE LAST WEEK'S
#       EXERCISE, WHICH WAS GIVEN TO US BY THE TEACHERS


# DEFINING A FUNCTION WHICH GETS THE DATA FROM URL
def get_postnumbers():
        # USING urllib.request LIBRARY TO OPEN AN URL ADDRESS
        # ----> FUNCTION IS STORED INSIDE response VARIABLE
        with urllib.request.urlopen('https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json') as response:

                # USING json LIBRARY TO PARSE THE CONTENT OF THE response VARIABLE,
                # WHICH IS BEING READ BY A METHOD FROM urllib.request LIBRARY
                # --> THE OUTCOME (CLEAN JSON DATA) IS STORED INSIDE cleanlist VARIABLE
                cleanlist = json.loads(response.read())

        return cleanlist


# DEFINING A FUNCTION WHICH TAKES A LIST AS A PARAMETER
# AND PUTS EACH ITEM'S KEY INTO A NEW ARRAY CALLED offices
# --> IF THE ITEM DOESN'T CONTAIN STRING, IT IS SKIPPED 
def sort_by_postoffices(list):
        offices = {}
        for number, name in list.items():
                if name not in offices:
                        offices[name] = []

                offices[name].append(number)
                
        return offices


# THIS FUNCTION IS MODIFIED FROM THE LAST WEEK'S EXERCISE
# IN ORDER TO BE TESTED WITHOUT PROBLEMS
# -----> RESULTS ARE NOT PRINTED, JUST RETURNED
# -----> THERE IS ALSO NO STRING FORMAT IN A LIST OBJECT
# -----> THE MODIFICATION OF THIS FUNCTION IS LOOSELY BASED ON
#        THE EXAMPLE SOLUTION GIVEN BY THE TEACHERS
def find_postnumbers():

	# UPPER FUNCTIONS ARE CALLED, AND THEIR VALUES
	# ARE STORED INSIDE TWO DIFFERENT VARIABLES
	postnumbers = get_postnumbers()
	postoffices = sort_by_postoffices(postnumbers)
	
	# THE USER IS ASKED TO WRITE A WORD,
	# WHICH IS STORED INSIDE answer VARIABLE
	# WITHOUT SPACES AND WITH UPPER-CASE LETTERS
	answer = input('Kirjoita postitoimipaikka: ').strip().upper()

	# AFTER THE USER'S INPUT AND REWRITING,
	# THE CONDITION CHECK STARTS:
	#-----> IF THE answer VARIABLE'S VALUE IS NOT THE SAME
	#       AS ANY VALUE IN THE postoffices LIST,
	#       THE PROGRAM PRINTS A NOTIFICATION ABOUT THAT
	if answer not in postoffices:
    		return('Postitoimipaikkaa ei ole olemassa')

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
                for key in postnumbers:
                        if postnumbers.get(key) == answer:
                                valuelist.append(key)
        # 	valuelist's CONTENT IS STORED AND THEN RETURNED
                valuelist.sort()
                return(valuelist)
