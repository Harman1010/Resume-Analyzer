from schemas.ats_schema import ATSResult

from schemas.optimization_schema import OptimizationSchema

from agents.rewrite_agent import get_rewritten_resume

class ResumeRewriter:

    def rewrite(
        self,
        resume_text: str,
        ats_result: ATSResult,
        optimization: OptimizationSchema
    ):

        rewrite = get_rewritten_resume(
            resume_text,
            ats_result,
            optimization
        )

        return rewrite