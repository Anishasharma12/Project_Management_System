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
    project_id = fields.Many2many('project.master', string='Project')
    name = fields.Char(related='project_id.name', string='Project Name')
    code = fields.Integer(related='project_id.code', string='Project Code')
    total = fields.Integer(string='Project Code')
    line_ids = fields.One2many('employee_assign_per_month_line', 'assign_per_month_id', string='Assignments')

    

    month = fields.Many2one(
        'month.master',
        string="Month",
        help="Select month",
    )

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
    
    

    # @api.model
    # def add_item(self):
    #     # Define the logic to add a new item
    #     new_item = self.create({
    #         'name': 'New Project',
    #         'month_04': 0,
    #         'month_05': 0,
    #         'month_06': 0,
    #         'month_07': 0,
    #         'month_08': 0,
    #         'month_09': 0,
    #         'month_10': 0,
    #         'month_11': 0,
    #         'month_12': 0,
    #         'month_01': 0,
    #         'month_02': 0,
    #         'month_03': 0,
    #     })
    #     return new_item
    
# this code works
    # def action_add_item(self):
    #     # Create a new record with default values
    #     new_record = self.create({
    #         'name': 'New Item',
    #     })
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'view_mode': 'form',
    #         'res_model': 'employee_assign_per_month',
    #         'res_id': new_record.id,
    #         'target': 'current',
    #     }

    def action_add_item(self):
        self.env['employee_assign_per_month_line'].create({
        'assign_per_month_id': self.id,
        'project_name': 'New Project',
            # Add other default values as needed
        })
        return True