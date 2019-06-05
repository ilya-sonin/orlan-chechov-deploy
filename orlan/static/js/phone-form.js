$(document).ready(function(){
    $('#phone-form').submit(function(){
        $.ajax({
            type: "POST",
            url: "/form/phone-form/",
            data: $(this).serialize(),
        }).done(function() {
            alert('Форма отправлена')
			$(this).find('input').val('');
			$('#phone-form').trigger('reset');
        });
        return false;
    });
});