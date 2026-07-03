from pydantic import BaseModel, Field


class JDSchema(BaseModel):

    role: str = Field(default="")

    required_skills: list[str] = Field(default_factory=list)

    preferred_skills: list[str] = Field(default_factory=list)

    responsibilities: list[str] = Field(default_factory=list)

    tools: list[str] = Field(default_factory=list)

    soft_skills: list[str] = Field(default_factory=list)

    experience: str = ""

    education: str = ""