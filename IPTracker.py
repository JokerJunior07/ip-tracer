import requests
import json

banner = """
IP Tracer Coded by Joker Jr ~ @JokerJunior07
"""

print(banner)

while True:

    target = input("\nTarget Address => ")

    # çıkış komutu
    if target.lower() == "exit":
        print("Program Closed.")
        break

    r = requests.get("http://ip-api.com/json/" + target)

    j = json.loads(r.text)

    if j['status'] == 'success':
        print("\n[!] Informations Found")
        print("Country : " + j["country"])
        print("Country Code : " + j["countryCode"])
        print("Region : " + j["region"])
        print("Region Name : " + j["regionName"])
        print("City : " + j["city"])
        print("ISP : " + j["isp"])
        print("Query : " + j["query"])

    else:
        print("[!] Error Created")
