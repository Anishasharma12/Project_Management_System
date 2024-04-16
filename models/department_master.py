from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from odoo.tools.translate import _

class DepartmentMaster(models.Model):
    _name = 'department.master'
    _description = 'Department Master Table'
    _rec_name = 'code'

    code = fields.Integer(string='Code', required=True, index=True, unique=True, help='Code must be Unique')
    name = fields.Char(string='Name', required=True)
    order = fields.Integer(string='Order', required=True)
    delete_flag = fields.Boolean(string='Delete Flag', default=False)
    description = fields.Text(string='Description')

    _sql_constraints = [
        ('code_unique', 'UNIQUE(code)', "The code must be unique across all department master records."),
    ]

    @api.model
    def name_create(self, name):
        # Create a new department with the code being the name provided
        # Assuming 'name' is the code that was entered in the Many2one field
        record = self.create({'code': name, 'name': 'Department {}'.format(name)})
        return record.name_get()

