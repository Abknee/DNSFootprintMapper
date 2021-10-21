import sys
import requests

inputList = sys.argv[1]
with open(inputList, "r", encoding='utf-8-sig') as domainBucket:
    for line in domainBucket:
        targetDomain = line
        url1 = "https://subdomains.whoisxmlapi.com/api/v1?apiKey=$APIKEY&domainName={}".format(
            targetDomain)
        url2 = "https://api.threatintelligenceplatform.com/v1/sslConfiguration?apiKey=$APIKEY&domainName={}".format(
            targetDomain)
        responseUrl1 = requests.get(url1).json()
        responseUrl2 = requests.get(url2).json()
        data2 = responseUrl2['testResults']
        data1 = responseUrl1['result']['records']
        for x in data1:
            with open('output.csv', 'a') as f:
                if data2["sslCertificateConfigured"] == True and data2["validFrom"]["status"] != "OK":
                    print("the domain " + x['domain'] + " SSL check has: " + data2["validFrom"]["status"], file=f)
                else:
                    print('SSL is good for ' + x['domain'], file=f)
