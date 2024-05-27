odoo.define('Project_Management.my_custom_script', function (require) {
    "use strict";

    // var ListRenderer = require('web.ListRenderer');

    // ListRenderer.include({
    //     events: _.extend({}, ListRenderer.prototype.events, {
    //         'click .o_data_row .custom-clickable': '_onItemClicked',
    //     }),

    //     _onItemClicked: function (event) {
    //         console.log('Item clicked');
    //         event.preventDefault();
    //         event.stopPropagation();

    //         var $item = $(event.currentTarget);
    //         var $row = $item.closest('tr.o_data_row');
    //         var recordId = $row.data('id');

    //         console.log('Record ID:', recordId);

    //         if (recordId) {
    //             var url = '/web#id=' + recordId + '&view_type=form&model=wb.project_listview&menu_id=123&action=456';
    //             console.log('Navigating to URL:', url);
    //             window.location.href = url;
    //         }
    //     },
    // });

});