# type: ignore
from user_details import get_user_details
from get_company_details import get_details_as_json_by_index
from get_company_details import get_file_name
from config import need_to_include_HR_name


def generate_prompt(user, company):
    experience_text = "\n".join(f"- {exp}" for exp in user["experiences"])
    skills = ", ".join(user["skills"])

    return f"""
You are a professional language assistant helping a job applicant draft a formal job application email.

Using the candidate and company details below, write a concise, polished, and professional email addressed to the HR. The email should be suitable for sending directly to the HR via email.

---

📌 **Candidate Details**  
- **Full Name:** {user["name"]}  
- **Email:** {user["email"]}  
- **Contact Number:** {user["contact"]}  
- **Role Applied For:** {user["role"]}  
- **Skills:** {skills}  
- **Professional Experiences:**  
{experience_text}  
- **Additional Info:** {user["other"]}  
- **Resume Attachment:** {user["pdf_path"]}

📌 **Company Details**  
- **HR Name:** {company.get("HR Name", "HR") if need_to_include_HR_name else "HR"}  
- **Company Email:** {company["Email"]}    
- **Company Name:** {company["Company Name"]}  

---

✍️ **Write an Email with the Following Rules:**

1. Start with a polite greeting using the HR's name (e.g., "Dear Mr. Sharma" or "Dear Ms. Priya").
2. Clearly state the purpose of the email — applying for the mentioned role.
3. Highlight the applicant's key skills and relevant experience.
4. Keep the tone professional, respectful, and enthusiastic.
5. Do not use overly casual or robotic phrases.
6. Avoid any filler text or generic statements that are not backed by the candidate's details.
7. Keep the email body concise (around 150-200 words).
8. End with a polite closing such as “Looking forward to hearing from you” and a proper sign-off.
9. Never include like as advertised on [Platform where you saw the advertisement - optional]
10. Dont add extra things so that the mail always looks like genuine
11. Ensure the email is ready to be sent without any further modifications.
12. Add a line that the candidate is attaching their resume for further details.
13. Also include candidate's contact number and candidate email in the email body at last of the mail.
Example 1:
Warm regards,  
Chintamani Pala  
chintamanipala67@gmail.com  
+91-9876543210
14. Include a subject line that is clear and relevant to the application and also include the candidate name in the subject.

✅ The output should be a ready-to-send email without any instructions or explanations.

Generate the email now.
"""


def get_system_prompt(companyIndex=0):
    """Generate the system prompt for the job application email."""
    return generate_prompt(
        get_user_details(),
        get_details_as_json_by_index(companyIndex, get_file_name()),
    )
