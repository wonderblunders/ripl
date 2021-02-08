$( document ).ready(function() {
function count(counter, end, timeLimit, elemClass) {
    var interval = timeLimit / end;
    var counting = setInterval(function() {
        if (counter < end) {
            counter++;
            $(elemClass).html(counter+"<sup>+</sup>");
        } else {
            clearInterval(counting);
        }
    }, interval);
}

var elem = $('.inc');
var counters = $('.stats').data('number');
for (var i=0; i< counters.length; i++)
{
	count(0, counters[i].value, 1500, elem.eq(i));	
}
$("#time-list").slider({
	min:1,
	max:8,
	width:150,
	margin:37.5,
	mode:2,
	index:1
});
$("#boardlist").slider({
	min:1,
	max:4,
	width:300,
	margin:10,
	mode:1,
	index:0
});
$("#timeslider").children(".subtie").addClass("flex-xs");
});

