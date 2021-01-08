/*
Template Name: Color Admin - Responsive Admin Dashboard Template build with Twitter Bootstrap 4
Version: 4.7.0
Author: Sean Ngu
Website: http://www.seantheme.com/color-admin/admin/
*/

var handleDataTableRowReorder = function() {
	"use strict";
    
	if ($('#data-ui_table-rowreorder').length !== 0) {
		$('#data-ui_table-rowreorder').DataTable({
			responsive: true,
			rowReorder: true
		});
	}
};

var TableManageRowReorder = function () {
	"use strict";
	return {
		//main function
		init: function () {
			handleDataTableRowReorder();
		}
	};
}();

$(document).ready(function() {
	TableManageRowReorder.init();
});