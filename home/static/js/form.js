$(document).ready(function(){
    $('#feedback-form1').submit(function(){
        $.ajax({
            type: "POST",
            url: "/form/parent_form/",
            data: $(this).serialize(),
        }).done(function() {
            alert('Форма отправлена')
			$(this).find('input').val('');
			$('#feedback-form1').trigger('reset');
        });
        return false;
    });
});