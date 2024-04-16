from odoo import api, fields, models

class ProjectMaster(models.Model):
    _name = "project.master"
    _description = "Project Master Table"
    _rec_name = 'code'  # Set the representative field to 'code'

    code = fields.Char(string='Code', required=True, index=True, unique=True, help='Code must be Unique')
    name = fields.Char(string='Name', required=True)
    order = fields.Integer(string='Order', required=True)
    delete_flag = fields.Boolean(string='Delete Flag', default=False)
    description = fields.Text(string='Description')

    _sql_constraints = [
        ('code_unique', 'UNIQUE(code)', "The code must be unique across all project master records."),
    ]