from odoo import api, fields, models
from odoo.exceptions import ValidationError

class EmployeeMaster(models.Model):
    _name = 'employee.master'
    _description = 'Employee Master Table'
    _rec_name = 'code' 

    code = fields.Integer(string='Code', required=True, index=True, unique=True , help='Code must be Unique')
    name = fields.Char(string='Name', required=True)

    # Many2one relationships
    department_code = fields.Many2one('department.master', string='Department code' , required=True, help='Enter Department Code', index = True)
    class_code = fields.Many2one('employee.class.master', string='Employee Class code' , required=True, help='Enter Employee Code', index = True)

    delete_flag = fields.Boolean(string='Delete Flag', default=False)
    description = fields.Text(string='Description')


    _sql_constraints = [
        ('code_unique', 'UNIQUE(code)', "The code must be unique across all employee master records."),
    ]
