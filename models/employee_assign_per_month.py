from odoo import api, fields, models
import calendar


class EmployeeAssignPerMonth(models.Model):
    _name = 'employee_assign_per_month'
    _description = 'Employee Assign Per Month'


    employees_assign = fields.Many2one('project_list_per_month_per_employee', string='Monthly Project')
    #     employee_code = fields.Many2one(related='employees_assign.employee_code', string='Employee code')

    
        # name
    employee = fields.Many2one(related='employees_assign.employees_assign', string='employee assign')
    take_project_code = fields.Many2one(related='employee.project_code', string='project_code')
    projects = fields.Char(related='take_project_code.name', string='Project name')

    # taking project name
    project_id = fields.Many2many('project_list_per_month', string='Project')
    # name = fields.Char(related='project_id.name', string='Project Name')
    # code = fields.Integer(related='project_id.code', string='Project Code')

    # month = fields.Many2one(
    #     'month.master',
    #     string="Month",
    #     help="Select month",
    # )

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

    total = fields.Char(string='total', compute='_compute_total')
    line_ids = fields.One2many('employee_assign_per_month_line', 'assign_per_month_id', string='Assignments')


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
    
    

    @api.model
    def add_item(self):
        new_item = self.create({
            'name': 'New Project',
            'month_04': 0,
            'month_05': 0,
            'month_06': 0,
            'month_07': 0,
            'month_08': 0,
            'month_09': 0,
            'month_10': 0,
            'month_11': 0,
            'month_12': 0,
            'month_01': 0,
            'month_02': 0,
            'month_03': 0,
        })
        return new_item
    

    # def action_add_item(self):
    #     self.env['employee_assign_per_month_line'].create({
    #     'assign_per_month_id': self.id,
    #     'employee_name': 'New Project',
    #         # Add other default values as needed
    #     })
    #     return True
    
    @api.depends('total')  # Method depends on these fields
    def _compute_total(self):
        for record in self:
            record.total = 'total' 

    
    @api.depends('total')  # Method depends on these fields
    def _compute_04(self):
        for record in self:
            record._compute_04 = 5