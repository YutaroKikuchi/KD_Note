"use strict";
const TOUCH = 'ontouchstart' in window ? 'touchend' : 'click';

$(function() {
	console.log("common.js > $(function()) loaded.");
  // headerの初期化
  $(".button-collapse").sideNav();
  
});

