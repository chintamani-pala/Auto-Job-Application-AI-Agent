# type: ignore
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from system_prompt import get_system_prompt
from output_structure import OutputStructure
from send_mail import send_mail_with_pdf
from track import (
    get_last_completed_index,
    update_tracker,
    get_last_completed_daily_index,
    update_daily_tracker,
)
from get_company_details import get_company_count
from get_company_details import get_file_name
import os
import time

load_dotenv(dotenv_path=".env", override=True)


def send_email_to_hr():
    print("Starting the email sending process...")

    company_index = get_last_completed_index() + 1

    chat_model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=1)
    prompt = get_system_prompt(company_index)
    model = chat_model.with_structured_output(OutputStructure)
    result = model.invoke(prompt)

    if not isinstance(result, OutputStructure):
        raise ValueError("The model did not return the expected structured output.")

    print("Email content Generated successfully.")
    send_mail_with_pdf(
        receiver_email=result.company_email,
        subject=result.subject,
        body=result.body,
        pdf_path=result.pdf_path,
    )
    print("Email sent successfully.")

    print("Updating tracker with the current company index...")
    update_tracker(company_index)
    print("Tracker updated successfully.")

    print(
        f"Email sent to {result.company_email} for company {result.company_name} for company index {company_index}."
    )


if __name__ == "__main__":
    try:
        max_mails_per_day = int(os.getenv("MAX_MAILS_PER_DAY", 10))
        company_count = int(get_company_count(file_path=get_file_name()))
        while (
            get_last_completed_daily_index() + 1 <= max_mails_per_day
            and get_last_completed_index() + 1 < company_count
        ):
            send_email_to_hr()
            update_daily_tracker(get_last_completed_daily_index() + 1)
            print("Waiting for 5 seconds before sending the next email...")
            time.sleep(5)
            print("Continuing to the next email...")
        else:
            print(
                "Reached the maximum number of emails for today or all companies processed."
            )
            update_daily_tracker(0)  # Reset daily tracker after processing
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print("Email sending process completed successfully.")
