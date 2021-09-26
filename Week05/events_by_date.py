import urllib.request
import json
from datetime import datetime, timedelta

def fetch_events():
    with urllib.request.urlopen('https://open-api.myhelsinki.fi/v1/events/') as response:
    	data = response.read()

    events = json.loads(data)

    return events['data']


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
