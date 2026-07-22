import json

from fastapi import APIRouter,Form,UploadFile,File

from fastapi.responses import FileResponse

from core.ats_engine import ATSEngine

from core.optimization_engine import ResumeAnalyzer

from core.parser import read_pdf

from core.rewriter import ResumeRewriter

from schemas.ats_schema import ATSResult

from schemas.optimization_schema import OptimizationSchema

router = APIRouter()

@router.get("/")
def home():
    return {"message" : "Hello, Welcome to AI Resume Optimization!"}

@router.post("/analyze")

async def analyze(resume: UploadFile = File(...),job_description: str = Form(...)):

    resume_text = read_pdf(resume.file)

    #engine = ATSEngine()

    engine = ResumeAnalyzer()

    result = engine.analyze(resume_text=resume_text,job_description=job_description)

    return result.model_dump()

@router.post("/rewrite")
async def rewrite(resume: UploadFile = File(...),ats_result : str = Form(...),optimization: str = Form(...)):

    resume_text = read_pdf(resume.file)

    ats = ATSResult.model_validate(json.loads(ats_result))
    optimization = OptimizationSchema.model_validate(
        json.loads(optimization)
    )

    rewriter = ResumeRewriter()

    file_path = rewriter.rewrite(
        resume_text=resume_text,
        ats_result=ats,
        optimization=optimization
    )

    return FileResponse(
        path=file_path,
        filename="ATS_Optimized_Resume.docx",
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )

