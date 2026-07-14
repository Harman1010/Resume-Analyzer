from config.settings import LLM_MODEL
from config.prompts import RESUME_OPTIMIZATION_PROMPT

from schemas.ats_schema import ATSResult
from schemas.optimization_schema import OptimizationSchema

from core.llm import llm

def generate_optimization_report(resume_text: str,job_description: str,ats_result: ATSResult) -> OptimizationSchema:

    prompt = f"""
{RESUME_OPTIMIZATION_PROMPT}

Resume:
{resume_text}

Job Description:
{job_description}

ATS Analysis

ATS Score:
{ats_result.ats_score}

Required Coverage:
{ats_result.required_skill_coverage:.2f}%

Preferred Coverage:
{ats_result.preferred_skill_coverage:.2f}%

Matched Required Skills:
{", ".join(ats_result.matched_required)}

Missing Required Skills:
{", ".join(ats_result.missing_required)}

Matched Preferred Skills:
{", ".join(ats_result.matched_preferred)}

Missing Preferred Skills:
{", ".join(ats_result.missing_preferred)}
"""

    structured_model = llm.with_structured_output(
        OptimizationSchema
    )

    response = structured_model.invoke(prompt)

    return response