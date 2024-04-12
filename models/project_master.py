from odoo import api, fields, models

class ProjectMaster(models.Model):
    _name = "project.master"
    _description = "Project Master Table"

    code = fields.Char(string='Code', required=True, index=True, unique=True)
    name = fields.Char(string='Name', required=True)
    order = fields.Integer(string='Order', required=True)
    delete_flag = fields.Boolean(string='Delete Flag', default=False)
    description = fields.Text(string='Description')