// main.js

document.addEventListener('DOMContentLoaded', function() {
    const dropdownToggle = document.querySelector('.dropdown-toggle');
    const dropdownContent = document.querySelector('.dropdown-content');

    if (dropdownToggle) {
        dropdownToggle.addEventListener('click', function(event) {
            event.stopPropagation();  // Prevent the click from propagating to the window event listener

            // Toggle the dropdown content visibility
            if (dropdownContent.classList.contains('show')) {
                dropdownContent.classList.remove('show');
            } else {
                dropdownContent.classList.add('show');
            }
        });

        // Hide dropdown when clicking outside
        window.addEventListener('click', function(e) {
            if (!dropdownToggle.contains(e.target)) {
                dropdownContent.classList.remove('show');
            }
        });
    }
});
