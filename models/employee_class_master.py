from odoo import api, fields, models


class EmployeeClassMaster(models.Model):
    _name = 'employee.class.master'
    _description = 'Employee Class Master Table'

    
    name = fields.Char(string='Name', required=True)
    code = fields.Integer(string='Code', required=True, index=True, unique=True)
    unit_price = fields.Integer(string='Unit Price', required=True)
    delete_flag = fields.Boolean(string='Delete Flag', default=False)
    description = fields.Text(string='Description', required=True)
