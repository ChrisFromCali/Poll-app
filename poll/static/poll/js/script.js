/*

let last = $('form .textinput:last-child').last();
addOnClick(last);

function addOnClick(elem) {
    elem.on('keypress', function() {
        elem.prevObject.off('keypress');
        $('form .choice_group').append("<label for='choice'>Choice text*</label>");
        $('form .choice_group').append("<input id='id_choice_text' class='textinput textInput form-control' name='choice_text' maxlength='256' required='' type='text'>");
        last = $('form .textinput:last-child').last();
        addOnClick(last);
    })};

    //last = $('form .choice_input:last-child');
*/

/*
$('#add_option_btn').on('click', function(event) {
    event.preventDefault();
    alert("What");
    let x = $('#div_id_form-' + $('.multiField div').length-1 + '-choice_text').clone(true);
})
*/