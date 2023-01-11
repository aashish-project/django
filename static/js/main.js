$(document).ready(function() {
    $('.child').slideToggle(0)
    $('.parent-ele').click(function () { 
        $('.child').slideUp(0.6)
        $('.dropdown').removeClass('rotate');
        $('.parent-ele').removeClass('transition');


        $(this).next('.child').slideDown(0.3);
        $(this).find('.dropdown').addClass('rotate');
        $(this).addClass('transition');
    });

    //if topics are on then hide subject
    if($('.topic').is(":visible")){
        $('.subject_container').hide(0);
    }
    // $('.')
    //item transfer to other container
    $('.topic').click(function () {
        $('#selected_list').prepend(this);
        $('#topic_selected').prepend(this);
        // var val=this.text;
        // console.log(val);
        // var newDiv = $('<div class="link subject topic">' + val + '</div>');
        // $('.select-items').append($(newDiv));
    });
});
