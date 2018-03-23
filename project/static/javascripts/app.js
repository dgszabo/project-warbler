$(document).ready(function() {
    $('#messages').on('click', '.like-area', function(event) {
        event.preventDefault();
        event.stopPropagation();
    
        var user_id = event.target.closest('div').id.split('.')[0];
        var message_id = event.target.closest('div').id.split('.')[1];
        
        if($(event.target).closest('div > i').hasClass('fa-heart-o')) {
            $.ajax({
                method: 'POST',
                url: 'http://localhost:5000/users/' + user_id + '/messages/ajax/' + message_id + '/likes'
            }).then(function(data) {
                $(event.target).closest('div > i').removeClass('fa-heart-o').addClass('fa-heart');
            });
        } else {
            $.ajax({
                method: 'DELETE',
                url: 'http://localhost:5000/users/' + user_id + '/messages/ajax/' + message_id + '/likes'
            }).then(function(data) {
                $(event.target).closest('div > i').removeClass('fa-heart').addClass('fa-heart-o');
            });
        }
    });
});

