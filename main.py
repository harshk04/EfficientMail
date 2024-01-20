import pandas as pd
import smtplib as sm
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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

    # Replace '\n' with HTML line breaks
    html_body = html_body.replace('\\n', '<br>')

    server = sm.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email_user, email_password)

    from_ = email_user
    to_ = email_list

    message = MIMEMultipart("alternative")
    message['Subject'] = subject_user
    message['From'] = from_

    # Convert the user input HTML body to MIMEText
    html = MIMEText(html_body, "html")
    message.attach(html)

    server.sendmail(from_, to_, message.as_string())
    print("Mails have been sent successfully. ")

except Exception as e:
    print(e)

finally:
    server.quit()
