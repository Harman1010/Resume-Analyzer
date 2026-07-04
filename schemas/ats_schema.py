from pydantic import BaseModel


class ATSResult(BaseModel):

    ats_score: float

    required_skill_coverage: float
    preferred_skill_coverage: float

    matched_required: list[str]
    missing_required: list[str]

    matched_preferred: list[str]
    missing_preferred: list[str]