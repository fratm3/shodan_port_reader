from dotenv import load_dotenv
from shodan import Shodan
#import json
import sys
import os

import requests

load_dotenv()
API_KEY = os.getenv("SHODAN_API_KEY")

api = Shodan(API_KEY)

if __name__ == "__main__" :

    try :
        host = sys.argv[1]
    except IndexError:
        print("Host not specified")
        

    query_result = api.host(host)
    print(query_result["ports"])


    #json_data = (requests.get(f"https://api.shodan.io/shodan/host/{host}?key={API_KEY}")).json()
    #print(json_data["ports"])

