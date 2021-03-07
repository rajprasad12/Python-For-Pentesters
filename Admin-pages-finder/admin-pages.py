import requests

url=input('enter the domain name like example.com\n')


with open("D:\\Hacking Scripts\\login-list.txt", 'r') as file:
    print("[!] Hunting for the login or Admin pages\n")
    for line in file:
        word= line.strip()
        page= url + "/" + word
        try:
            response= requests.get('https://www.' + page)
            if response.status_code ==200:
                print("[!] Paste this Domain name  in your URL address bar =",  page)
        except:
            pass



        

