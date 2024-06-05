from odoo import api, fields, models
import calendar
from odoo.exceptions import ValidationError



class ProjectsPerMonth(models.Model):
    _name = 'project_list_per_month'
    _description = 'project list per month'



    id = fields.Integer("id")
    project_id = fields.Many2one('wb.project_listview', string='Project')
    month_id = fields.Many2one(
        'month.master',
        string="Month",
        help="Select month",
    )
    op_planned_hours = fields.Float(string='Hours Planned', compute="_compute_op_planned_hours")
    op_actual_hours = fields.Float(string='Actual Hours',  compute="_compute_op_actual_hours")
    planned_cost = fields.Float(string='planned cost',  compute="_compute_op_planned_cost")
    actual_cost = fields.Float(string='actual cost',  compute="_compute_op_actual_cost")

    project_list_per_month_ids = fields.One2many('project_list_per_month_per_employee', 'month_id', string='Project Months')


    _sql_constraints = [
        ('unique_month', 'unique(month)', 'The month must be unique.')
    ]
    
    #  showing total planned hours which is taken from project_list_per_month model
    @api.depends('project_list_per_month_ids.op_planned_hours')
    def _compute_op_planned_hours(self):
        for record in self:
            record.op_planned_hours = sum(record.project_list_per_month_ids.mapped('op_planned_hours'))

    #  showing total planned hours which is taken from project_list_per_month model
    @api.depends('project_list_per_month_ids.op_actual_hours')
    def _compute_op_actual_hours(self):
        for record in self:
            record.op_actual_hours = sum(record.project_list_per_month_ids.mapped('op_actual_hours'))

    @api.depends('project_list_per_month_ids.planned_cost')
    def _compute_op_planned_cost(self):
        for record in self:
            record.planned_cost = sum(record.project_list_per_month_ids.mapped('planned_cost'))

    @api.depends('project_list_per_month_ids.actual_cost')
    def _compute_op_actual_cost(self):
        for record in self:
            record.actual_cost = sum(record.project_list_per_month_ids.mapped('actual_cost'))




    # @api.depends('project_list_per_month_employee')
    # def _compute_hours(self):
    #     for records in self:
    #         project_list = records.project_list_per_month_employee
            
    #         records.op_planned_hours = sum(project.op_planned_hours for project in project_list)
    #         records.op_actual_hours = sum(project.op_actual_hours for project in project_list)

    # @api.depends('project_list_per_month_employee')
    # def _compute_cost(self):
    #     for records in self:

    #         project_list = records.project_list_per_month_employee
            
    #         # Sum the 'op_hours_planned' and 'op_hours_actual' fields for all related records
    #         records.planned_cost = sum(project.planned_cost for project in project_list)
    #         records.actual_cost = sum(project.actual_cost for project in project_list)

