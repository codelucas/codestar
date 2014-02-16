
$(function(){
  $('#datepicker').datepicker({
    inline: true,
    nextText: 'Next',
    prevText: 'Prev',
    showOtherMonths: true,
    dateFormat: 'dd MM yy',
    dayNamesMin: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
    showOn: "button",
    buttonText: "Calendar",
    gotoCurrent: true
  });
});
	