import requests
#requests.get('https://detik.com')
com = 'https://detik.com'
try:
    response = requests.get(com)
    if response.status_code == 200:
        print(f'Success! Response = {response.status_code}')
        print(f'Content{response.text}')
    else:
        print(f'Upss, ada kesalahan request {response.status_code}')
    #print(f'success,{response}')
    #print(f'Content {response.text}')
except Exception as a:
    print(f'There is an error {a}')
print(f'program ended')