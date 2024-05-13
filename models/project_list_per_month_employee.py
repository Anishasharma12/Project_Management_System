from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from odoo.tools.translate import _

class ProjectListView(models.Model):
    _name = 'project_list_per_month_employee_view'
    _description = 'Project List Per month employee view'

    employee_name = fields.Char(string='Project Name', required=True,  store=True)
    op_planned_hours = fields.Integer(string='Unit Price', store=True)
    op_actual_hours = fields.Integer(string='op actual hours', default=False, store=True)
    planned_cost = fields.Float(string='planned cost', store=True)
    actual_cost = fields.Float(string='actual cost', store=True)


