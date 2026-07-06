const resumeInput = document.getElementById("resume");

const jdInput = document.getElementById("jd");

const analyzeBtn = document.getElementById("analyzeBtn");

const loading = document.getElementById("loading");

const results = document.getElementById("results");

const score = document.getElementById("score");

const requiredCoverage = document.getElementById("requiredCoverage");

const preferredCoverage = document.getElementById("preferredCoverage");

const matchedRequired = document.getElementById("matchedRequired");

const missingRequired = document.getElementById("missingRequired");

const matchedPreferred = document.getElementById("matchedPreferred");

const missingPreferred = document.getElementById("missingPreferred");


analyzeBtn.addEventListener("click", analyzeResume);


async function analyzeResume() {

    if (resumeInput.files.length === 0) {

        alert("Please upload a resume.");

        return;
    }

    if (jdInput.value.trim() === "") {

        alert("Please enter a job description.");

        return;
    }

    loading.style.display = "block";

    results.style.display = "none";


    const formData = new FormData();

    formData.append("resume", resumeInput.files[0]);

    formData.append(
        "job_description",
        jdInput.value
    );


    try {

        const response = await fetch(
            "http://127.0.0.1:8000/analyze",
            {
                method: "POST",

                body: formData
            }
        );

        if (!response.ok) {

            throw new Error("Analysis failed.");
        }

        const data = await response.json();


        score.innerText =
            data.ats_score.toFixed(2);


        requiredCoverage.innerText =
            (data.required_skill_coverage * 100).toFixed(2) + "%";


        preferredCoverage.innerText =
            (data.preferred_skill_coverage * 100).toFixed(2) + "%";


        matchedRequired.innerHTML = "";

        missingRequired.innerHTML = "";

        matchedPreferred.innerHTML = "";

        missingPreferred.innerHTML = "";


        data.matched_required.forEach(skill => {

            const li = document.createElement("li");

            li.innerText = "✓ " + skill;

            matchedRequired.appendChild(li);

        });

        data.matched_preferred.forEach(skill => {

            const li = document.createElement("li");

            li.innerText = "✓ " + skill;

            matchedPreferred.appendChild(li);

        });


        data.missing_required.forEach(skill => {

            const li = document.createElement("li");

            li.innerText = "✗ " + skill;

            missingRequired.appendChild(li);

        });

        data.missing_preferred.forEach(skill => {

            const li = document.createElement("li");

            li.innerText = "✗ " + skill;

            missingPreferred.appendChild(li);

        });


        results.style.display = "block";

    }

    catch (error) {

        alert(error.message);

    }

    finally {

        loading.style.display = "none";

    }

}