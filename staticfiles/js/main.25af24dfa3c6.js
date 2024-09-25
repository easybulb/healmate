document.addEventListener('DOMContentLoaded', function () {
    var dropdownToggle = document.querySelector('.dropdown-toggle');
    var dropdownContent = document.querySelector('.dropdown-content');

    dropdownToggle.addEventListener('click', function () {
        dropdownContent.classList.toggle('show');
    });
});
