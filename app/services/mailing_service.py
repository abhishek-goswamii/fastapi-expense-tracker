import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from models.expense import ExpenseCreateRequest
from typing import List

def send_email_to_participants(expense_data: ExpenseCreateRequest, sender_email: str):
    try:
        smtp_server = ""
        smtp_port = 587  
        smtp_username = ""
        smtp_password = ""

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['Subject'] = "Expense Notification"
        
        message = f"You owe {expense_data.paid_by} amounts:\n"
        
        for participant in expense_data.participants:
            if participant['user_id'] != expense_data.paid_by:
                message += f"- {participant['user_id']}: {participant['share']} \n"
        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        text = msg.as_string()
        server.sendmail(sender_email, [participant['email'] for participant in expense_data.participants], text)
        server.quit()

    except Exception as e:
        print(f"Failed to send email: {str(e)}")