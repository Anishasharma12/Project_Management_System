from odoo import api, fields, models

class ProjectMaster(models.Model):
    _name = "project.master"
    _description = "Project Master Table"
    _rec_name = 'code'  # Set the representative field to 'code'

    code = fields.Integer(string='Code', required=True, index=True, unique=True, help='Code must be Unique')
    name = fields.Char(string='Name', required=True)
    order = fields.Integer(string='Order', required=True)
    delete_flag = fields.Boolean(string='Delete Flag', default=False)
    description = fields.Text(string='Description', required=True)

    project_assigned_per_month = fields.Many2one('project_list_per_month', string='Project assigned per month')
    employee_assign_ids = fields.Many2many('employee_assign_per_month', string='Employee Assignments')


    # Code should be unique , so here defining code is unique using sql constrain
    _sql_constraints = [
        ('code_unique', 'UNIQUE(code)', "The code must be unique across all project master records."),
    ]