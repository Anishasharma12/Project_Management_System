from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from odoo.tools.translate import _

class ProjectListView(models.Model):
    _name = 'wb.project_listview'
    _description = 'Project List View'
        
 # Assuming the project.master has fields 'name' and 'code'
    project_id = fields.Many2one('project.master', string='Project', required=True)
    name = fields.Char(related='project_id.name', string='Project Name', readonly=True, required=True)
    code = fields.Integer(related='project_id.code', string='Project Code', readonly=True)
    edit = fields.Char(string=' ',)
    summery = fields.Char(string=' ')
    project_name = fields.Char(string='Name', )
    op_planned_hours = fields.Integer(string='Unit Price', compute='_compute_planned_hours')
    op_actual_hours = fields.Integer(string='', default=False, compute='_compute_actual_hours')
    planned_cost = fields.Float(string='planned cost',compute='_compute_planned_cost')
    actual_cost = fields.Float(string='actual cost', compute='_compute_actual_cost')

# this _compute_planned_hours is for function of planned hours
    @api.depends('code')  # Method depends on these fields
    def _compute_planned_hours(self):
        for record in self:
            record.op_planned_hours = 10


# this _compute_actual_hours is for function of planned hours
    @api.depends('code')  # Method depends on these fields
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


    # @api.model
    # def _get_project_info(self):
    #     projects = self.env['project.master'].search([])
    #     project_name_list = []
    #     for project in projects:
    #         project_name_list.append((0, 0, {
    #             'name': project.name,
    #             'code':project.code
    #         }))
    #     self.project_names = project_name_list

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

    def action_details(self):
        # Assuming you have a specific view for details
        view_id = self.env.ref('ProjectAssignSystem.wb_project_tree_view').id
        return {
            'type': 'ir.actions.act_window',
            'name': ('View Details'),
            'res_model': self._name,
            'res_id': self.id,
            'view_mode': 'pivot',
            'views': [(view_id, 'form')],
            'target': 'new',  # Opens in a new window/dialog
        }

    
