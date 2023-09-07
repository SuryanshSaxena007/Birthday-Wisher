import smtplib
import datetime as dt
import pandas
import random

now = dt.datetime.now()
day = now.day
month = now.month
num = random.randint(1, 3)


ni = pandas.read_csv("birthdays.csv")
n = ni.to_dict(orient='records')

for date in n:
    if day in date.values() and month in date.values():

        my_mail = "pavilioncode@gmail.com"
        password = "12345@new"
        name = date["name"]

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_mail, password=password)

            with open(f"letter_{num}.txt", "r") as letter:
                new_letter = letter.read()
                final = new_letter.replace("[NAME]", f"{name}")

            connection.sendmail(from_addr=my_mail,
                                to_addrs="saxena.suryansh@rediffmail.com",
                                msg=f"Subject:Happy Birthday\n\n{final}"
                                )




# if day == 4:
#     today = random.choice(q_list)
#
    # my_mail = "pavilioncode@gmail.com"
    # password = "12345@new"
    #
    # with smtplib.SMTP("smtp.gmail.com") as connection:
    #     connection.starttls()
    #     connection.login(user=my_mail, password=password)
    #     connection.sendmail(from_addr=my_mail,
    #                         to_addrs="saxena.suryansh@rediffmail.com",
    #                         msg=f"Subject:Quotes with Python\n\n{today}"
    #                         )
    #
    #

# with open("./Input/Names/invited_names.txt") as names:
#     name_list = names.readlines()
#
#     for i in name_list:
#         j = i.strip("\n")
#         with open("./Input/Letters/starting_letter.txt") as letter:
#             new_letter = letter.read()
#             name = new_letter.replace("[name]", f"{j}")
#             with open(f"./Output/ReadyToSend/letter_for_{j}.txt", mode="w") as file:
#                 file.write(name)




##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




