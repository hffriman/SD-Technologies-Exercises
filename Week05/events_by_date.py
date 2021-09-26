import urllib.request
import json
from datetime import datetime, timedelta

# WRITTEN AND COMMENTED BY HENRY FRIMAN 2021


# CREATING A FUNCTION THAT USES:
# ---> urllib LIBRARY TO READ
#      DATA FROM myhelsinki's API PAGE
# ---> json LIBRARY TO STORE THE API'S CONTENT
#      INSIDE THE VARIABLE events
def fetch_events():
    with urllib.request.urlopen('https://open-api.myhelsinki.fi/v1/events/') as response:
    	data = response.read()

    events = json.loads(data)

    return events['data']



# CREATING A MAIN FUNCTION THAT WORKS THE FOLLOWING WAY:

# --> 1. USES THE UPPER FUNCTION TO STORE
#        THE RESULTS OF fetch_events FUNCTION
#        INSIDE A VARIABLE events
#
# --> 2. DEFINES VARIABLES FOR THE CURRENT DATE (min),
#        AS WELL AS THE VARIABLE FOR A DATE 30 DAYS
#        AFTER THE CURRENT DATE (max),
#        --> BOTH OF THESE VALUES ARE ALSO CHANGED INTO
#            ISO FORMAT INSIDE VARIBLES start_srt and end_str
#
# --> 3. HANDLES EACH ELEMENT OF THE events LIST
#        ONE ELEMENT AT A TIME, WITH THESE CONDITIONS:
#        ---> IF THERE IS NO VALUE INSIDE THE CURRENT
#             ELEMENT'S VALUE starting_day, IT IS SKIPPED
#        ---> OTHERWISE, THE LOOP CONTINUES:
#             ----> IF THE CURRENT ELEMENT HAS A NAME IN FINNISH,
#                   THE FINNISH NAME WILL BE PRINTED
#             ----> IF THE NAME'S NOT IN FINNISH BUT IN ENGLISH,
#                   THE ENGLISH NAME WILL BE PRINTED
#             ----> FINALLY, IF THE NAME IS ONLY IN CHINESE,
#                   THE CHINESE NAME WILL BE PRINTED

#           !!!! THE DATE OF THE EVENT IS ALWAYS PRINTED AFTER THE NAME !!!!

def main():
    
    events = fetch_events()

    min = datetime.utcnow()
    max = min + timedelta(days=30)

    start_str = min.isoformat()
    end_str = max.isoformat()
    
    for event in events:
        if event['event_dates']['starting_day'] is None:
            continue
        else:
            if start_str < event['event_dates']['starting_day'] < end_str:
                if (event['name']['fi']):
                    print(event['name']['fi'] + ', ' + event['event_dates']['starting_day'])
                elif (event['name']['en']):
                    print(event['name']['en'] + ', ' + event['event_dates']['starting_day'])
                elif (event['name']['zh']):
                    print(event['name']['zh'] + ', ' + event['event_dates']['starting_day'])
                      
if __name__ == '__main__':
    main()
