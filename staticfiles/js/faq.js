document.addEventListener("DOMContentLoaded", function() {
    const faqItems = document.querySelectorAll(".faq-item");

    faqItems.forEach(item => {
        const questionButton = item.querySelector(".faq-question");

        questionButton.addEventListener("click", function() {
            // Toggle the 'open' class
            item.classList.toggle("open");

            // Toggle aria-expanded attribute
            const expanded = questionButton.getAttribute("aria-expanded") === "true";
            questionButton.setAttribute("aria-expanded", !expanded);

            // Toggle visibility of answer
            const answer = item.querySelector(".faq-answer");
            answer.style.display = answer.style.display === "block" ? "none" : "block";
        });
    });
});
