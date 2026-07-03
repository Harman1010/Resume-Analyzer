import re

from core.embeddings import keyword_model

GENERIC_WORDS = {
    "experience",
    "knowledge",
    "ability",
    "understanding",
    "excellent",
    "strong",
    "good",
    "working",
    "using",
    "development",
    "developer",
    "engineering",
    "engineer",
    "application",
    "applications",
    "project",
    "projects",
    "responsible",
    "requirements",
    "skills",
    "skill",
    "team",
    "work",
    "year",
    "years",
    "preferred",
    "required"
}


def clean_phrase(phrase: str) -> str:
    """ 
    Clean extracted keyword.
    """

    phrase = phrase.strip().lower()

    phrase = re.sub(r"[^\w\s\+\#\-\.]", "", phrase)

    return phrase


def extract_resume_skills(resume_text: str) -> list[str]:
    """
    Extract candidate skills/keywords from a resume using KeyBERT.
    """

    keywords = keyword_model.extract_keywords(
        resume_text,
        keyphrase_ngram_range=(1, 3),
        stop_words="english",
        top_n=50,
        use_maxsum=True,
        nr_candidates=100
    )

    extracted = []

    for keyword, score in keywords:

        keyword = clean_phrase(keyword)

        if len(keyword) < 2 or keyword in GENERIC_WORDS:
            continue

        extracted.append(keyword)

    unique_keywords = list(dict.fromkeys(extracted))
    return unique_keywords