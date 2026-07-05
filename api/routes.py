from fastapi import APIRouter,Form,UploadFile,File

from core.ats_engine import ATSEngine

from core.parser import read_pdf

router = APIRouter()

@router.get("/")
def home():
    return {"message" : "Hello, Welcome to AI Resume Optimization!"}

@router.post("/analyze")

async def analyze(resume: UploadFile = File(...),job_description: str = Form(...)):

    resume_text = read_pdf(resume.file)

    engine = ATSEngine()

    result = engine.analyze(resume_text=resume_text,job_description=job_description)

    return result.model_dump()



