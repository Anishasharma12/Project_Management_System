from odoo import api, fields, models
import calendar


class ProjectsPerMonth(models.Model):
    _name = 'project_list_per_month'
    _description = 'project list per month'

    # project_code = fields.One2many('project.master', 'project_assigned_per_month', string='project_code')
    # employee_relation = fields.One2many('project.employee.assign.master', 'employee_project_per_month', string="employee_relation") 
    project_code = fields.Many2one('project.master', string='project_code')
    employee_relation = fields.Many2one('project.employee.assign.master', string="employee_relation") 
    month = fields.Many2one(
        'month.master',
        string="Month",
        help="Select month",
    )
    op_hours_planned = fields.Integer(string='Hours Planned', compute="_compute_hours")
    op_hours_actual = fields.Integer(string='Actual Hours')
    planned_cost = fields.Float(string='planned cost', compute="_compute_cost")
    actual_cost = fields.Float(string='actual cost')

    @api.depends('employee_relation')
    def _compute_hours(self):
        for records in self:
            if records.employee_relation:
                records.op_hours_planned = records.employee_relation.op_hours_planned
                records.op_hours_actual = records.employee_relation.op_hours_actual

    @api.depends('employee_relation')
    def _compute_cost(self):
        for records in self:
            records.planned_cost = records.employee_relation.op_hours_planned * records.employee_relation.employee_code.class_code.unit_price
            records.actual_cost = records.employee_relation.op_hours_actual * records.employee_relation.employee_code.class_code.unit_price
