document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    const tooltipElements = document.querySelectorAll('[data-tooltip]');
    tooltipElements.forEach(function(element) {
        element.addEventListener('mouseenter', function() {
            const tooltipText = element.getAttribute('data-tooltip');
            const tooltip = document.createElement('div');
            tooltip.className = 'tooltip';
            tooltip.innerText = tooltipText;
            document.body.appendChild(tooltip);
            const rect = element.getBoundingClientRect();
            tooltip.style.left = `${rect.left + window.scrollX}px`;
            tooltip.style.top = `${rect.bottom + window.scrollY}px`;
        });

        element.addEventListener('mouseleave', function() {
            const tooltip = document.querySelector('.tooltip');
            if (tooltip) {
                tooltip.remove();
            }
        });
    });

    // Quiz functionality
    const quizForm = document.getElementById('quiz-form');
    if (quizForm) {
        quizForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const formData = new FormData(quizForm);
            const answers = {};
            formData.forEach((value, key) => {
                answers[key] = value;
            });
            // Process answers (e.g., send to server or display results)
            console.log(answers);
            alert('Quiz submitted! Check the console for your answers.');
        });
    }

    // Poll functionality
    const pollForm = document.getElementById('poll-form');
    if (pollForm) {
        pollForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const selectedOption = document.querySelector('input[name="poll-option"]:checked');
            if (selectedOption) {
                const pollAnswer = selectedOption.value;
                // Process poll answer (e.g., send to server)
                console.log(`Poll answer submitted: ${pollAnswer}`);
                alert('Thank you for your response!');
            } else {
                alert('Please select an option before submitting.');
            }
        });
    }
});