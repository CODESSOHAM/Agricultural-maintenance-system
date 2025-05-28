document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const successMessage = document.createElement("p");
    successMessage.textContent = "Report generated successfully!";
    successMessage.style.color = "green";
    successMessage.style.fontWeight = "bold";
    successMessage.style.display = "none"; // Initially hidden
    form.appendChild(successMessage);

    form.addEventListener("submit", function (event) {
        let isValid = true;
        const inputs = form.querySelectorAll("input, select");

        // Validate input fields
        inputs.forEach(input => {
            if (input.value.trim() === "") {
                isValid = false;
                input.style.border = "2px solid red";
            } else {
                input.style.border = "1px solid #ccc";
            }
        });

        if (!isValid) {
            event.preventDefault(); // Stop form submission if validation fails
            alert("Please fill in all fields correctly!");
        } else {
            successMessage.style.display = "block"; // Show success message
        }
    });

    // Add animation to the report section
    const reportSection = document.querySelector(".report");
    if (reportSection) {
        reportSection.style.opacity = "0";
        reportSection.style.transform = "translateY(20px)";
        setTimeout(() => {
            reportSection.style.opacity = "1";
            reportSection.style.transform = "translateY(0)";
            reportSection.style.transition = "all 0.5s ease-in-out";
        }, 200);
    }
});
