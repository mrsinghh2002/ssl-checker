# the python script for finding the ssl certificate status
# you can enter a single url and also take url from a text file
# designed by Mrsingh2002 (https://github.com/mrsinghh2002)


import subprocess
import os
import time
from datetime import datetime
import sys
import re


websites = []

# ascii art
def ascii():
    print("""\

         | |      | |             | |
  ___ ___| |   ___| |__   ___  ___| | _____ _ __
 / __/ __| |  / __| '_ \ / _ \/ __| |/ / _ \ '__|
 \__ \__ \ | | (__| | | |  __/ (__|   <  __/ |
 |___/___/_|  \___|_| |_|\___|\___|_|\_\___|_|


ssl-checker 1.0.0
https://github.com/mrsinghh2002/ssl-checker

    """)



# help tag for usage
def help():
    ascii()
    print("usage: ssl-checker [option] [url]")
    print("\n option:")
    print("\t-s, --single-url\t: enter the url for your website")
    print("\t-m, --multiple-url\t: select the text file of your urls")
    print("\t-h, --help")
    print()
    print("\n url:")
    print("\t-s\t: enter the url in format: google.com")
    print("\t-m\t: enter the text file in format: abc.txt")
    print()

# ssl checker
def ssl_checker(website):

    # -v for verbose mode, -s to hide the progress bar that is displayed, -o to save the output to a particular file
    # and 2 in front of shell_output will merge the data from stream1 to stream2
    connect_website = f"curl https://{website} --connect-timeout 10 -v -s -o shell_output 2>ca.info"
    subprocess.check_output(connect_website, shell=True)

    # getting the start date
    start_date = "cat ca.info | grep 'start date: '"
    out_byte_first = subprocess.check_output(start_date, shell = True)
    out_text_first = out_byte_first.decode('utf-8')
    # if you only wanted to show the date and no time
    #expire_date_final = time.strftime("%Y-%m-%d")
    start_date_final = time.strftime("%Y-%m-%d %H:%M:%S", time.strptime(out_text_first[-25:-5], "%b %d %H:%M:%S %Y"))


    # getting the expire date
    expire_date = "cat ca.info | grep 'expire date: '"
    out_byte_second = subprocess.check_output(expire_date, shell = True)
    out_text_second = out_byte_second.decode('utf-8')
    expire_date_final = time.strftime("%Y-%m-%d %H:%M:%S", time.strptime(out_text_second[-25:-5], "%b %d %H:%M:%S %Y"))


    # getting the issuer name
    issuer_name = "cat ca.info | grep 'issuer: '"
    out_byte_third = subprocess.check_output(issuer_name, shell = True)
    out_text_third = out_byte_third.decode('utf-8')
    issuer_name_final = out_text_third.split("CN=")[1].strip()


    # calculate number of days left
    check_datetime = datetime.now()
    expire_datetime = datetime.strptime(out_text_second[-25:-5], "%b %d %H:%M:%S %Y")
    left_days = (expire_datetime - check_datetime).days


    # origin finder
    origin_country = "cat ca.info | grep 'subject: '"
    out_byte_fourth = subprocess.check_output(origin_country, shell = True)
    out_text_fourth = out_byte_fourth.decode('utf-8')
    origin_country_final = out_text_fourth.split("C")[1].split(';')[0].split("=")[1].strip()




    # printing the values

    print('\033[33m[*]\033[0m Website: {name}'.format(name = website))
    print("\033[32m[*]\033[0m Country Of Origin: \033[32m{countryName}". format(countryName = origin_country_final))
    print("\033[32m[*]\033[0m Start Date: \033[32m{startDate}". format(startDate = start_date_final))
    print("\033[32m[*]\033[0m Expiry Date: \033[32m{expiryDate}". format(expiryDate = expire_date_final))
    print("\033[32m[*]\033[0m Issuer Name: \033[32m{issuerName}". format(issuerName = issuer_name_final))
    print('\033[33m[*]\033[0m No of Days Left: \033[33m{daysLeft} days'.format(daysLeft = left_days))
    print('\n')





def fileRemoval():
    #  removing the file after every subprocess
    os.system('rm -f ca.info')
    os.system('rm -f shell_output')



def mainFunction():

    for website in websites:
        try:
            # removing any http: or https: in front of our url
            website = re.sub("https://","",website)
            website = re.sub("http://","",website)
            ssl_checker(website)


        except subprocess.CalledProcessError as e:
            print(e)
            print('\n')


        time.sleep(1)

    fileRemoval()


# handling different modes and options
if len(sys.argv) == 1:
    help()
    exit(1)
else:
    # single url
    if "-s" in sys.argv or "--single-url" in sys.argv:
        n = len(sys.argv)

        if n <= 3:
            url = sys.argv[n-1]
            websites.append(url)

            ascii()
            mainFunction()


        else:
            print("Use -m [mode] for adding more than one url")

    # multiple url
    elif "-m" in sys.argv or "--multiple-url" in sys.argv:
        n = len(sys.argv)
        if n <=3:
            url_file = open(sys.argv[n-1], "r")
            content = url_file.read().splitlines()
            # for removing the '' new line characters that are present in url file
            content = [x for x in content if x]

            for u in content:
                websites.append(u)

            ascii()
            mainFunction()



        else:
            print("Invalid Format, Use: -h for help")

    # help section
    elif "-h" in sys.argv or "--help" in sys.argv:
        help()

    else:
        help()
        exit(1)
