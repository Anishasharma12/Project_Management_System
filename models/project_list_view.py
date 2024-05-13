from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from odoo.tools.translate import _

class ProjectListView(models.Model):
    _name = 'wb.project_listview'
    _description = 'Project List View'
        
 # Assuming the project.master has fields 'name' and 'code'
    # project_id = fields.Many2one('project.master', string='Project')
    # name = fields.Char(related='project_id.name', string='Project Name', required=True,  store=True)
    # code = fields.Integer(related='project_id.code', string='Project Code',   required=True, store=True)
   
    id = fields.Integer(string='ID')  # This is your logical link
    name = fields.Char(string=' Name', )
    code = fields.Char(string=' code',)
   
    edit = fields.Char(string=' edit')
    summery = fields.Char(string='Summery ')
    # project_name = fields.Char(string='Project Name',  store=True)
    project_info = fields.Char(string='code    Name', compute='_compute_project_info')
    op_planned_hours = fields.Integer(string='Unit Price', compute='_compute_planned_hours',  store=True)
    op_actual_hours = fields.Integer(string='', default=False, compute='_compute_actual_hours',  store=True)
    planned_cost = fields.Float(string='planned cost',compute='_compute_planned_cost',  store=True)
    actual_cost = fields.Float(string='actual cost', compute='_compute_actual_cost',  store=True)

    @api.model
    def _compute_project_info(self):
        # Assuming we're showing info from the first record as an example
        # This is just an example and might not fit all use cases
        project_record = self.env['project.master'].search([], limit=1)
        if project_record:
            for rec in self:
                rec.project_info = f" {project_record.code}, name: {project_record.name}"
        else:
            for rec in self:
                rec.project_info = "No Project Data Available"
        # for record in self:
        #     month = self.env['project.master'].search([('id', '=', record.id)])
        #     record.name = month.name if month else 'N/A'

    @api.model
    def _compute_code(self):
        for record in self:
            record.code = 'N/A'

            

# this _compute_planned_hours is for function of planned hours
    @api.depends('code')  # Method depends on these fields
    def _compute_planned_hours(self):
        for record in self:
            record.op_planned_hours = 10


# this _compute_actual_hours is for function of planned hours
    @api.depends('code')  # Method depends on dthese fields
    def _compute_actual_hours(self):
        for record in self:
            record.op_actual_hours = 10            

# this _compute_actual_hours is for function of planned hours
    @api.depends('code')  # Method depends on these fields
    def _compute_planned_cost(self):
        for record in self:
            record.planned_cost = 10    



# this _compute_actual_hours is for function of planned hours
    @api.depends('code')  # Method depends on these fields
    def _compute_actual_cost(self):
        for record in self:
            record.actual_cost = 10   

            

# this _compute_actual_hours is for function of planned hours
    @api.depends('name')  # Method depends on these fields
    def _compute_summery(self):
        for record in self:
            record.summery = 'summery'   

        # view_id = self.env.ref('Project_Management.project_list_per_month_form_view').id

    def action_open_another_model_form(self):
        self.ensure_one()  # Ensures that the method is called on a single record
        return  {
            'type': 'ir.actions.act_window',
            'name': _('Project List per Month'),
            'view_mode': 'tree,form',
            'res_model': 'project_list_per_month',  # Specify the target model
            'res_id': self.id,  # Pass the current record's ID
            'target': 'new',  # Open in current window, use 'new' for a new window
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

    
