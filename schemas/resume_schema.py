from pydantic import BaseModel, Field


class ATSResult(BaseModel):

    ats_score: float

    semantic_score: float

    skill_match_score: float

    critical_skill_score: float

    keyword_match_score: float

    matched_skills: list[str] = Field(default_factory=list)

    missing_skills: list[str] = Field(default_factory=list)