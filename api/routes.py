from fastapi import APIRouter,Form,UploadFile,File

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
async def rewrite(resume: UploadFile = File(...),job_description: str = Form(...)):

    resume_text = read_pdf(resume.file)

    analyzer = ResumeAnalyzer()

    analysis = analyzer.analyze(resume_text=resume_text,job_description=job_description)

    rewriter = ResumeRewriter()

    rewritten_resume = rewriter.rewrite(resume_text=resume_text,ats_result=analysis.ats,optimization=analysis.optimization)

    return rewritten_resume.model_dump()

