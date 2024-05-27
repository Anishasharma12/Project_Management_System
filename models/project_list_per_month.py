from odoo import api, fields, models
import calendar


class ProjectsPerMonth(models.Model):
    _name = 'project_list_per_month'
    _description = 'project list per month'

    # project_code = fields.One2many('project.master', 'project_assigned_per_month', string='project_code')
    # employee_relation = fields.One2many('project.employee.assign.master', 'employee_project_per_month', string="employee_relation") 
    
    project_code = fields.Many2one('project.master', string='project_code')
    employee_relation = fields.Many2many('project.employee.assign.master', string="employee_relation") 
    month = fields.Many2one(
        'month.master',
        string="Month",
        help="Select month",
    )
    op_hours_planned = fields.Integer(string='Hours Planned', compute="_compute_hours")
    op_hours_actual = fields.Integer(string='Actual Hours')
    planned_cost = fields.Float(string='planned cost', compute="_compute_cost")
    actual_cost = fields.Float(string='actual cost')
    project_list_per_month_employee = fields.Many2many('project.list_per_month_employee', string = "Project Employees assigned per month")
    
    @api.model
    def render_button_template(self):
        records = self.search([])
        return self.env['ir.ui.view']._render_template('project_management.dynamic_button_template', {
            'docs': records
        })

    @api.depends('project_list_per_month_employee')
    def _compute_hours(self):
        for records in self:
            project_list = records.project_list_per_month_employee
            
            records.op_hours_planned = sum(project.op_hours_planned for project in project_list)
            records.op_hours_actual = sum(project.op_hours_actual for project in project_list)

    @api.depends('project_list_per_month_employee')
    def _compute_cost(self):
        for records in self:
            # if records.project_code:
            # project_list = self.env['project.list_per_month_employee'].search(
            #     [('project_code', '=', records.project_code.code)])
            # project_list = records.project_list_per_month_employee
            # records.planned_cost = sum([project_list.planned_cost])
            # records.actual_cost = sum([project_list.actual_cost])
            project_list = records.project_list_per_month_employee
            
            # Sum the 'op_hours_planned' and 'op_hours_actual' fields for all related records
            records.planned_cost = sum(project.planned_cost for project in project_list)
            records.actual_cost = sum(project.actual_cost for project in project_list)
