# PasteMonitor
Scrape Pastebin API to collect daily pastes, setup a wordlist and be alerted by email when you have a match.												 

## Description
The PasteMonitor tool allows you to perform two main actions (for educational purposes only):

- ### Download daily new public pastes
![image](https://user-images.githubusercontent.com/75697623/145390083-e1f8ca14-a0d1-4763-90a7-56634c87f20d.png)
Average number of pastes per day: 1000-3000 (filetype: .txt)

- ### Send automatic email alert
You can setup a wordlist and be alerted by email when you have a match
![image](https://user-images.githubusercontent.com/75697623/145399396-e685c7c2-252b-4266-8f07-8934fab935d5.png)

If your paste is no longer online, you can find it on your computer/server via the ID of your paste (here ID is "WJq2YxPg")
![image](https://user-images.githubusercontent.com/75697623/145396434-d3db83c0-4c43-4c6f-a8e1-9a57f063db25.png)


## Before start

Before starting the tool, make sure to:
- Get a [Pastebin PRO](https://pastebin.com/pro) account
- Enter the IP address of your machine in the "[Your Account & Whitelisted IP](https://pastebin.com/doc_scraping_api)" section
- Activate a mail account that can authorize a third party application (here we use a [Gmail account](https://www.google.com/intl/fr/gmail/about/))
- [Enable 2-step verification](https://myaccount.google.com/u/2/signinoptions/two-step-verification)
- [Generate app password](https://myaccount.google.com/u/2/apppasswords) (for more help, see this [tutorial](https://ljmocic.medium.com/send-an-email-using-python-and-gmail-4ebc980eae9b))

Then, add to the code "pastemonitor.py":
- Email credentials ("email", "password")
- Email alert recipient ("receiver")
- Working directory path ("pathDirectory" - Example: "/home/user/PASTEBIN/")

## Prerequisite

```bash
pip3 install -r requirements.txt
```

## Usage

```bash
python3 pastemonitor.py
```

 ## Pastebin.com usage
 Visit the official Pastebin webpage [Scraping API](https://pastebin.com/doc_scraping_api).

## Contributing
Feel free to clone this project. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
