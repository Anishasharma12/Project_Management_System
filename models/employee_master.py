from odoo import api, fields, models
from odoo.exceptions import ValidationError

class EmployeeMaster(models.Model):
    _name = 'employee.master'
    _description = 'Employee Master Table'

    code = fields.Integer(string='Code', required=True, index=True, unique=True , help='Code must be Unique')
    name = fields.Char(string='Name', required=True)

    # Many2one relationships
    department_code = fields.Many2one('department.master', string='Department code' , required=True, help='Enter Department Code', index = True)
    class_code = fields.Many2one('employee.class.master', string='Class code' , required=True, help='Enter Department Code', index = True)

    delete_flag = fields.Boolean(string='Delete Flag', default=False)
    description = fields.Text(string='Description')

    # @api.constrains('department_code')
    # def _check_department_code(self):
    #     for record in self:
    #         if record.department_code and not record.department_code.exists():
    #             raise ValidationError("The Department code does not exist or is incorrect.")

    # @api.constrains('class_code')
    # def _check_class_code(self):
    #     for record in self:
    #         if record.class_code and not record.class_code.exists():
    #             raise ValidationError("The Class code does not exist or is incorrect.")
    
    _sql_constraints = [
        ('code_unique', 'UNIQUE(code)', "The code must be unique across all employee master records."),
    ]
