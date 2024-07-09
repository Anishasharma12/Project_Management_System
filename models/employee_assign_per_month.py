from odoo import api, fields, models
import calendar
import logging

_logger = logging.getLogger(__name__)



class EmployeeAssignPerMonth(models.Model):
    _name = 'employee_assign_per_month'
    _description = 'Employee Assign Per Month'


    employees_assign = fields.Many2one('project_list_per_month_per_employee', string='Monthly Project')


    month_04_total = fields.Float(string='Total April', compute='_compute_totals', store=True)
    month_05_total = fields.Float(string='Total May', compute='_compute_totals', store=True)
    month_06_total = fields.Float(string='Total June', compute='_compute_totals' , store=True)
    month_07_total = fields.Float(string='Total July', compute='_compute_totals', store=True)
    month_08_total = fields.Float(string='Total August', compute='_compute_totals',  store=True)
    month_09_total = fields.Float(string='Total September', compute='_compute_totals',  store=True)
    month_10_total = fields.Float(string='Total October', compute='_compute_totals',  store=True)
    month_11_total = fields.Float(string='Total November', compute='_compute_totals',  store=True)
    month_12_total = fields.Float(string='Total December', compute='_compute_totals', store=True)
    month_01_total = fields.Float(string='Total January', compute='_compute_totals',  store=True)
    month_02_total = fields.Float(string='Total February', compute='_compute_totals',  store=True)
    month_03_total = fields.Float(string='Total March', compute='_compute_totals',  store=True)

    line_ids = fields.One2many('employee_assign_per_month_line', 'assign_per_month_id', string='Assignments', store=True)
    
    _logger.info('hellllo id: %s', line_ids)

        

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
    
    


    

    # def action_add_item(self):
    #     self.env['employee_assign_per_month_line'].create({
    #     'assign_per_month_id': self.id,
    #     'employee_name': 'New Project',
    #         # Add other default values as needed
    #     })
    #     return True


