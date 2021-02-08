var mover = null,
	latestY = 0,
    ticking = false,
	wheight = 0,
	p=[],
    fps = 60;

function onScroll() {
    latestY = window.pageYOffset;					
    requestTick();
}
var requestTick = function() {
    if (!ticking) {
		requestAnimationFrame(animate);
		ticking = true;
    }
};
$(window).scroll(function() {
    onScroll();
});

function animate()
{
		if (mover!=null)
		{
	for (m=0; m<mover.length;m++)
	{					
		var elem = mover[m];
		var animType = $(elem).data("anim-type");
		var beyond = latestY+wheight >= p[m];
		switch (beyond) {
			case true:
				elem.classList.add(animType);
				break;
			default :
				elem.classList.remove(animType);
		}
	}
		}
	ticking=false;
}
$(document).ready(function() {
	mover = document.querySelectorAll(".animate");
	smoothScroll.init();
function init(){
	wheight = $(window).height();
	offset = wheight*0.4;
	for (m=0; m<mover.length;m++)
	{
		p[m]=$(mover[m]).offset().top+offset;
		
	}
};
	$(document).ready(init);
	$(window).on('resize',init);
	$(window).on('resize',animate);
});

(function($) {

$.fn.slider = function(options)
{
	var defaults = {
		controls:'true',
		auto:'false',
		min:1,
		index:0
	};
	options = $.extend({}, defaults, options); 
	var list=this, slider= $(list).closest(".slider"), kids = list.children();
	var viewport, wrapper;
	wrap(list,'tie');
	viewport = $(list).closest(".viewport");
	wrapper = $(list).closest(".wrapper");
	var n=kids.length;
	var p=1, index = options.index, grp, ngrp;
	if(options.max>n)
	{
		options.max=n;
	}
	if(options.min<1)
	{
		options.min=1;
	}
	if(options.controls=='true')
	{
		var prev, next;
		controls();
	}		
	if (options.mode==0)
{
	set(list, 100, 0, "%");
}
	else
{
	set(list, options.width, options.margin, "px");
	var itemWidth = options.width+(2*options.margin);
	var upper = options.max*itemWidth;
	var lower = options.min*itemWidth;
	wrapper.css({"max-width":upper+"px","min-width":lower+"px"});
	$(document).ready(fit);
	$(window).on('resize',fit);

	if (options.mode==2)
{
	var sublist = $(slider).find(".sublist");
	set(sublist, 100, 0, "%");
	wrap(sublist,'subtie');
	kids.on('click', slide);
	kids.css("cursor","pointer");
}
}
	$(document).ready(slide);
	$(window).on('resize',slide);
	function controls()
	{
		wrapper.append('<div class="nav"><a class="prev nav-tag" data-direction="1"><a class="next nav-tag" data-direction="2"></div>');
		prev = slider.find(".prev");
		next = slider.find(".next");
		prev.bind('click',slide);
		next.bind('click',slide);
	}
	function grpset()
	{
		grp = parseInt(index/p);
		ngrp = parseInt((n-1)/p);
	}
	function fit()
	{
		var curWidth = wrapper.width();
		p = parseInt(curWidth/itemWidth);
		if(curWidth <= upper && curWidth >= lower)
		{
			var newWidth = itemWidth*p;
			viewport.css("width",newWidth);
		}
	}

	function slider_nav()
{
		if (grp<ngrp)
		{
			next.show();
		}
		else
		{
			next.hide();
		}
		if (grp>0)
		{
			prev.show();
		}
		else
		{
			prev.hide();
		}
}
	function slide()
{
	if ($(this).data("direction")==1)
	{	
		if(options.mode!=2)
		{
			index -=p;
		}
		else
		{
			index--;
		}
	}
	else if($(this).data("direction")==2)
	{
		if(options.mode!=2)
		{
			index +=p;
		}
		else
		{
			index++;
		}
	}
	else if(event.type=='click')
	{
		index = $(this).index();
	}
	grpset();
	if(options.controls=='true')
	{
		slider_nav();
	}
	translate(list,grp);
		if(options.mode==2)
	{
		tabList(list, sublist, index);//sublist slide and list active item
	}
}
}
$.fn.vslider = function()
{
	//for custom source target css
	var source = this.find(".source");
	var target = this.find(".target");
	var index=0;
	source.children().css("cursor","pointer");
	set(target, 100, 0, "%");
	wrap(target,'subtie');
	wrap(source,'tie');
	function shift(){
	//also call this on resize
	if(event.type!='resize')
	{
		index = $(this).index();
	}
	tabList(source,target,index);
	}
	source.children().bind('click',shift);
	$(window).bind('resize',shift);
}

$.fn.normalize = function()
{

function do_normalize()
{
	var flexi = $(".flexilist");
	var viewport = flexi.closest(".viewport");
	//var featured = flexi.children(".featured");
	var pwidth = viewport.outerWidth();
	var cwidth = flexi.children().not(".featured").outerWidth();
	//var cfwidth = featured.outerWidth();
	var near = parseInt(pwidth/cwidth);
	flexi.css("width",near*cwidth+"px");
}
$(document).on('ready',do_normalize);
$(window).on('resize',do_normalize);
}
/*
$.fn.dropitem = function()
{
	function shufflefaq()
	{
		var wrap = $(this).closest(".faqwrap");
		var index = this.selectedIndex;
		this.options[index].css("display","block");
	}

	$(this).on('change',shuffle);
}*/
return this;
})(jQuery);
function translate(obj, set)
{
	var width = obj.parent().width();
	obj.css("transform","translate3d(-"+set*width+"px, 0px, 0px)");//list slide
}

