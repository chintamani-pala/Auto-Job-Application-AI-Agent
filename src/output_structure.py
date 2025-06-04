from pydantic import BaseModel, Field
from typing import List, Optional


class OutputStructure(BaseModel):
    """
    Represents the structured output for a job application email.
    """

    subject: str = Field(..., description="Email subject line")
    body: str = Field(..., description="Email body/content to send to the HR")

    candidate_name: str = Field(..., description="Full name of the candidate")
    candidate_email: str = Field(..., description="Email address of the candidate")
    contact: str = Field(..., description="Contact number of the candidate")
    role: str = Field(..., description="Role applied for by the candidate")

    skills: List[str] = Field(..., description="List of skills the candidate has")
    experiences: List[str] = Field(..., description="List of professional experiences")
    other: Optional[str] = Field(None, description="Any additional information")

    company_name: str = Field(..., description="Name of the target company")
    hr_name: Optional[str] = Field(..., description="HR's name at the company")
    company_email: str = Field(..., description="HR or company email address")
    pdf_path: Optional[str] = Field(
        None, description="Path to the candidate's resume PDF file"
    )
