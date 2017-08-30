import requests
site=''
while not site:
  print("Please Enter the Domain Ip for reverse lookup")
  site=input()
  break
x = requests.get("http://api.hackertarget.com/reverseiplookup/?q="+site)
print(x.text)

