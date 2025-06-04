# # type: ignore
import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env", override=True)


def send_mail_with_pdf(receiver_email, subject, body, pdf_path=None):
    sender_email = os.getenv("SENDER_EMAIL")
    sender_password = os.getenv("SENDER_PASSWORD")
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = int(os.getenv("SMTP_PORT", 465))  # default to 587 if not set

    if not sender_email or not sender_password or not smtp_server or not smtp_port:
        raise ValueError("Missing email or SMTP configuration in environment variables")

    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.set_content(body)

    if pdf_path:
        with open(pdf_path, "rb") as f:
            pdf_data = f.read()
        msg.add_attachment(
            pdf_data,
            maintype="application",
            subtype="pdf",
            filename=os.path.basename(pdf_path),
        )
    print("Sending email...")
    try:
        if smtp_port == 465:
            # SSL connection
            with smtplib.SMTP_SSL(smtp_server, smtp_port) as smtp:
                smtp.login(sender_email, sender_password)
                smtp.send_message(msg)
        else:
            # TLS connection (e.g., port 587)
            with smtplib.SMTP(smtp_server, smtp_port) as smtp:
                smtp.starttls()
                smtp.login(sender_email, sender_password)
                smtp.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print("Error sending email:", e)
    print("Email sending process completed.")
