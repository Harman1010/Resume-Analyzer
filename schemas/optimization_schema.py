from pydantic import BaseModel

class OptimizationSchema(BaseModel):

    existing_skills_to_highlight: list[str]

    recommendations: list[str]

    summary: str