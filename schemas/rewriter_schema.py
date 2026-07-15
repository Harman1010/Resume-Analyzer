from pydantic import BaseModel

class RewriteSchema(BaseModel):

    profile : str

    education : list[str]
    
    experience : list[str]

    skills : list[str]

    projects : list[str]

    achievements : list[str]