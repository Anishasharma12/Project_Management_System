from odoo import api, fields, models


class EmployeeMaster(models.Model):
    _name = 'employee.master'
    _description = 'Employee Master Table'
    _rec_name = 'code' 

    code = fields.Integer(string='Code', required=True, index=True, unique=True)
    name = fields.Char(string='Name', required=True)
    department_code = fields.Many2one('department.master', string='Department Code', required=True)
    class_code = fields.Many2one('employee.class.master', string='Class Code', required=True)
    delete_flag = fields.Boolean(string='Delete Flag', default=False, required=True)
    description = fields.Text(string='Description', required=True)
