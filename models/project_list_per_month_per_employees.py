from odoo import api, fields, models

class ProjectsPerMonthPerEmployee(models.Model):
    _name = 'project_list_per_month_per_employee'
    _description = 'project per month employee table'

    
    # project_code = fields.Many2one('project.master', string='project_code')
    # employee_relation = fields.Many2one('project.employee.assign.master', string="employee_relation") 

    month_id = fields.Many2one('project_list_per_month', string='Monthly Project')
   
    employees_assign = fields.Many2one('project.employee.assign.master', string='Employee')
    employee_code = fields.Many2one(related='employees_assign.employee_code', string='Employee code', required=True, store=True, readonly=False)
    employee_name = fields.Char(related='employee_code.name', string='Employee Name')

    # taking for unit price
    employee_class_code = fields.Many2one(related='employee_code.class_code', string='Employee code')
    employee_class_unit_price =  fields.Float(related='employee_class_code.unit_price', string='Employee code')


    op_planned_hours = fields.Integer(string='Planned Hours', compute="_compute_op_planned_hours")
    op_actual_hours = fields.Integer(string='Actual Hours', compute="_compute_op_actual_hours")
    planned_cost = fields.Float(string='planned cost' ,compute="_compute_op_planned_cost")
    actual_cost = fields.Float(string='actual cost' ,compute="_compute_op_actual_cost")

    # # Taking data od employee.master model
    # employee_master_id = fields.One2many('employee.master', string='Project Months')


    _sql_constraints = [
    ('unique_month_employee', 'unique(month_id, employee_code)', 'The month must be unique per project.')
    ]


    employee_assign_per_month_ids = fields.One2many('employee_assign_per_month', 'employees_assign', string='Project Months')


    #    showing total planned hours which is taken from project_list_per_month model
    @api.depends('employee_assign_per_month_ids')
    def _compute_op_planned_hours(self):
        for record in self:
            record.op_planned_hours = 5

    #  showing total planned hours which is taken from project_list_per_month model
    @api.depends('employee_assign_per_month_ids')
    def _compute_op_actual_hours(self):
        for record in self:
            record.op_actual_hours = 6

    @api.depends('employee_class_unit_price', 'op_planned_hours')
    def _compute_op_planned_cost(self):
        for record in self:
            record.planned_cost =  record.employee_class_unit_price * record.op_planned_hours


    @api.depends('employee_class_unit_price', 'op_actual_hours')
    def _compute_op_actual_cost(self):
        for record in self:
            record.actual_cost =  record.employee_class_unit_price * record.op_actual_hours


    # This migrate function is to manage primary key for the employee
    def migrate(cr, version):
        cr.execute("""
        ALTER TABLE project_list_per_month_per_employee DROP CONSTRAINT IF EXISTS project_list_per_month_per_employee_unique_employee_code;
        ALTER TABLE project_list_per_month_per_employee ADD CONSTRAINT unique_project_month UNIQUE (month_id, employee_code);
        """)