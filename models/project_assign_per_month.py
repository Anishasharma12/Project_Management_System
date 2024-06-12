from odoo import api, fields, models
import calendar
from odoo.exceptions import ValidationError



class ProjectsAssignPerMonth(models.Model):
    _name = 'project_assign_per_month'
    _description = 'project list per month'



    id = fields.Integer("id")
    project_id = fields.Many2one('wb.project_listview', string='Project', required=True)
    month_id = fields.Many2one(
        'month.master',
        string="Month",
        help="Select month",
        required=True,
        store=True,
        readonly=False
    )

    line_ids = fields.One2many('project_assign_per_month_line', 'assign_per_month_id', string='Assignments')

    # project_list_per_month_ids = fields.One2many('project_list_per_month_per_employee', 'month_id', string='Project Months')

    month_04 = fields.Integer(string='04')
    month_05 = fields.Integer(string='05')
    month_06 = fields.Integer(string='06')
    month_07 = fields.Integer(string='07')
    month_08 = fields.Integer(string='08')
    month_09 = fields.Integer(string='09')
    month_10 = fields.Integer(string='10')
    month_11 = fields.Integer(string='11')
    month_12 = fields.Integer(string='12')
    month_01 = fields.Integer(string='01')
    month_02 = fields.Integer(string='02')
    month_03 = fields.Integer(string='03')

    # This  
    def action_add_item(self):
        self.env['project_assign_per_month_line'].create({
        'assign_per_month_id': self.id,
        'project_name': 'New Project',
            # Add other default values as needed
        })
        return True
