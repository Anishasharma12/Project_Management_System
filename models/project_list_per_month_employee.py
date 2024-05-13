from odoo import api, fields, models


class ProjectsPerMonth(models.Model):
    _name = 'project.list.per.month.employee'
    _description = 'project per month employee table'
    
    project_code = fields.Many2one('project.master', string='project_code')
    employee_relation = fields.Many2one('project.employee.assign.master', string="employee_relation") 
    month = fields.Date(string='Month', compute="_compute_month")
    op_hours_planned = fields.Integer(string='Unit Price')
    op_hours_actual = fields.Integer(string='op actual hours')
    planned_cost = fields.Float(string='planned cost')
    actual_cost = fields.Float(string='actual cost')
    project_list_per_month = fields.Many2Many('project_list_per_month', string = "Project assigend per month") 

    @api.depends('employee_relation')
    def _compute_month(self):
        for records in self:
            records.month = records.employee_relation.month
   
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
