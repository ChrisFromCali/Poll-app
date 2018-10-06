var count = $('.multiField').length - 1;
var last;

$('document').ready(function() {
    var count = $('.multiField').length - 1;
    var last = $('.multiField').last().find('input');
    console.log(last);
    console.log(count)
})

$('#add_option_btn').on('click', function(e) {
    e.preventDefault();
    addField();
})

function addField() {
    count ++;
    let newElem = $('.multiField').last().clone(true);
    newElem.find('div').first().attr('id', 'div_id_form-' + count + '-choice_text');
    newElem.find('label').attr('for', 'id_form-' + count + '-choice_text');
    newElem.find('input').attr('id', 'id_form-' + count + '-choice_text');
    newElem.find('input').attr('name', 'form-' + count + '-choice_text');
    newElem.find('input').val('');
    newElem.appendTo('.choices_group');
    $('form #id_form-TOTAL_FORMS').last().attr('value', count+1);
}