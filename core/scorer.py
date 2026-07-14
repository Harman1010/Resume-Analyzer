from config.settings import REQUIRED_SKILL_WEIGHT,PREFERRED_SKILL_WEIGHT


def calculate_ats_score(required_coverage: float,preferred_coverage: float) -> float:
    """
    Calculate final ATS score.
    """

    score = ( required_coverage * REQUIRED_SKILL_WEIGHT + preferred_coverage * PREFERRED_SKILL_WEIGHT )

    return round(score * 100, 2)