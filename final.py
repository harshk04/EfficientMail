import streamlit as st
import pandas as pd
import smtplib as sm
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

# Function to read email list from Excel file
def read_email_list(file):
    try:
        df = pd.read_excel(file)
        email_col = df.get("Email")
        return list(email_col)
    except Exception as e:
        st.error(f"Error reading the Excel file: {e}")
        return []

# Streamlit UI
st.set_page_config(
    page_title="EfficientMail",
    page_icon="✉️",
    layout="centered",
)

st.header("EfficientMail - Email Sender App")

# Pop-up button with instructions for the Excel sheet
with st.expander("ℹ️ How should the Excel sheet look like?"):
    st.write("Please make sure your Excel sheet contains a column named 'Email'")
    # st.image("path/to/instruction_image.jpg", use_container_width=True)  # Add the correct path to your image

# Option to upload Excel file
uploaded_file = st.file_uploader("Upload Excel file with email addresses", type=["xlsx", "xls"])

# Display warning text if no file is uploaded
if uploaded_file is not None:
    email_list = read_email_list(uploaded_file)
else:
    st.warning("Please upload an Excel file to proceed.")

# User input for email and password
password_hover_text = "How to generate app password from Gmail"
password_hover_link = "https://www.youtube.com/watch?v=T0Op3Qzz6Ms"
password_hover_message = f'<a href="{password_hover_link}" target="_blank">{password_hover_text}</a>'
password_tooltip = st.markdown(password_hover_message, unsafe_allow_html=True, key="password_tooltip", enable_st_writer=False)

email_user = st.text_input("Enter your email:")
email_password = st.text_input("Enter your email password (APP PASSWORD) to be generated from Gmail Account:", type="password")

# User input for CC recipients
add_cc = st.checkbox("Add CC recipients?")
if add_cc:
    cc_recipients = st.text_input("Enter CC email addresses (separated by commas):")
    cc_list = [email.strip() for email in cc_recipients.split(',')]
else:
    cc_list = []

# User input for subject and HTML body
subject_user = st.text_input("Enter the email subject:")
html_body = st.text_area("Enter the HTML body (use '\\n' for new paragraphs):")

# User input for attachment
add_attachment = st.checkbox("Add an attachment?")
if add_attachment:
    file_path = st.file_uploader("Upload attachment", type=["xlsx", "xls", "pdf", "docx", "png", "jpg", "jpeg"])
else:
    file_path = None

if st.button("Send Emails") and email_list:
    try:
        # Replace '\n' with HTML line breaks
        html_body = html_body.replace('\\n', '<br>')

        server = sm.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email_user, email_password)

        from_ = email_user

        message = MIMEMultipart("alternative")
        message['Subject'] = subject_user
        message['From'] = from_
        message['Cc'] = ", ".join(cc_list)

        # Convert the user input HTML body to MIMEText
        html = MIMEText(html_body, "html")
        message.attach(html)

        if add_attachment and file_path is not None:
            attachment = MIMEBase("application", "octet-stream")
            attachment.set_payload(file_path.read())
            encoders.encode_base64(attachment)
            attachment.add_header('Content-Disposition', f'attachment; filename="{file_path.name}"')
            message.attach(attachment)

        server.sendmail(from_, email_list, message.as_string())
        st.success("Mails have been sent successfully.")

    except Exception as e:
        st.error(f"An error occurred: {e}")

    finally:
        server.quit()

# Made with love by Harsh
st.markdown("---")
st.markdown("Made with ❤️ by [Harsh](https://www.linkedin.com/in/harsh-kumawat-069bb324b/)")
