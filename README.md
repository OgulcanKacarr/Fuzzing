# Fuzzing
find hidden folders and files



```

usage: fuzzing.py [-h] -u URL -w WORDLIST [-c COOKIE] [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     Target url http://test.com
  -w WORDLIST, --wordlist WORDLIST
                        Directories or files wordlist default: /usr/share/dirb/wordlists/common.txt
  -c COOKIE, --cookie COOKIE
                        Ör: 'Cookie': 'PHPSESSID=d143rj8718t2fl67a4jv4tb2s7; security=low'
  -o OUTPUT, --output OUTPUT
                        Save to file

```
<br>

```
python3 fuzzing.py -u http://192.168.1.34 -w /usr/share/dirb/wordlists/common.txt -o links

```
