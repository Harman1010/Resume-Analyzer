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

const showOptimizationBtn = document.getElementById("showOptimizationBtn");

const optimizationResults = document.getElementById("optimizationResults");

const skillsToHighlight = document.getElementById("skillsToHighlight");

const recommendations = document.getElementById("recommendations");

const summary = document.getElementById("summary");

const generateResumeBtn = document.getElementById("generateResumeBtn");


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

    optimizationResults.style.display = "none";

    showOptimizationBtn.innerText = "View Suggestions";


    const formData = new FormData();

    formData.append("resume", resumeInput.files[0]);

    formData.append(
        "job_description",
        jdInput.value
    );


    try {

        const response = await fetch(
            "https://resume-optimizer.duckdns.org/analyze",
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
            data.ats.ats_score.toFixed(2);


        requiredCoverage.innerText =
            (data.ats.required_skill_coverage * 100).toFixed(2) + "%";


        preferredCoverage.innerText =
            (data.ats.preferred_skill_coverage * 100).toFixed(2) + "%";


        matchedRequired.innerHTML = "";

        missingRequired.innerHTML = "";

        matchedPreferred.innerHTML = "";

        missingPreferred.innerHTML = "";


        data.ats.matched_required.forEach(skill => {

            const li = document.createElement("li");

            li.innerText = "✓ " + skill;

            matchedRequired.appendChild(li);

        });

        data.ats.matched_preferred.forEach(skill => {

            const li = document.createElement("li");

            li.innerText = "✓ " + skill;

            matchedPreferred.appendChild(li);

        });


        data.ats.missing_required.forEach(skill => {

            const li = document.createElement("li");

            li.innerText = "✗ " + skill;

            missingRequired.appendChild(li);

        });

        data.ats.missing_preferred.forEach(skill => {

            const li = document.createElement("li");

            li.innerText = "✗ " + skill;

            missingPreferred.appendChild(li);

        });

        skillsToHighlight.innerHTML = "";
        recommendations.innerHTML = "";

        data.optimization.existing_skills_to_highlight.forEach(skill => {

            const li = document.createElement("li");

            li.innerText = "✓ " + skill;

            skillsToHighlight.appendChild(li);

        });

        data.optimization.recommendations.forEach(item => {

            const li = document.createElement("li");

            li.innerText = item;

            recommendations.appendChild(li);

        });

        summary.innerText =
            data.optimization.summary;

        results.style.display = "block";

    }

    catch (error) {

        alert(error.message);

    }

    finally {

        loading.style.display = "none";

    }

}

showOptimizationBtn.addEventListener("click", () => {

    if (optimizationResults.style.display === "none") {

        optimizationResults.style.display = "block";

        showOptimizationBtn.innerText =
            "Hide Suggestions";

    }

    else {

        optimizationResults.style.display = "none";

        showOptimizationBtn.innerText =
            "View Suggestions";

    }

});

generateResumeBtn.addEventListener(
    "click",
    generateResume
);

async function generateResume() {

    if (resumeInput.files.length === 0) {

        alert("Please upload a resume.");

        return;

    }

    generateResumeBtn.disabled = true;

    generateResumeBtn.innerText =
        "Generating Resume...";

    const formData = new FormData();

    formData.append(
        "resume",
        resumeInput.files[0]
    );

    formData.append(
        "job_description",
        jdInput.value
    );

    try {

        const response = await fetch(

            "https://resume-optimizer.duckdns.org/rewrite",

            {

                method: "POST",

                body: formData

            }

        );

        if (!response.ok) {

            throw new Error(
                "Resume generation failed."
            );

        }

        const blob =
            await response.blob();

        const url =
            window.URL.createObjectURL(blob);

        const a =
            document.createElement("a");

        a.href = url;

        a.download =
            "ATS_Optimized_Resume.docx";

        document.body.appendChild(a);

        a.click();

        a.remove();

        window.URL.revokeObjectURL(url);

    }

    catch (error) {

        alert(error.message);

    }

    finally {

        generateResumeBtn.disabled = false;

        generateResumeBtn.innerText =
            "Generate ATS Optimized Resume";

    }

}