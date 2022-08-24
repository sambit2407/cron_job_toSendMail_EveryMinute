import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from config_reader import ConfigReader
    
    
    
    
def sendEmailToSupport(name, email, user_query):
    config_reader = ConfigReader()
    
    configuration = config_reader.read_config()

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = "sambitbehera2016@gmail.com"

    # storing the receivers email address
    msg['To'] = "sambitbehera2016@gmail.com"

    # storing the subject
    msg['Subject'] = "Customer query"

    body = """We have a customer query, which we were not able to answer as of now. Here is the query:- 
                {}\n
                Customer-name:- {}\n
                Customer-email:- {}\n
                Please have a look into this.
                \n\n\n\n
                Regards,
                Team iNeuron
            """.format(user_query,name,email)

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'html'))


    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # creates SMTP session
    smtp = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    smtp.starttls()

    # Authentication
    smtp.login(
        configuration['SENDER_EMAIL'], configuration['PASSWORD'])

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    smtp.sendmail(
        configuration['SENDER_EMAIL'], msg['To'], text)

    print("Email sent to support team!")

    # terminating the session
    smtp.quit()
    return "Email sent to support team!"