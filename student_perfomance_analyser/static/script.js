function analyzeStudent() {
    const data = {
        name: document.getElementById("name").value,
        roll: document.getElementById("roll").value,
        section: document.getElementById("section").value,

        maths: document.getElementById("maths").value,
        python: document.getElementById("python").value,
        ai: document.getElementById("ai").value,
        mechanical: document.getElementById("mechanical").value,
        chemistry: document.getElementById("chemistry").value,
        communication: document.getElementById("communication").value
    };

    fetch("/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        let output = `
            <h2>Student Result</h2>
            <p><b>Name:</b> ${result.name}</p>
            <p><b>Roll No:</b> ${result.roll}</p>
            <p><b>Section:</b> ${result.section}</p>

            <p><b>Total Marks:</b> ${result.total_marks}</p>
            <p><b>Percentage:</b> ${result.percentage}%</p>

            <h3 style="color:${result.result === "PASS" ? "green" : "red"}">
                Result: ${result.result}
            </h3>
        `;

        if (result.failed_subjects.length > 0) {
            output += `<h4>Failed Subjects:</h4><ul>`;
            result.failed_subjects.forEach(sub => {
                output += `<li>${sub}</li>`;
            });
            output += `</ul>`;
        }

        output += `<h4>Overall Suggestion:</h4><p>${result.suggestion}</p>`;

        if (result.subject_suggestions.length > 0) {
            output += `<h4>Subject-wise Suggestions:</h4><ul>`;
            result.subject_suggestions.forEach(msg => {
                output += `<li>${msg}</li>`;
            });
            output += `</ul>`;
        }

        document.getElementById("result").innerHTML = output;
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("result").innerHTML =
            "<p style='color:red'>Something went wrong. Try again.</p>";
    });
}
