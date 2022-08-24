## Schedule your time



```sh
schedule.every(10).seconds.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every(5).to(10).minutes.do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().day.at("12:42", "Europe/Amsterdam").do(job)
schedule.every().minute.at(":17").do(job)
```

## To send Mail 

 The **smtplib** is a Python library for sending emails using the Simple Mail Transfer Protocol (SMTP). The smtplib is a built-in module; we do not need to install it.
 
 
 **MIMEMultipart** is used when we have attachments or want to provide alternative versions of the same content (e.g. a plain text/HTML version). We have a simple text     file. The example sends an email with a text file attachment to Mailtrap. We read the contents of the text file.
