from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class EmployeeAssignPerMonthLine(models.Model):
    _name = 'employee_assign_per_month_line'
    _description = 'Employee Assign Per Month Line'

    # project_id = fields.Many2one('project.master', string='Project')
    # name = fields.Char(related='project_id.name', string='Project Name' ,readonly=False)
    # code = fields.Integer(related='project_id.code', string='Project Code')
   
    # project = fields.Many2one('project_list_per_month', string='Project')
    # project_ids = fields.Many2one(related='project.project_id', string='Project Name' ,readonly=False)
    # project_id_s = fields.Many2one(related='project_ids.project_id', string='Project Name' ,readonly=False)
    # name_s = fields.Char(related='project_id.name', string='Project Name' ,readonly=False)
    # code_s = fields.Integer(related='project_id.code', string='Project Code')

    # taking from project.master
    
    project_id = fields.Many2one('project.master', string='Project', domain=lambda self: self._get_project_domain())
    name = fields.Char(related='project_id.name', string='Project Name')
    code = fields.Integer(related='project_id.code', string='Project Code')

    project_employee_assign_id = fields.Many2one('project.employee.assign.master', string='Project Employee assign master id')  
    project_assign_code = fields.Many2one(related='project_employee_assign_id.project_code', string='project code', domain=lambda self: self._get_project_domain())
    project_name = fields.Char(related='project_assign_code.name', string='project name')
    project_code_i = fields.Integer(related='project_assign_code.code', string='project name')
    planning_hours = fields.Integer(related='project_employee_assign_id.op_hours_planned')

    month_code = fields.Many2one(related='project_employee_assign_id.month', string='month code')


   
    month_04 = fields.Integer(string='04', store=True, compute='_compute_months')
    month_05 = fields.Integer(string='05',  store=True, compute='_compute_months')
    month_06 = fields.Integer(string='06',  store=True, compute='_compute_months')
    month_07 = fields.Integer(string='07',  store=True, compute='_compute_months')
    month_08 = fields.Integer(string='08',  store=True, compute='_compute_months')
    month_09 = fields.Integer(string='09',  store=True, compute='_compute_months')
    month_10 = fields.Integer(string='10',  store=True, compute='_compute_months')
    month_11 = fields.Integer(string='11', store=True, compute='_compute_months')
    month_12 = fields.Integer(string='12',  store=True, compute='_compute_months')
    month_01 = fields.Integer(string='01',  store=True, compute='_compute_months')
    month_02 = fields.Integer(string='02',  store=True, compute='_compute_months')
    month_03 = fields.Integer(string='03', store=True, compute='_compute_months')
    assign_per_month_id = fields.Many2one('employee_assign_per_month', string='Assign Per Month')


    @api.depends('project_id')
    def _compute_months(self):
        for record in self:
            project_code = record.code  # Assuming 'code' is the project code
            _logger.debug('Computing month_04 for project code: %s', project_code)
            if project_code == 67:
                domain = [
                    ('project_code', '=', project_code),
                    ('month', '=', 4)  # Assuming 'month' is stored as an integer (April)
                ]
                planned_hours_record = self.env['project.employee.assign.master'].search(domain, limit=1)
                planned_hours = planned_hours_record.op_hours_planned if planned_hours_record else 0
                _logger.debug('Planned hours for project %s, month 04: %s', project_code, planned_hours)
                record.month_04 = planned_hours
            else:
                record.month_04 = 5

    # @api.depends('project_id')
    # def _compute_months(self):
    #     for record in self:

    #         record.month_04 = record.planning_hours

            # _logger.debug('Computing months for project code: %s', project_code)
            # if project_code:
            #     for month in range(1, 13):
            #         month_code = f'{month:04}'
            #         _logger.debug('Processing month: %s', month_code)
            #         month_record = self.env['month.master'].search([('month', '=', month_code)], limit=1)
            #         if month_record:
            #             _logger.debug('Found month record: %s', month_record.month)
            #             domain = [
            #                 ('project_code', '=', project_code),
            #                 ('month', '=', month_record.id)
            #             ]
            #             planned_hours_record = self.env['project.employee.assign.master'].search(domain, limit=1)
            #             planned_hours = planned_hours_record.op_hours_planned if planned_hours_record else 0
            #             _logger.debug('Planned hours for project %s, month %s: %s', project_code, month_code, planned_hours)
            #             setattr(record, f'month_{month_code}', planned_hours)
            #         else:
            #             _logger.warning('No month record found for month: %s', month_code)
            #             _logger.warning('No month record found for month: %s', record.planning_hours)

    @api.model
    def _get_project_domain(self):
        """
        Compute the domain for the project_id field to restrict available projects
        to those listed in the wb.project_listview model.

        This method fetches all project records from the wb.project_listview model,
        extracts their IDs, and constructs a domain that limits the project_id 
        selection to these IDs. This ensures that the user can only select projects
        that are associated with wb.project_listview.

        Returns:
            list: A domain list for filtering the project_id field.
        """
        # Fetch all records from wb.project_listview model
        project_records = self.env['wb.project_listview'].search([])

        # Extract the project_id from each record and get the list of IDs
        project_ids = project_records.mapped('project_id').ids

        # Return the domain to filter project_id field based on the extracted IDs
        return [('id', 'in', project_ids)]
    
