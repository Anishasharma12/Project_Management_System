from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from odoo.tools.translate import _

class EmployeeClassMaster(models.Model):
    _name = 'employee.class.master'
    _description = 'Employee Class Master Table'
    _rec_name = 'code'
    
    name = fields.Char(string='Name', required=True)
    code = fields.Integer(string='Code', required=True, index=True, unique=True, help='Code must be Unique')
    unit_price = fields.Float(string='Unit Price', required=True)
    delete_flag = fields.Boolean(string='Delete Flag', default=False)
    description = fields.Text(string='Description')

    _sql_constraints = [
        ('code_unique', 'UNIQUE(code)', "The code must be unique across all employee class master records."),
    ]
