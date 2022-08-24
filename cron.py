import schedule
import time
from send_email import sendEmailToSupport



def send_mail_interval(name,email,query):
    msg=sendEmailToSupport(name,email,query)

    print(msg)

# schedule.every(20).seconds.do(send_mail_interval,'Rahul','sambitbehera2016@gmail.com','this is cron job testing msg')
schedule.every(1).minute.do(send_mail_interval,'Rahul','sambitbehera2016@gmail.com','this is cron job testing msg')

while True:
    schedule.run_pending()
    time.sleep(2)