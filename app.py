import requests

url = "https://search5-noneu.truecaller.com/v2/search?q=%2B919241112963&countryCode=IN&type=4&encoding=json"
headers = {
  "Accept": "application/x-protobuf",
  "Authorization": "Bearer a2i0k--zM_DYFVpkIVfh-PnQUuXr-YA1ispvuRElZ47BGoAaNBfroGL5d82brLuE",
  "User-Agent": "Truecaller/16.10.5 (Android;16)",
  "Host": "search5-noneu.truecaller.com",
  "Connection": "Keep-Alive",
  "Accept-Encoding": "gzip"
}

res = requests.get(url, headers=headers)
print(res.text)
