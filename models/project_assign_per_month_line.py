from odoo import models, fields

class EmployeeAssignPerMonthLine(models.Model):
    _name = 'project_assign_per_month_line'
    _description = 'Employee Assign Per Month Line'

    employee_id = fields.Many2one('employee.master', string='Employee')
    name = fields.Char(related='employee_id.name', string='Employee Name' ,readonly=False)
    code = fields.Char(related='employee_id.code', string='Employee Code')
       
    month_04 = fields.Integer(string='04', store=True,)
    month_05 = fields.Integer(string='05', store=True,)
    month_06 = fields.Integer(string='06', store=True,)
    month_07 = fields.Integer(string='07', store=True,)
    month_08 = fields.Integer(string='08', store=True,)
    month_09 = fields.Integer(string='09', store=True,)
    month_10 = fields.Integer(string='10', store=True,)
    month_11 = fields.Integer(string='11', store=True,)
    month_12 = fields.Integer(string='12', store=True,)
    month_01 = fields.Integer(string='01', store=True,)
    month_02 = fields.Integer(string='02', store=True,)
    month_03 = fields.Integer(string='03', store=True,)
    assign_per_month_id = fields.Many2one('project_assign_per_month', string='Assign Per Month')
