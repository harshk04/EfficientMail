# EfficientMail
EfficientMail is now seamlessly integrated with Streamlit, offering a user-friendly interface to automate the process of sending personalized emails via Gmail. The streamlined interaction involves importing email addresses from an Excel file, securely inputting email credentials, specifying the subject line, and customizing the HTML body. Experience the convenience of sending tailored emails effortlessly with EfficientMail through the intuitive and interactive Streamlit deployment.

## Screenshots
<img width="889" alt="Screenshot 2024-01-27 at 8 18 22 PM" src="https://github.com/harshk04/EfficientMail/assets/115946158/743f5657-e1cc-482e-b583-45536098cf58">


### Getting Started
Follow these steps to use the script:

#### 1. Clone the Repository:
Clone this repository to your local machine using the following command:

`git clone https://github.com/harshk04/EfficientMail.git`

#### 2. Install Dependencies:
Ensure you have the required Python packages installed. You can install them using the following command:

`pip install pandas`

`pip install secure-smtplib`

#### 3. Update Excel File Path:
Open the script file *(main.py)* and locate the line where the Excel file path is specified. Update the path to point to your Excel file containing the list of email addresses.

`df = pd.read_excel("/path/to/your/email.xlsx")`

#### 4. Run the Script:
Execute the script by running the following command in your terminal:

`python main.py`


### User Input Prompts
During script execution, you will be prompted to provide the following information:

**Email:** Your Gmail email address.

**Email Password:** Your Gmail account **APP PASSWORD** *(You have to set up it in your google account)*.

**Subject:** The subject line for the email.

**HTML Body:** The HTML body of the email. Use \n to indicate new paragraphs.

**Attachment:** You will be asked if you want to add an attachment (1 for Yes, 0 for No).

**CC Recipients:** If you choose to add CC recipients, you will be prompted to enter CC email addresses (separated by commas).




### Important Note
Make sure to handle your email credentials with caution and do not share them with others. Additionally, it's recommended to use an App Password for Gmail if you encounter any authentication issues.




### Disclaimer
This script is provided as-is and may require modifications based on your specific use case. Use it responsibly and ensure compliance with Gmail's policies on automated email sending.

If you encounter any issues or have suggestions for improvements, feel free to open an issue on the GitHub repository.

#### Happy Emailing!


<h2>📬 Contact</h2>

If you want to contact me, you can reach me through below handles.

&nbsp;&nbsp;<a href="https://www.linkedin.com/in/harsh-kumawat-069bb324b/"><img src="https://www.felberpr.com/wp-content/uploads/linkedin-logo.png" width="30"></img></a>

© 2024 Harsh
