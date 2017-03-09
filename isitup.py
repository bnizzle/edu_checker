__author__ = 'Bnizzle'
from SendEmail import sendEmailWithFields, logDownStatus
import requests
import config

# Request the website to query the status code
url = "http://evedownunder.com"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
r = requests.get(url, headers=headers)

if r.status_code != 200:
    tolist = config.tolist
    subject = 'EDU.com is down.'
    text = 'Hey Guys,\nhttp://evedownunder.com is currently down for an unknown reason. ' \
           'Can you please look into it ASAP.\n Thanks.'
    sendEmailWithFields(tolist, subject, text)
    # Write this event to a log file
    logDownStatus(r.status_code)