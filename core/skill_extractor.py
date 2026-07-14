from langchain_google_genai import ChatGoogleGenerativeAI

from config.settings import LLM_MODEL

from config.prompts import resume_prompt

from schemas.resume_schema import ResumeSchema


llm = ChatGoogleGenerativeAI(
    model=LLM_MODEL,
    temperature=0
)

structured_llm = llm.with_structured_output(
    ResumeSchema
)

chain = resume_prompt | structured_llm


def extract_resume_skills(
    resume_text: str
) -> list[str]:
    """
    Extract technical skills from the resume using Gemini.
    
    """

    response = chain.invoke(
        {
            "resume": resume_text
        }
    )

    return response.technical_skills