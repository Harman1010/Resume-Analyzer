from pydantic import BaseModel, Field


class ResumeSchema(BaseModel):

    technical_skills: list[str] = Field(
        default_factory=list,
        description="Programming languages, frameworks, libraries, databases, cloud platforms, tools, software, technologies and technical concepts explicitly mentioned in the resume."
    )