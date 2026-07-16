from schemas.ats_schema import ATSResult

from schemas.optimization_schema import OptimizationSchema

from agents.rewrite_agent import get_rewritten_resume

from utils.resume_generator import get_resume

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

        file_path = get_resume(rewrite)

        return file_path