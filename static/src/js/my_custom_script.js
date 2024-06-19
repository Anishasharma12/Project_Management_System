// odoo.define('Project_Management.my_custom_script', function (require) {
//     "use strict";

//     var fieldRegistry = require('web.field_registry');
//     var FieldMany2one = require('web.relational_fields').FieldMany2one;

//     var ClickableMonthField = FieldMany2one.extend({
//         events: _.extend({}, FieldMany2one.prototype.events, {
//             'click': '_onClick',
//         }),

//         _onClick: function (event) {
//             event.preventDefault();
//             var self = this;
//             this._rpc({
//                 model: 'project_list_per_month',
//                 method: 'search_read',
//                 domain: [['id', '=', this.res_id]],
//                 fields: ['month_id'],
//             }).then(function (result) {
//                 if (result.length > 0) {
//                     var month_id = result[0].month_id[0];
//                     var action = {
//                         type: 'ir.actions.act_window',
//                         name: 'Project List Per Month Per Employee',
//                         res_model: 'project_list_per_month_per_employee',
//                         view_mode: 'tree,form',
//                         domain: [['month_id', '=', month_id]],
//                         target: 'current',
//                     };
//                     self.do_action(action);
//                 }
//             });
//         },
//     });

//     fieldRegistry.add('clickable_month', ClickableMonthField);
// });
