import pandas as pd
import smtplib as sm
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os


# CHANGE FILE NAME AND FILEPATH OF EXCEL SHEET
df = pd.read_excel("/content/email.xlsx")
email_col = df.get("Email")
email_list = list(email_col)

try:
    # User input for email and password
    email_user = input("Enter your email: ")
    email_password = input("Enter your email password: ")

    # User input for subject and HTML body
    subject_user = input("Enter the email subject: ")

    # Explicitly mention the use of '\n' for new paragraphs in the prompt
    print("Enter the HTML body (use '\\n' for new paragraphs): ")
    html_body = input()


    html_body = html_body.replace('\\n', '<br>')

    server = sm.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email_user, email_password)

    from_ = email_user
    to_ = ", ".join(email_list) 

    message = MIMEMultipart("alternative")
    message['Subject'] = subject_user
    message['From'] = from_


    add_cc = int(input("Do you want to add CC recipients? (1 for Yes, 0 for No): "))

    if add_cc == 1:
        cc_recipients = input("Enter CC email addresses (separated by commas): ")
        cc_list = [email.strip() for email in cc_recipients.split(',')]
        cc_ = ", ".join(cc_list)
        message['Cc'] = cc_


    add_attachment = int(input("Do you want to add an attachment? (1 for Yes, 0 for No): "))
    if add_attachment == 1:
      # CHANGE FILE NAME AND FILEPATH FOR ATTACHMENT
        fileName = "email.xlsx"
        filePath = "/content/email.xlsx"
        fileSize = os.path.getsize(filePath) / 10 ** 6

        if fileSize > float(20):
            print(fileName, "Can't Be Uploaded As The Size Is much large.")
        else:
            attachment = MIMEBase("application", "octet-stream")
            attachment.set_payload(open(filePath, "rb").read())
            encoders.encode_base64(attachment)
            attachment.add_header('Content-Disposition', f'attachment; filename="{fileName}"')
            message.attach(attachment)

    
    # Convert the user input HTML body to MIMEText
    html = MIMEText(html_body, "html")
    message.attach(html)

    server.sendmail(from_, to_, message.as_string())
    print("Mails have been sent successfully.")

except Exception as e:
    print(e)

finally:
    server.quit()
