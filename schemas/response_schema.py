from pydantic import BaseModel

from schemas.ats_schema import ATSResult
from schemas.optimization_schema import OptimizationSchema


class AnalyzeResponse(BaseModel):

    ats: ATSResult

    optimization: OptimizationSchema