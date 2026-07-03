from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from config.settings import LLM_MODEL
from config.prompts import JD_EXTRACTION_PROMPT
from schemas.jd_schema import JDSchema


# Load environment variables
load_dotenv()


# Initialize Gemini
llm = ChatGoogleGenerativeAI(
    model=LLM_MODEL,
    temperature=0
)


# Enforce structured output
structured_llm = llm.with_structured_output(JDSchema)


# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", JD_EXTRACTION_PROMPT),
        ("human", "{job_description}")
    ]
)


# Create LangChain pipeline
jd_extraction_chain = prompt | structured_llm


def extract_jd_information(job_description: str) -> JDSchema:
    """
    Extract structured information from a Job Description.

    Args:
        job_description (str): Raw Job Description text.

    Returns:
        JDSchema: Structured representation of the Job Description.
    """

    return jd_extraction_chain.invoke(
        {
            "job_description": job_description
        }
    )