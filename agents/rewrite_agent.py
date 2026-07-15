from config.prompts import RESUME_REWRITING_PROMPT

from core.llm import llm

from schemas.rewriter_schema import RewriteSchema
from schemas.optimization_schema import OptimizationSchema
from schemas.ats_schema import ATSResult


def get_rewritten_resume(
    resume_text: str,
    ats_result: ATSResult,
    optimization_report: OptimizationSchema
) -> RewriteSchema:

    prompt = f"""
{RESUME_REWRITING_PROMPT}

Resume:
{resume_text}

ATS Analysis

ATS Score:
{ats_result.ats_score}

Required Skill Coverage:
{ats_result.required_skill_coverage:.2f}%

Preferred Skill Coverage:
{ats_result.preferred_skill_coverage:.2f}%

Matched Required Skills:
{", ".join(ats_result.matched_required)}

Missing Required Skills:
{", ".join(ats_result.missing_required)}

Matched Preferred Skills:
{", ".join(ats_result.matched_preferred)}

Missing Preferred Skills:
{", ".join(ats_result.missing_preferred)}

Optimization Report

Skills to Highlight:
{", ".join(optimization_report.existing_skills_to_highlight)}

Recommendations:
{chr(10).join("- " + recommendation for recommendation in optimization_report.recommendations)}

Summary:
{optimization_report.summary}
"""

    structured_model = llm.with_structured_output(
        RewriteSchema
    )

    response = structured_model.invoke(prompt)

    return response