function set(obj, width, margin, unit)
	{
		var items = obj.children().length;
		var total = (width+(2*margin))*items;
		if(unit=="px")
		{
			obj.children().css({"width": width+unit,"margin": "0 "+margin+"px"});
		}
		else
		{
			width = 100/items;
		}
		obj.css("width", total+unit);
		obj.children().css({"width": width+unit,"margin": "0 "+margin+"px"});
	}
function nset(obj, lwidth, iwidth, margin)
	{
		obj.children().css({"width": iwidth,"margin": "0 "+margin});
		obj.css("max-width", lwidth);
	}
function wrap(obj, outerclass)
	{
		obj.wrap('<div class='+outerclass+'><div class="wrapper"><div class="viewport"></div></div></div>');
	}

function tabList(source, target, set)
{
		source.children(".active").removeClass("active");
		source.children().eq(set).addClass('active');
		translate(target,set);
}
function reveal()
{
	var item = $(this).closest(".faq-item");
	var twrap = $(this).find(".togglewrap");
	var answer = item.find(".answer");
	twrap.toggleClass("rotate");
	answer.slideToggle("fast");
}
//end of slider












$(document).ready(function(){
$(".query").bind('click',reveal);
setTimeout(function()
{
$(".loading" ).removeClass( "loading" );
},2000);

$("#burger").click(function(){
	$(".navbar").toggleClass("display");
});
});

