# Automated Job Application Email Sender

This project automates the process of sending personalized job application emails to HR contacts at various companies. It uses Google Gemini (via LangChain), structured prompts, and email automation to generate and send professional emails with resume attachments.

## Features

- Reads candidate and company details from Excel files
- Generates a professional, personalized email for each company using an LLM (Google Gemini)
- Attaches the candidate's resume PDF to each email
- Tracks which companies have already been contacted to avoid duplicates
- Configurable via environment variables

## Folder Structure

```
src/
  main.py                # Main script to run the email sending process
  user_details.py        # Candidate details
  get_company_details.py # Functions to read company info from Excel
  system_prompt.py       # Prompt template for the LLM
  output_structure.py    # Pydantic model for structured LLM output
  send_mail.py           # Email sending logic
  config.py              # Configuration flags
  track.py               # Progress tracking
  companies.xlsx         # Excel file with company details
  chintamani_pala_web-developer-resume.pdf # Resume PDF
  .env                     # Environment variables (not committed)
```

## Setup

1. **Clone the repository**

2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

3. **Configure environment variables**

   Copy `src/.env.example` to `src/.env` and fill in your credentials:
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   SENDER_EMAIL=your_sender_email_here
   SENDER_PASSWORD=your_sender_password_here
   SMTP_SERVER=your_smtp_server_here
   SMTP_PORT=your_smtp_port_here
   COMPANY_LIST_FILE_NAME=companies.xlsx
   MAX_MAILS_PER_DAY=50
   ```
   > **Note:** If you are using Gmail (`smtp.gmail.com`) as your SMTP server, set `SMTP_PORT=465`.

4. **Prepare your Excel file**

   Make sure `companies.xlsx` is present in the `src/` folder with columns like:
   ```
   SNo | HR Name | Email | Title | Company Name
   ```

5. **Add your resume PDF**

   Place your resume PDF in the `src/` folder and update the path in `user_details.py` if needed.

6.  **Edit your candidate details**

     Open `src/user_details.py` and update all fields (name, email, contact, skills, experiences, resume path, etc.) to match your own information.

## Usage

Run the main script:

```sh
cd ./src
python main.py
```

The script will:
- Generate a personalized email for each company
- Attach your resume
- Send the email via SMTP
- Wait 5 seconds between emails
- Track progress in `track.json`

## Customization

- **Prompt and email rules:** Edit `system_prompt.py`
- **Candidate details:** Edit `user_details.py`
- **Company list:** Edit `companies.xlsx`
- **Resume path:** Edit `user_details.py`
- **Max emails per day:** Set `MAX_MAILS_PER_DAY` in `.env`

## Notes

- Make sure your SMTP credentials are correct and allow sending emails via your provider.
- The project uses Google Gemini via LangChain for email generation.
- Progress is tracked in `src/track.json`.

---

**Disclaimer:** Use responsibly. Do not spam companies.
