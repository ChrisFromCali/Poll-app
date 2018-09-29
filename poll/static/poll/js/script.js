let last = $('form input').last();
addOnClick(last);

function addOnClick(elem) {
    elem.on('keypress', function() {
        elem.off('keypress');
        $('form').append("<label for='choice'>Choice</label>");
        $('form').append("<input type='text' class='form-control choice_input'>");
        last = $('form .choice_input:last-child');
        last = $('form input').last();
        addOnClick(last);
    })};

    //last = $('form .choice_input:last-child');