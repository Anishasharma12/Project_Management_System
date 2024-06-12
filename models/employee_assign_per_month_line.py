from odoo import models, fields

class EmployeeAssignPerMonthLine(models.Model):
    _name = 'employee_assign_per_month_line'
    _description = 'Employee Assign Per Month Line'

    project_id = fields.Many2one('project.master', string='Project')
    name = fields.Char(related='project_id.name', string='Project Name' ,readonly=False)
    code = fields.Integer(related='project_id.code', string='Project Code')
    month_04 = fields.Integer(string='04')
    month_05 = fields.Integer(string='05')
    month_06 = fields.Integer(string='06')
    month_07 = fields.Integer(string='07')
    month_08 = fields.Integer(string='08')
    month_09 = fields.Integer(string='09')
    month_10 = fields.Integer(string='10')
    month_11 = fields.Integer(string='11')
    month_12 = fields.Integer(string='12')
    month_01 = fields.Integer(string='01')
    month_02 = fields.Integer(string='02')
    month_03 = fields.Integer(string='03')
    assign_per_month_id = fields.Many2one('employee_assign_per_month', string='Assign Per Month')
