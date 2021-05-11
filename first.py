import requests


client_id = ''

client_secret = ''

def main():
    url = f"""https://yoomoney.ru/oauth/authorize?client_id={client_id}&response_type=code&redirect_uri=http://100.74.24.55:8095&scope=account-info operation-history"""

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    try:
        r = requests.post(url, headers)
    except:
        pass

    print(r.url)

main()

