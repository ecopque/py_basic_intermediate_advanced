import requests #1:
url = 'http://127.0.0.1:3333/' #2: #4:
# [terminal]$: python3 -m http.server -d Pasta_Site/ 3333 #11:
# [browser]: http://127.0.0.1:3333/ #3:
response = requests.get(url) #5:
print(response) #6: #12:
print(response.status_code) #7: #13:
print(response.headers) #8: #14:
# print(response.content) #9:
print(response.text) #10:
