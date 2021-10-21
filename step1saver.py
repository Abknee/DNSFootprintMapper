import sys
import requests

inputList = sys.argv[1]
with open(inputList, "r", encoding='utf-8-sig') as domainBucket:
    for line in domainBucket:
        targetDomain = line
        url1 = "https://subdomains.whoisxmlapi.com/api/v1?apiKey=$APIKEY&domainName={0}".format(
            targetDomain)
        response = requests.get(url1).json()
        for subs in response["result"]["records"]:
            with open('output.csv', 'a') as f:
                print((subs['domain']), file=f)