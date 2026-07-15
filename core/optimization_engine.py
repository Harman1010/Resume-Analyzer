from core.ats_engine import ATSEngine
from agents.optimization_agent import generate_optimization_report

from schemas.response_schema import AnalyzeResponse

from agents.rewrite_agent import get_rewritten_resume

class ResumeAnalyzer:

    def __init__(self):
        self.ats_engine = ATSEngine()

    def analyze(
        self,
        resume_text: str,
        job_description: str
    ) -> AnalyzeResponse:

        ats_result = self.ats_engine.analyze(
            resume_text,
            job_description
        )

        optimization = generate_optimization_report(
            resume_text,
            job_description,
            ats_result
        )

        return AnalyzeResponse(
            ats=ats_result,
            optimization=optimization
        )