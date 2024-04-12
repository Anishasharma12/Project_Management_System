from odoo import api, fields, models

class DepartmentMaster(models.Model):
    _name = 'department.master'
    _description = 'Department Master Table'

    code = fields.Char(string='Code', required=True, index=True, unique=True)
    name = fields.Char(string='Name', required=True)
    order = fields.Integer(string='Order', required=True)
    delete_flag = fields.Boolean(string='Delete Flag', default=False)
    description = fields.Text(string='Description')
