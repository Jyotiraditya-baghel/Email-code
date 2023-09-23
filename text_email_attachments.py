import smtplib 
import os
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart 
from email.mime.base import MIMEBase 
from email import encoders
# Setup port number and servr name
smtp_port = 587
smtp_server = "smtp.gmail.com"


#put the mail id in the quotes 
email_from = "Your gmail"

#can send to one or multiple persons
email_lists = ["sender email1, sender email2"]

#put the password here from google each user diffrent password
pswd = "password"

subject = "subject for the mail"

def send_emails(email_lists):
    filename = 'file path'  # Adjust the filename if needed
    file_path = os.path.join(os.path.dirname(__file__), filename)
    
    try:
        with open(file_path, 'rb') as attachment:
            # Rest of your email sending code
            pass
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

def send_emails(email_lists):

  for person in email_lists:

#write body within the quotes    
    body = f"""
    this is a sample book
    
    
    """

    # make a MIME object to define parts of the email
    msg = MIMEMultipart()
    msg['From'] = email_from
    msg['To'] = person
    msg['Subject'] = subject

    #Attach the body of the message
    msg.attach(MIMEText(body,'plain'))

    #Define file to attach
    filename = "Name of the file"

    #open the file
    attachment= open(filename, 'rb')

    # Encode as base 64
    attachment_package = MIMEBase('application', 'octet-stream')
    attachment_package.set_payload( (attachment).read())
    encoders.encode_base64 (attachment_package)
    attachment_package.add_header ('Content-Disposition', "attachment; filename= " + filename)
    msg.attach(attachment_package)

    #cast as string
    text = msg.as_string()

    # Connect with the server
    print ("Connecting to server...")
    TIE_server = smtplib.SMTP(smtp_server, smtp_port)
    TIE_server.starttls()
    TIE_server.login (email_from, pswd) 
    print ("Succesfully connected to server") 
    print()

    # Send emails to "person" as list is iterated
    print (f"Sending email to: {person}...")
    TIE_server.sendmail(email_from, person, text) 
    print (f"Email sent to: {person}")
    print ()
 
  TIE_server.quit()

send_emails(email_lists)
