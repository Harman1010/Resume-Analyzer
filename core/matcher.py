from sentence_transformers import util

from config.settings import SKILL_MATCH_THRESHOLD
from core.embeddings import embedding_model


def match_skills(resume_keywords: list[str],jd_skills: list[str]) -> tuple[list[str], list[str]]:
    """
    Match JD skills against resume keywords using:
    1. Exact matching
    2. Semantic matching
    """

    if not resume_keywords:
        return [], jd_skills

    if not jd_skills:
        return [], []

    resume_keywords = [
        keyword.lower().strip()
        for keyword in resume_keywords
    ]

    jd_skills = [skill.strip() for skill in jd_skills]

    resume_embeddings = embedding_model.encode(resume_keywords,convert_to_tensor=True)

    jd_embeddings = embedding_model.encode(jd_skills,convert_to_tensor=True)

    matched = []
    missing = []

    for skill, skill_embedding in zip(jd_skills,jd_embeddings):
        
        if skill.lower() in resume_keywords:
            matched.append(skill)
            continue

        
        similarities = util.cos_sim(skill_embedding,resume_embeddings)[0]

        if similarities.max().item() >= SKILL_MATCH_THRESHOLD:
            matched.append(skill)
        else:
            missing.append(skill)

    return matched, missing


def compute_skill_coverage(matched_skills: list[str],jd_skills: list[str]) -> float:
    """
    Compute percentage of JD skills covered by the resume.
    """

    if not jd_skills:
        return 1.0

    return round(len(matched_skills) / len(jd_skills),4)