/*! smooth-scroll v10.2.0 | (c) 2016 Chris Ferdinandi | MIT License | http://github.com/cferdinandi/smooth-scroll */
!(function(e,t){"function"==typeof define&&define.amd?define([],t(e)):"object"==typeof exports?module.exports=t(e):e.smoothScroll=t(e)})("undefined"!=typeof global?global:this.window||this.global,(function(e){"use strict";var t,n,o,r,a,c,l,i={},u="querySelector"in document&&"addEventListener"in e,s={selector:"[data-scroll]",selectorHeader:null,speed:500,easing:"easeInOutCubic",offset:0,callback:function(){}},f=function(){var e={},t=!1,n=0,o=arguments.length;"[object Boolean]"===Object.prototype.toString.call(arguments[0])&&(t=arguments[0],n++);for(var r=function(n){for(var o in n)Object.prototype.hasOwnProperty.call(n,o)&&(t&&"[object Object]"===Object.prototype.toString.call(n[o])?e[o]=f(!0,e[o],n[o]):e[o]=n[o])};n<o;n++){var a=arguments[n];r(a)}return e},d=function(e){return Math.max(e.scrollHeight,e.offsetHeight,e.clientHeight)},h=function(e,t){for(Element.prototype.matches||(Element.prototype.matches=Element.prototype.matchesSelector||Element.prototype.mozMatchesSelector||Element.prototype.msMatchesSelector||Element.prototype.oMatchesSelector||Element.prototype.webkitMatchesSelector||function(e){for(var t=(this.document||this.ownerDocument).querySelectorAll(e),n=t.length;--n>=0&&t.item(n)!==this;);return n>-1});e&&e!==document;e=e.parentNode)if(e.matches(t))return e;return null},m=function(e){"#"===e.charAt(0)&&(e=e.substr(1));for(var t,n=String(e),o=n.length,r=-1,a="",c=n.charCodeAt(0);++r<o;){if(t=n.charCodeAt(r),0===t)throw new InvalidCharacterError("Invalid character: the input contains U+0000.");a+=t>=1&&t<=31||127==t||0===r&&t>=48&&t<=57||1===r&&t>=48&&t<=57&&45===c?"\\"+t.toString(16)+" ":t>=128||45===t||95===t||t>=48&&t<=57||t>=65&&t<=90||t>=97&&t<=122?n.charAt(r):"\\"+n.charAt(r)}return"#"+a},p=function(e,t){var n;return"easeInQuad"===e&&(n=t*t),"easeOutQuad"===e&&(n=t*(2-t)),"easeInOutQuad"===e&&(n=t<.5?2*t*t:-1+(4-2*t)*t),"easeInCubic"===e&&(n=t*t*t),"easeOutCubic"===e&&(n=--t*t*t+1),"easeInOutCubic"===e&&(n=t<.5?4*t*t*t:(t-1)*(2*t-2)*(2*t-2)+1),"easeInQuart"===e&&(n=t*t*t*t),"easeOutQuart"===e&&(n=1- --t*t*t*t),"easeInOutQuart"===e&&(n=t<.5?8*t*t*t*t:1-8*--t*t*t*t),"easeInQuint"===e&&(n=t*t*t*t*t),"easeOutQuint"===e&&(n=1+--t*t*t*t*t),"easeInOutQuint"===e&&(n=t<.5?16*t*t*t*t*t:1+16*--t*t*t*t*t),n||t},g=function(e,t,n){var o=0;if(e.offsetParent)do o+=e.offsetTop,e=e.offsetParent;while(e);return o=Math.max(o-t-n,0),Math.min(o,v()-b())},b=function(){return Math.max(document.documentElement.clientHeight,e.innerHeight||0)},v=function(){return Math.max(document.body.scrollHeight,document.documentElement.scrollHeight,document.body.offsetHeight,document.documentElement.offsetHeight,document.body.clientHeight,document.documentElement.clientHeight)},y=function(e){return e&&"object"==typeof JSON&&"function"==typeof JSON.parse?JSON.parse(e):{}},O=function(e){return e?d(e)+e.offsetTop:0},S=function(t,n,o){o||(t.focus(),document.activeElement.id!==t.id&&(t.setAttribute("tabindex","-1"),t.focus(),t.style.outline="none"),e.scrollTo(0,n))};i.animateScroll=function(n,o,c){var i=y(o?o.getAttribute("data-options"):null),u=f(t||s,c||{},i),d="[object Number]"===Object.prototype.toString.call(n),h=d||!n.tagName?null:n;if(d||h){var m=e.pageYOffset;u.selectorHeader&&!r&&(r=document.querySelector(u.selectorHeader)),a||(a=O(r));var b,E,H=d?n:g(h,a,parseInt(u.offset,10)),I=H-m,A=v(),j=0,M=function(t,r,a){var c=e.pageYOffset;(t==r||c==r||e.innerHeight+c>=A)&&(clearInterval(a),S(n,r,d),u.callback(n,o))},w=function(){j+=16,b=j/parseInt(u.speed,10),b=b>1?1:b,E=m+I*p(u.easing,b),e.scrollTo(0,Math.floor(E)),M(E,H,l)},Q=function(){clearInterval(l),l=setInterval(w,16)};0===e.pageYOffset&&e.scrollTo(0,0),Q()}};var E=function(t){e.location.hash;n&&(n.id=n.getAttribute("data-scroll-id"),i.animateScroll(n,o),n=null,o=null)},H=function(r){if(0===r.button&&!r.metaKey&&!r.ctrlKey&&(o=h(r.target,t.selector),o&&"a"===o.tagName.toLowerCase()&&o.hostname===e.location.hostname&&o.pathname===e.location.pathname&&/#/.test(o.href))){var a=m(o.hash);if("#"===a){r.preventDefault(),n=document.body;var c=n.id?n.id:"smooth-scroll-top";return n.setAttribute("data-scroll-id",c),n.id="",void(e.location.hash.substring(1)===c?E():e.location.hash=c)}n=document.querySelector(a),n&&(n.setAttribute("data-scroll-id",n.id),n.id="",o.hash===e.location.hash&&(r.preventDefault(),E()))}},I=function(e){c||(c=setTimeout((function(){c=null,a=O(r)}),66))};return i.destroy=function(){t&&(document.removeEventListener("click",H,!1),e.removeEventListener("resize",I,!1),t=null,n=null,o=null,r=null,a=null,c=null,l=null)},i.init=function(n){u&&(i.destroy(),t=f(s,n||{}),r=t.selectorHeader?document.querySelector(t.selectorHeader):null,a=O(r),document.addEventListener("click",H,!1),e.addEventListener("hashchange",E,!1),r&&e.addEventListener("resize",I,!1))},i}));

