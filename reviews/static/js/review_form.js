$(document).ready(function(){
    $('#review-form').submit(function(){
        $.ajax({
            type: "POST",
            url: "/reviews/form/recive/",
            data: $(this).serialize(),
        }).done(function() {
            alert('Отзыв отправлен на обработку')
			$(this).find('input').val('');
			$('#review-form').trigger('reset');
        });
        return false;
    });
})