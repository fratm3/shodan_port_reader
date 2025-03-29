#!/usr/bin/env python

from dotenv import load_dotenv
from shodan import Shodan
import os
import argparse

#import requests

load_dotenv()
API_KEY = os.getenv("SHODAN_API_KEY")

api = Shodan(API_KEY)

parser = argparse.ArgumentParser()
parser.add_argument("--host", type=str, help="Specify a single IP address to inspect")
parser.add_argument("--file", type=str, help="Specify a .txt file with a list of IPs to inspect")

args = parser.parse_args()

if args.host : 

    host = args.host
    query_result = api.host(host)
    print(f"Host {host} has the following open ports: {query_result["ports"]}")

    #json_data = (requests.get(f"https://api.shodan.io/shodan/host/{host}?key={API_KEY}")).json()
    #print(json_data["ports"])


elif args.file : 
    
    with open(args.file, mode='r') as inputFile:

        hosts = inputFile.readlines()

        for host in hosts:

            query_result = api.host(host)
            print(f"Host {host.strip()} has the following open ports: {query_result["ports"]}")

            #json_data = (requests.get(f"https://api.shodan.io/shodan/host/{host}?key={API_KEY}")).json()
            #print(json_data["ports"])


else :

    print("Invalid syntax. Please specify either a --host or --file parameter")
