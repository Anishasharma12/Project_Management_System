from odoo import api, fields, models


class ProjectsPerMonth(models.Model):
    _name = 'project.list.per.month.employee'
    _description = 'project per month employee table'
    
    employee_relation = fields.Many2one('project.employee.assign.master', ondelete="set null", string="employee_relation")
    project_code = fields.Integer(related='employee_relation.project_code.code', string='code')
    month = fields.Many2one(
        'month.master',
        string="Month"
    )
    op_planned_hours = fields.Integer(string='Unit Price')
    op_actual_hours = fields.Integer(string='op actual hours')
    planned_cost = fields.Float(string='planned cost')
    actual_cost = fields.Float(string='actual cost')
   

