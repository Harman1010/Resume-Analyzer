from core.parser import read_pdf

from core.jd_extractor import extract_jd_information
from core.skill_extractor import extract_resume_skills

from core.matcher import match_skills , compute_skill_coverage

from core.scorer import calculate_ats_score

from schemas.ats_schema import ATSResult

class ATSEngine:

    def analyze(self,resume_path: str,job_description: str):

        resume_text = read_pdf(resume_path)

        resume_skills = extract_resume_skills(resume_text)

        jd = extract_jd_information(job_description)

        matched_required, missing_required = match_skills(resume_skills,jd.required_skills)

        matched_preferred, missing_preferred = match_skills(resume_skills,jd.preferred_skills)

        required_coverage = compute_skill_coverage(matched_required,jd.required_skills)

        preferred_coverage = compute_skill_coverage(matched_preferred,jd.preferred_skills)

        ats_score = calculate_ats_score(required_coverage,preferred_coverage)

        return ATSResult(
            ats_score=ats_score,

            required_skill_coverage=required_coverage,
            preferred_skill_coverage=preferred_coverage,

            matched_required=matched_required,
            missing_required=missing_required,

            matched_preferred=matched_preferred,
            missing_preferred=missing_preferred
        )