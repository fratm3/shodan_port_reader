The script accepts either a --host parameter (which should be a single IP address) or a --file parameter (which should be the path to a txt file containing a list of IPs) and returns the list of open ports each IP has by using the Shodan API.
A `.env` file should be included containing the shodan API key with the following format: 

```
SHODAN_API_KEY=""
```
