document.addEventListener('DOMContentLoaded', function() {
    const dropdownToggle = document.querySelector('.dropdown-toggle');
    const dropdownContent = document.querySelector('.dropdown-content');

    if (dropdownToggle) {
        dropdownToggle.addEventListener('click', function() {
            // Toggle the dropdown content visibility
            if (dropdownContent.style.display === 'block') {
                dropdownContent.style.display = 'none';
            } else {
                dropdownContent.style.display = 'block';
            }
        });

        // Hide dropdown when clicking outside
        window.addEventListener('click', function(e) {
            if (!dropdownToggle.contains(e.target) && !dropdownContent.contains(e.target)) {
                dropdownContent.style.display = 'none';
            }
        });
    }
});
