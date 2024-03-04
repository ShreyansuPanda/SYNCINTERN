#SYNC Intern's Task 2:OTP Verification:- This is a project that sends an OTP Verification Email 
#Use the apppassword from Google Email


from email.message import EmailMessage
import ssl
import smtplib
import random

email_sender="eziomorningstar123@gmail.com"
password=r"E:\programming\Python\CodesonBytes\Task 1-Automated Email\PASSWORD.txt"
email_receiver=input("Enter Email:")

otp=random.randint(100000,999999)


subject="OTP Verification"
body=f"""
Hello,This is an email sent  for OTP verification.
One Time Password: {otp}
"""

with open(password, 'r') as password:
        email_password = password.read().strip()


em=EmailMessage()
em['From']=email_sender
em['To']=email_receiver
em['Subject']=subject
em.set_content(body)

context=ssl.create_default_context()

try:
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())
        print("Email sent successfully!")
        otp_recieved=int(input("Enter OTP:"))
        if (otp_recieved==otp):
            print("OTP Verified")
        else:
            print("OTP Verification failed!")
except Exception as e:
    print("Error",str(e))
