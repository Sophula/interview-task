from datetime import datetime
import requests
import csv

URL = 'http://google.com/'

response = requests.get(URL)

rows = [('Service Name', 'Status', 'Timestamp',
         'Content', 'Error')]


def generate_html(data):
    with open(f"report.html", "w") as file:
        file.write(data.text)
        print(f"{datetime.now()} html has been generated, {file.name}")
        return file.name


def generate_csv(data):
    with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(rows)


def check_status(url):
    try:
        response = requests.get(url)
        if(response.status_code == 200):
            generate_html(response)
    except requests.exceptions.RequestException as e:
        generate_csv(response)
        raise(e)


check_status(URL)
