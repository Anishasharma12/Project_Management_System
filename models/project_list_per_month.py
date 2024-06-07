from odoo import api, fields, models
import calendar
from odoo.exceptions import ValidationError
from markupsafe import Markup
from odoo.tools import html_escape




class ProjectsPerMonth(models.Model):
    _name = 'project_list_per_month'
    _description = 'project list per month'



    id = fields.Integer("id")
    project_id = fields.Many2one('wb.project_listview', string='Project', required=True)
    month_id = fields.Many2one(
        'month.master',
        string="Month",
        required=True,
        store=True,
        readonly=False
    )
    # month_value = fields.Selection(related='month_id.month', string='Month', store=True, readonly=False)
    # month_button = fields.Html(string='Month Button', compute="_compute_month_button")



    op_planned_hours = fields.Float(string='Hours Planned', compute="_compute_op_planned_hours")
    op_actual_hours = fields.Float(string='Actual Hours',  compute="_compute_op_actual_hours")
    planned_cost = fields.Float(string='planned cost',  compute="_compute_op_planned_cost")
    actual_cost = fields.Float(string='actual cost',  compute="_compute_op_actual_cost")

    project_list_per_month_ids = fields.One2many('project_list_per_month_per_employee', 'month_id', string='Project Months')

    
    _sql_constraints = [
    ('unique_project_month', 'unique(project_id, month_id)', 'The month must be unique per project.')
    ]

    @api.depends('month_id')
    def _compute_month_button(self):
        for record in self:
            if record.month_id:
                month_id_value = record.month_id.month or 'Unknown'  # Or use any other default value          
        

                action_id = self.env.ref('Project_Management.month_id').id  # Replace with your action XML ID
                next_model_url = '/web#action=%s&active_id=%s&model=project_list_per_month_per_employee&view_type=list&cids=1&menu_id=148' % (action_id, record.id)
                record.month_button = Markup(
                    '<P><a href="%s">%s</a></P>' % (next_model_url, html_escape(month_id_value))
                )
    
                # next_model_url = '/web#id=%s&model=project_list_per_month_per_employee&view_type=form' % record.month_id
                # record.month_button = Markup(
                #     '<li><a href="%s">%s</a></li>' % (next_model_url, html_escape(month_id_value))
                # )

                # record.month_button = Markup('<p> <a href="/your/link/here">%s</a> </p>') % month_id_value
            else:
                record.month_button = Markup("<li>null</li>")


    def migrate(cr, version):
        cr.execute("""
        ALTER TABLE project_list_per_month DROP CONSTRAINT IF EXISTS project_list_per_month_unique_month_id;
        ALTER TABLE project_list_per_month ADD CONSTRAINT unique_project_month UNIQUE (project_id, month_id);
        """)

    
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



