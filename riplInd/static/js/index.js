  //scrollIntervalID = setInterval(checkPos, 10);
var headerstrip = $(".headerstrip").outerHeight();
var scrolled, ratio, width, margin;
var w = window.innerWidth;
var h = window.innerHeight;
var offset = 0;

setInterval(function() {
    var active = $(".slide.active");
    var nextItem = active.next();
    if (nextItem.length) {
        currentItem = nextItem.addClass('active');
        active.removeClass('active');
    } else {
        currentItem = $(".slide").first().addClass('active');
        active.removeClass('active');
    }

}, 2000);

function count(counter, end, timeLimit, elemClass) {
    var interval = timeLimit / end;
    var counting = setInterval(function() {
        if (counter < end) {
            counter++;
            $("." + elemClass).text(counter);
        } else {
            clearInterval(counting);
        }
    }, interval);
}
count(0, 100, 1000, "counter");

$(document).ready(function() {
    /* $(document).mousemove(function(event) {
        $("#cover").css({"transform":"translate3d("+0.2*event.pageX+"px,"+0.2*event.pageY+"px,0px","transform-origin":"50% 50%"});
       // $(this).css("top", 50 + 0.002 * event.pageY + "%");
    }); */
$("#abt-list").slider({
	min:1,
	max:5,
	width:180,
	margin:10,
	mode:2
});
$("#prod-list").slider({
	min:1,
	max:12,
	width:250,
	margin:10,
	mode:1
});
$("#sign").slider({
	min:1,
	max:6,
	width:20,
	unit:"%",
	margin:10,
	mode:2,
	controls:'false'
});
$('#uspslide').vslider();

$("#abtslider").children(".subtie").addClass("flex-xs");
});


$(window).resize(function() {

});
var latestKnownScrollY = 0,
    ticking = false,
    fps = 60;

function scroller() {
    latestKnownScrollY = window.scrollY;
    ticker();
}


var ticker = function() {
    if (!ticking) {
        window.requestAnimationFrame(checkPos);
        ticking = true;
    }
};

//parallax
function checkPos() {
    setTimeout(function() {
        scrolled = $(window).scrollTop().toFixed(2);
        $("").css({
            '-webkit-transform': 'translate3d(0px,' + scrolled + 'px,0px)'
        });
        $("").css({
            'transform': 'translate3d(0px,-' + (2) * scrolled + 'px,0px)'
        });
        ticking = false;
    }, 1000 / fps);
}
$(window).scroll(function() {
    scroller();
});

function send_mail(){
    $.ajax({
	url: "index", 
	data: {csrfmiddlewaretoken: csrftoken},
	type:"POST",
	success: function(result){
	alert("Thank you! We will call you back soon.")    }
	});
}
$(".callme").click(send_mail);