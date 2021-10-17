# SSL Certificate Check Tool

Check SSL Certificate Status like, Start Date, Expiry Date, Issuer Name, Country of Origin 


![Python 3.7](https://img.shields.io/badge/python-v3.7-blue) ![Python 3.8](https://img.shields.io/badge/python-v3.8-blue) ![Python 3.9](https://img.shields.io/badge/python-v3.9-blue)
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://paypal.me/meshivanshsingh)


## Usage

### One Way
Use -s or --single-url for passing single url to the script

Run script : ` python3 ssl-checker.py -s facebook.com`
#### Output
```
$ python3 ssl-checker.py -s facebook.com

         | |      | |             | |
  ___ ___| |   ___| |__   ___  ___| | _____ _ __
 / __/ __| |  / __| '_ \ / _ \/ __| |/ / _ \ '__|
 \__ \__ \ | | (__| | | |  __/ (__|   <  __/ |
 |___/___/_|  \___|_| |_|\___|\___|_|\_\___|_|


ssl-checker 1.0.0
https://github.com/mrsinghh2002/ssl-checker

    
[*] Website: facebook.com
[*] Country Of Origin: US
[*] Start Date: 2021-09-09 00:00:00
[*] Expiry Date: 2021-12-08 23:59:59
[*] Issuer Name: DigiCert SHA2 High Assurance Server CA
[*] No of Days Left: 52 days

```
 


### The Other Way (recommend)
Uae -m or --multiple-url for taking the url from a text file, let's say a.txt for example

## Output 


```
python3 ssl-checker.py -m a.txt

         | |      | |             | |
  ___ ___| |   ___| |__   ___  ___| | _____ _ __
 / __/ __| |  / __| '_ \ / _ \/ __| |/ / _ \ '__|
 \__ \__ \ | | (__| | | |  __/ (__|   <  __/ |
 |___/___/_|  \___|_| |_|\___|\___|_|\_\___|_|


ssl-checker 1.0.0
https://github.com/mrsinghh2002/ssl-checker

    
[*] Website: facebook.com
[*] Country Of Origin: US
[*] Start Date: 2021-09-09 00:00:00
[*] Expiry Date: 2021-12-08 23:59:59
[*] Issuer Name: DigiCert SHA2 High Assurance Server CA
[*] No of Days Left: 52 days


[*] Website: www.kaspersky.com
[*] Country Of Origin: RU
[*] Start Date: 2021-02-26 00:00:00
[*] Expiry Date: 2022-03-02 23:59:59
[*] Issuer Name: DigiCert TLS RSA SHA256 2020 CA1
[*] No of Days Left: 136 days

```



## Advance Features Like:
1. Checking the SSL for a particular website (Using -s mode for single website)
2. Checking the SSL from a particular text file (Using -m mode for multiple website)
3. Removing http:// and https:// from url 

## Thanks
This project is highly inspired by : [https://flyhigher.top/develop/755.html](https://flyhigher.top/develop/755.html)

## Similar Projects
* [starnightcyber/SSLCheck](https://github.com/starnightcyber/SSLCheck)

## Author
ssl-checker @[MrSinghh2002](https://github.com/mrsinghh2002) , Released under the MIT License.

---


## Donation
If this project help you reduce time to develop, you can give me a cup of coffee :) 

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://paypal.me/meshivanshsingh)

 
