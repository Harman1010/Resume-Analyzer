from langchain_core.prompts import ChatPromptTemplate


JD_EXTRACTION_PROMPT = """
You are an expert recruitment assistant.

Analyze the given Job Description and extract structured information.

Extract ONLY the following fields:

- Job Role
- Required Skills
- Preferred Skills
- Responsibilities
- Tools / Technologies
- Soft Skills
- Experience Requirement
- Education Requirement

Rules:
1. Do not invent information.
2. If a field is missing, return an empty string or an empty list.
3. Return information that matches the provided schema exactly.
"""


jd_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", JD_EXTRACTION_PROMPT),
        ("human", "{job_description}")
    ]
)


RESUME_EXTRACTION_PROMPT = """
You are an expert resume parser.

Extract ONLY the technical skills explicitly mentioned in the resume.

Technical skills include:
- Programming languages
- Frameworks
- Libraries
- Databases
- Cloud platforms
- Developer tools
- Software
- Technologies
- Platforms
- Technical methodologies

Rules:
1. Do NOT infer skills.
2. Do NOT add missing skills.
3. Normalize names.
4. Remove duplicates.
5. Ignore soft skills.
6. Ignore education.
7. Ignore job titles.
8. Ignore company names.

Return ONLY structured output.
"""

resume_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", RESUME_EXTRACTION_PROMPT),
        ("human", "{resume}")
    ]
)