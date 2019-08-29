$(document).ready(function(){
    $('#review-form').submit(function(){
        $.ajax({
            type: "POST",
            url: "/form/recive/",
            data: $(this).serialize(),
        }).done(function() {
            alert('Форма отправлена')
			$(this).find('input').val('');
			$('#review-form').trigger('reset');
        });
        return false;
    });
})