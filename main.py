##################### Extra Hard Starting Project ######################
import datetime
import os
import random
import smtplib
import pandas as pd

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
# 1. Update the birthdays.csv
def add_birthday(name, email, birthday):
    data = pd.read_csv('birthdays.csv')
    birthday_list = birthday.split("/")
    day = birthday_list[0]
    month = birthday_list[1]
    year = birthday_list[2]
    row = pd.DataFrame([[name, email, year, month, day]], columns = data.columns)
    row.to_csv('birthdays.csv', mode='a', header=False, index=False)

def get_list_of_templates():
    templates = []
    for file in os.listdir("letter_templates"):
        templates.append(file)
    return templates
#add_birthday("Dad", "bogdansinik@gmail.com", birthday="14/8/1959")

data = pd.read_csv('birthdays.csv')

# 2. Check if today matches a birthday in the birthdays.csv
today = datetime.date.today()
list_of_templates = get_list_of_templates()
for index, row in data.iterrows():
    birthday = datetime.date(int(row.year), int(row.month), int(row.day))
    if today.month == birthday.month and today.day == birthday.day:
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        random_template = random.choice(list_of_templates)
        with open(f"letter_templates/{random_template}", "r") as f:
            text = f.read()
            text = text.replace("[NAME]", row["name"])
# 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=row["email"], msg=f"Subject: Happy Birthday!\n\n{text}")

print("Birthday greetings have been sent!")

