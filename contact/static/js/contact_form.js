$(document).ready(function(){
    $('#contact-form').submit(function(){
        $.ajax({
            type: "POST",
            url: "/form/contact_form/",
            data: $(this).serialize(),
        }).done(function() {
            alert('Форма отправлена')
			$(this).find('input').val('');
			$('#contact-form').trigger('reset');
        });
        return false;
    });
});