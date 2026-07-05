from core.ats_engine import ATSEngine

from core.parser import read_pdf

def main():
    
    jd_path = "sample_jd.txt"

    with open(jd_path, "r", encoding="utf-8") as file:
        job_description = file.read()

    with open("HarmanSingh_Resume.pdf", "rb") as file:

        resume_text = read_pdf(file)

    engine = ATSEngine()

    result = engine.analyze(
        resume_path=resume_text,
        job_description=job_description
    )

    print("\n" + "=" * 60)
    print("ATS ANALYSIS RESULT")
    print("=" * 60)

    print(f"\nATS Score: {result.ats_score:.2f}")

    print(f"\nRequired Skill Coverage: {result.required_skill_coverage:.2%}")
    print(f"Preferred Skill Coverage: {result.preferred_skill_coverage:.2%}")

    print("\nMatched Required Skills")
    print("-" * 30)
    for skill in result.matched_required:
        print(f"✓ {skill}")

    print("\nMissing Required Skills")
    print("-" * 30)
    for skill in result.missing_required:
        print(f"✗ {skill}")

    print("\nMatched Preferred Skills")
    print("-" * 30)
    for skill in result.matched_preferred:
        print(f"✓ {skill}")

    print("\nMissing Preferred Skills")
    print("-" * 30)
    for skill in result.missing_preferred:
        print(f"✗ {skill}")


if __name__ == "__main__":
    main()