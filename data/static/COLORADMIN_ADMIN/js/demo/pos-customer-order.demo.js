/*
Template Name: Color Admin - Responsive Admin Dashboard Template build with Twitter Bootstrap 4
Version: 4.7.0
Author: Sean Ngu
Website: http://www.seantheme.com/color-admin/admin/
*/

var handleFilter = function() {
	"use strict";
	
	$(document).on('click', '.z_app_pos-menu [data-filter]', function(e) {
		e.preventDefault();
		
		var targetType = $(this).attr('data-filter');
		
		$(this).addClass('active');
		$('.z_app_pos-menu [data-filter]').not(this).removeClass('active');
		if (targetType == 'all') {
			$('.z_app_pos-content [data-type]').removeClass('d-none');
		} else {
			$('.z_app_pos-content [data-type="'+ targetType +'"]').removeClass('d-none');
			$('.z_app_pos-content [data-type]').not('.z_app_pos-content [data-type="'+ targetType +'"]').addClass('d-none');
		}
	});
};
		
$(document).ready(function() {
	handleFilter();
});