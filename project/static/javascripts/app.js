$(document).ready(function() {
    $('#messages').on('click', '.like-area', function(event) {
        alert('you clicked the heart!');
        // event.target.preventDefault();
        // event.target.stopPropagation();
    });
});