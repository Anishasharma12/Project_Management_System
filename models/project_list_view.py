from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from odoo.tools.translate import _

class ProjectListView(models.Model):
    _name = 'wb.project_listview'
    _description = 'Project List View'
        
 # Assuming the project.master has fields 'name' and 'code'
    project_id = fields.Many2one('project.master', string='Project')
    name = fields.Char(related='project_id.name', string='Project Name')
    code = fields.Integer(related='project_id.code', string='Project Code', store=True, readonly=False)
    op_planned_hours = fields.Float(string='Planned Hours', compute='_compute_op_planned_hours')
    op_actual_hours = fields.Float(string='Actual Hours', compute='_compute_op_actual_hours')
    planned_cost = fields.Float(string='planned cost', compute='op_planned_cost')
    actual_cost = fields.Float(string='Actual cost', compute='op_actual_cost')
    project_list_per_month = fields.Many2many('project_list_per_month', string = "Project assigend per month") 
    project_month_ids = fields.One2many('project_list_per_month', 'project_id', string='Project Months')


    _sql_constraints = [
        ('code_unique', 'unique(code)', 'The project name must be unique in the list view!')
    ]

   #  showing total planned hours which is taken from project_list_per_month model
    @api.depends('project_month_ids.op_planned_hours')
    def _compute_op_planned_hours(self):
        for record in self:
            record.op_planned_hours = sum(record.project_month_ids.mapped('op_planned_hours'))

   #  showing total actual hours which is taken from project_list_per_month model

    @api.depends('project_month_ids.op_actual_hours')
    def _compute_op_actual_hours(self):
        for record in self:
            record.op_actual_hours = sum(record.project_month_ids.mapped('op_actual_hours'))

   #  showing total planned cost which is taken from project_list_per_month model

    @api.depends('project_month_ids.planned_cost')
    def op_planned_cost(self):
        for record in self:
            record.planned_cost = sum(record.project_month_ids.mapped('planned_cost'))

   #  showing total actual cost which is taken from project_list_per_month model
    @api.depends('project_month_ids.actual_cost')
    def op_actual_cost(self):
        for record in self:
            record.actual_cost = sum(record.project_month_ids.mapped('actual_cost'))

   
   
