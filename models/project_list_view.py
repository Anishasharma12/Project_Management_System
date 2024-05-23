from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from odoo.tools.translate import _

class ProjectListView(models.Model):
    _name = 'wb.project_listview'
    _description = 'Project List View'
        
 # Assuming the project.master has fields 'name' and 'code'
    project_id = fields.Many2one('project.master', string='Project')
    name = fields.Char(related='project_id.name', string='Project Name')
    code = fields.Integer(related='project_id.code', string='Project Code')
    # edit = fields.Char(string=' edit')
    # summery = fields.Char(string='Summery ')
    project_name = fields.Char(string='Name')
    op_planned_hours = fields.Integer(string='Planned hours', compute='_compute_hours')
    op_actual_hours = fields.Integer(string='Actual hours')
    planned_cost = fields.Float(string='Planned cost',compute='_compute_cost')
    actual_cost = fields.Float(string='Actual cost')
    project_list_per_month = fields.Many2many('project_list_per_month', string = "Project assigend per month") 


    @api.depends('project_list_per_month')
    def _compute_hours(self):
        for records in self:
            project_list = self.env['project_list_per_month'].search([('project_code.code', '=', records.code)])
            
            records.op_planned_hours = sum(project.op_hours_planned for project in project_list)
            records.op_actual_hours = sum(project.op_hours_actual for project in project_list)
      
    @api.depends('project_list_per_month')
    def _compute_cost(self):
        for records in self:
            project_list = self.env['project_list_per_month'].search([('project_code.code', '=', records.code)])
            
            records.planned_cost = sum(project.planned_cost for project in project_list)
            records.actual_cost = sum(project.actual_cost for project in project_list)


    def action_view_summary(self):
        return  {
            'type': 'ir.actions.act_window',
            'name': _('Project List per Month'),
            'view_mode': 'tree,form',
            'res_model': 'project_list_per_month',
            'res_id': self.id,
            'domain': [('project_code', '=', self.code)],
            'target': 'new',
            'context': {'create': False},
        }
   
    # def action_view_invoice(self):
    #     self.ensure_one()
    #     query = self.env['account.move.line']._search([('move_id.move_type', 'in', self.env['account.move'].get_sale_types())])
    #     query.add_where('analytic_distribution ? %s', [str(self.id)])
    #     query_string, query_param = query.select('DISTINCT account_move_line.move_id')
    #     self._cr.execute(query_string, query_param)
    #     move_ids = [line.get('move_id') for line in self._cr.dictfetchall()]
    #     result = {
    #         "type": "ir.actions.act_window",
    #         "res_model": "account.move",
    #         "domain": [('id', 'in', move_ids)],
    #         "context": {"create": False, 'default_move_type': 'out_invoice'},
    #         "name": _("Customer Invoices"),
    #         'view_mode': 'tree,form',
    #     }
    #     return result


    def action_edit(self):
        # Return an action that opens the form view of the current record in edit mode
        return {
            'type': 'ir.actions.act_window',
            'name': ('Edit Record'),
            'res_model': self._name,
            'res_id': self.id,
            'view_mode': 'form',
            'target': 'current',
            'flags': {'mode': 'edit'},
        }

    
