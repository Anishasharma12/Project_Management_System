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
    total = fields.Char(string='total', compute='_compute_total')

    # project_list_per_month_ids = fields.One2many('project_list_per_month_per_employee', 'month_id', string='Project Months')

    month_04_total = fields.Float(string='Total April', compute='_compute_totals')
    month_05_total = fields.Float(string='Total May', compute='_compute_totals')
    month_06_total = fields.Float(string='Total June', compute='_compute_totals')
    month_07_total = fields.Float(string='Total July', compute='_compute_totals')
    month_08_total = fields.Float(string='Total August', compute='_compute_totals')
    month_09_total = fields.Float(string='Total September', compute='_compute_totals')
    month_10_total = fields.Float(string='Total October', compute='_compute_totals')
    month_11_total = fields.Float(string='Total November', compute='_compute_totals')
    month_12_total = fields.Float(string='Total December', compute='_compute_totals')
    month_01_total = fields.Float(string='Total January', compute='_compute_totals')
    month_02_total = fields.Float(string='Total February', compute='_compute_totals')
    month_03_total = fields.Float(string='Total March', compute='_compute_totals')

    
    @api.depends('line_ids')
    def _compute_totals(self):
        for record in self:
            record.month_04_total = sum(line.month_04 for line in record.line_ids)
            record.month_05_total = sum(line.month_05 for line in record.line_ids)
            record.month_06_total = sum(line.month_06 for line in record.line_ids)
            record.month_07_total = sum(line.month_07 for line in record.line_ids)
            record.month_08_total = sum(line.month_08 for line in record.line_ids)
            record.month_09_total = sum(line.month_09 for line in record.line_ids)
            record.month_10_total = sum(line.month_10 for line in record.line_ids)
            record.month_11_total = sum(line.month_11 for line in record.line_ids)
            record.month_12_total = sum(line.month_12 for line in record.line_ids)
            record.month_01_total = sum(line.month_01 for line in record.line_ids)
            record.month_02_total = sum(line.month_02 for line in record.line_ids)
            record.month_03_total = sum(line.month_03 for line in record.line_ids)
