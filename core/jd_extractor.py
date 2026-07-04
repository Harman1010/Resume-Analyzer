from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from config.settings import LLM_MODEL
from config.prompts import jd_prompt
from schemas.jd_schema import JDSchema

load_dotenv()

llm = ChatGoogleGenerativeAI(model=LLM_MODEL,temperature=0)

structured_llm = llm.with_structured_output(JDSchema)

jd_extraction_chain = jd_prompt | structured_llm

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