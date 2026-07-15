from pydantic import BaseModel

from schemas.ats_schema import ATSResult
from schemas.optimization_schema import OptimizationSchema
from schemas.rewriter_schema import RewriteSchema

class AnalyzeResponse(BaseModel):

    ats: ATSResult

    optimization: OptimizationSchema