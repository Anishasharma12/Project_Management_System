from odoo import api, fields, models

class ProjectsPerMonthPerEmployee(models.Model):
    _name = 'project_list_per_month_per_employee'
    _description = 'project per month employee table'
    
    # project_code = fields.Many2one('project.master', string='project_code')
    # employee_relation = fields.Many2one('project.employee.assign.master', string="employee_relation") 
    # employees_assign = fields.Many2one('project.employee.assign.master', string='Employee')
    op_hours_planned = fields.Integer(string='Unit Price')
    op_hours_actual = fields.Integer(string='op actual hours')
    planned_cost = fields.Float(string='planned cost')
    actual_cost = fields.Float(string='actual cost')