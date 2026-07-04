from langchain_core.prompts import ChatPromptTemplate

JD_EXTRACTION_PROMPT = """
You are an expert recruitment assistant.

Analyze the job description and extract the information according to the provided schema.

Rules:
- Extract only explicitly mentioned information.
- Required Skills and Preferred Skills must contain only technical skills, technologies, programming languages, frameworks, libraries, databases, cloud platforms, developer tools, APIs, software, and technical methodologies.
- Return each technical skill using its commonly accepted canonical technical name. If a common abbreviation is used (e.g., ML, NLP, LLMs, RAG, OOP, CI/CD), return the full technical name.
- Do not infer missing skills.
- Remove duplicate entries.
- If a field is missing, return an empty string or empty list according to the schema.

Return only structured output.
"""


jd_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", JD_EXTRACTION_PROMPT),
        ("human", "{job_description}")
    ]
)

RESUME_EXTRACTION_PROMPT = """
You are an expert resume parser.

Extract every technical skill explicitly mentioned in the resume according to the provided schema.

Extract skills from all sections including Skills, Projects, Experience, Certifications, Achievements, and Summary.

Technical skills include programming languages, frameworks, libraries, databases, cloud platforms, developer tools, software, APIs, technologies, technical concepts, and methodologies.

Rules:
- Extract only explicitly mentioned technical skills.
- Return each technical skill using its commonly accepted canonical technical name. If a common abbreviation is used (e.g., ML, NLP, LLMs, RAG, OOP, CI/CD), return the full technical name.
- Do not infer missing skills.
- Remove duplicate entries.
- Ignore soft skills, job titles, company names, and educational qualifications.

Return only structured output.
"""


resume_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", RESUME_EXTRACTION_PROMPT),
        ("human", "{resume}")
    ]
)