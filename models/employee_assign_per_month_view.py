from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from odoo.tools.translate import _

class ProjectListView(models.Model):
    _name = 'employee_assign_per_month'
    _description = 'Project List Per month employee view'

    project = fields.Char(string='Project Name', required=True,  store=True)
    op_planned_hours = fields.Char(string='Op planned hours', store=True)
    op_actual_hours = fields.Integer(string='op actual hours', default=False, store=True)
    planned_cost = fields.Float(string='planned cost', store=True)
    actual_cost = fields.Float(string='actual cost', store=True)