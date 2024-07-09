import sys
sys.setrecursionlimit(1500)

from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class EmployeeAssignPerMonthLine(models.Model):
    _name = 'employee_assign_per_month_line'
    _description = 'Employee Assign Per Month Line'


    # taking from project.master
    
    project_id = fields.Many2one('project.master', string='Project', domain=lambda self: self._get_project_domain(), store=True, required=True)
    name = fields.Char(related='project_id.name', string='Project Name', store=True)
    code = fields.Char(related='project_id.code', string='Project Code', store=True)

   
    month_04 = fields.Integer(string='4', store=True)
    month_05 = fields.Integer(string='5',  store=True)
    month_06 = fields.Integer(string='6',  store=True)
    month_07 = fields.Integer(string='7',  store=True)
    month_08 = fields.Integer(string='8',  store=True)
    month_09 = fields.Integer(string='9',  store=True)
    month_10 = fields.Integer(string='10',  store=True)
    month_11 = fields.Integer(string='11', store=True)
    month_12 = fields.Integer(string='12',  store=True)
    month_01 = fields.Integer(string='1',  store=True)
    month_02 = fields.Integer(string='2',  store=True)
    month_03 = fields.Integer(string='3', store=True)
    assign_per_month_id = fields.Many2one('employee_assign_per_month', string='Assign Per Month', store=True)
 
    # month_id = fields.Many2one('month.master', string='Month', required=True)


    @api.model
    def create(self, vals):
        # Fetch data from another model
        project_code = vals.get('code')
        project_id = vals.get('project_id')
        _logger.info('this is project id: %s', project_id)


        if project_id:
            project = self.env['project.master'].browse(project_id)
            if project:
                project_code = project.code

        
        if project_code:
            assignments = self.env['project.employee.assign.master'].search([
                ('project_code_i', '=', project_code)
            ])

            for assignment in assignments:
                month = assignment.month.month
                planned_hours = assignment.op_hours_planned
                try:
                    month = int(month)  # Ensure month is an integer
                except ValueError:
                    continue  # Skip if month is not an integer

                if 1 <= month <= 12:
                    vals[f'month_{month:02}'] = planned_hours

        # Create the record with updated vals
        record = super(EmployeeAssignPerMonthLine, self).create(vals)
        _logger.info('returned record: %s', record)
        return record

    def write(self, vals):
        res = super(EmployeeAssignPerMonthLine, self).write(vals)
        for record in self:
            record._update_months()
        return res

    def _update_months(self):
        if not self.project_id:
            _logger.info('There is no project: %s', self.id)
            return

        project_code_id = self.project_id.code
        for month in range(1, 13):
            month_str = f'{month:02}'
            # _logger.info(f'There is no project: %s', {month_str}, 'month ma k aayo', month, 'project code ma k ayo' project_code_id)
            _logger.info(f'month str: {month_str} month: {month}, project {project_code_id}')

            assignment = self.env['project.employee.assign.master'].search([
                ('project_code_i', '=', project_code_id),
                ('month.month', '=', month)
            ], limit=1)
            _logger.info('exist assignment?: %s', assignment)

            if assignment:
                planned_hours = assignment.op_hours_planned
            else:
                planned_hours = 65  # Default value

            setattr(self, f'month_{month_str}', planned_hours)



#     @api.model
#     def create(self, vals):
#         record = super(EmployeeAssignPerMonthLine, self).create(vals)
#         record._update_months()
#         return record

#     def write(self, vals):
#         res = super(EmployeeAssignPerMonthLine, self).write(vals)
#         for record in self:
#             record._update_months()
#         return res
    
#     def _update_months2(self):
#         if not self.project_id:
#             _logger.info('No project selected. Record ID: %s', self.id)
#             return
        
#         project_code_id = self.project_id.code
        
#         for month in range(1, 13):
#             month_str = f'{month:02}'
#             _logger.info('Processing month: %s', month_str)

#             # Fetch all assignments for the project and month
#             assignment = self.env['project.employee.assign.master'].search([
#                 ('project_code', '=', project_code_id),
#                 ('month.month', '=', int(month_str))
#             ], limit=1)

#             if assignment:
#                 planned_hours = assignment.op_hours_planned
#                 _logger.info(f'Found matching assignment: {assignment.id} with planned hours: {planned_hours}')
#             else:
#                 planned_hours = 65  # Default value if no assignment is found
#                 _logger.info(f'No matching assignment found for month: {month_str}. Setting planned hours to default: {planned_hours}')
            
#             # Update the respective month field
#             setattr(self, f'month_{month_str}', planned_hours)
#             _logger.info(f'Set month_{month_str} to {planned_hours}')
    
#     def _update_months(self):

        
#         # Initialize the planned hours to 65
#         planned_hours = 65
#         project_code_id = self.project_id.code



        
#         # for month in range(1, 13):
#         #     month_str = f'{month:02}'
#         #     _logger.info('Processing month: %s', month_str)
             
#         #     _logger.info('Record ID1: %s', month_str)

#             # Fetch all assignments for the project and month
#         # assignment_1 = self.env['project.employee.assign.master'].search([
#         #         ('project_code', '=', project_code_id),
#         #         ('month.month', '=', int(month_str))
#         #     ], limit=1)

#         # _logger.info('aaisn: %s', assignment_1)


#         project_code = self.project_id.code
#         _logger.info(f'Updating months for project code: {project_code}')

#         # Fetch all records from project.master
#         all_projects = self.env['project.master'].search([])
#         # Fetch all records from project.employee.assign.master
#         all_assignments = self.env['project.employee.assign.master'].search([])


#         # Log all project codes for debugging
#         project_codes = [project.code for project in all_projects]
#         _logger.info(f'All project codes: {project_codes}')
#         planned_hours = 65

#         # for month in range(1, 13):
#         month_str = 12
#             # _logger.info(f'Updating hours for month: {month_str}')
#         # for month in range(1, 13):
#             # month_str = f'{month:02}'
#             # _logger.info('Processing month: %s', month_str)
#         # Compare and update planned hours
#         for assignment in all_assignments:
#                 _logger.info(f'Checking assignment_5: {assignment.id} with project code: {assignment.project_code.code} selected code is : {project_code_id} month_str : {int(month_str)}')
#                 if assignment.project_code.code == project_code_id and assignment.month.month == int(month_str):
#                     # _logger.info(f'Match found for assignment: {assignment.id}')
#                     # month_str = assignment.month.month  # Ensure the month string is two digits
#                     _logger.info(f'get month string1:{ month_str}')
#                     planned_hours = assignment.op_hours_planned
#                     _logger.info(f'Found matching assignment0: {assignment.id} with planned hours: {planned_hours}')
#                 break
        
#         # Update the respective month field
#         setattr(self, f'month_{month_str}', planned_hours)
#         _logger.info(f'Set month_{month_str} to {planned_hours}')



#     def _update_months1(self):
#         if not self.project_id:
#             _logger.info('No project selected. Record ID: %s', self.id)
#             return
           
#         project_code_id = self.project_id.code
#         project_code = self.code
#         _logger.info(f'here code: {project_code}')
#         _logger.info(f'qqqqqq: {project_code_id}')
#         assignments = self.env['project.employee.assign.master'].search([])
#         _logger.info(f'nnnooooo assignment: {assignments}')

#              # Fetch all records from project.master
#         all_projects = self.env['project.master'].search([])


#             # Log all project codes for debugging
#         project_codes = [project.code for project in all_projects]
#         _logger.info(f'All project codes: {project_codes}')

#         for month in range(1, 13):
#             month_str = f'{month:02}'
#             _logger.info('Processing month: %s', month_str)

#             # Fetch all assignments for the project and month
#             assignment = self.env['project.employee.assign.master'].search([
#                 ('project_code', '=', project_code_id),
#                 ('month.month', '=', int(month_str))
#             ], limit=1)
#             _logger.info(f' assignment:EXIST? {assignment.id} with planned hours: {planned_hours}')
#             if assignment:
#                 planned_hours = assignment.op_hours_planned
#                 _logger.info(f'Found matching assignment: {assignment.id} with planned hours: {planned_hours}')
#             else:
#                 planned_hours = 65  # Default value if no assignment is found
#                 _logger.info(f'No matching assignment found for month: {month_str}. Setting planned hours to default: {planned_hours}')
            
#             # Update the respective month field
#             setattr(self, f'month_{month_str}', planned_hours)
#             _logger.info(f'Set month_{month_str} to {planned_hours}')


# # not solved using compute method
#     @api.depends('project_id')
#     def _compute_months(self):
#         for record in self:
#             if not record.code:
#                 _logger.info('Anisha1')
#                 continue

#             project_code = record.code
#             _logger.info(f'Anisha2: {project_code}')

#             for month in range(1, 13):
#                 _logger.info(f'Anisha3: {month}')

#                 assignment = self.env['project.employee.assign.master'].search([
#                     ('project_code', '=', project_code),
#                     ('month', '=', month)
#                 ], limit=1)

#                 if assignment:
#                     _logger.info(f'Anisha4: {assignment.id} with planned hours: {assignment.op_hours_planned}')
#                 else:
#                     _logger.info(f'Anisha5: {month}')

#                 setattr(record, f'month_{month:02}', assignment.op_hours_planned if assignment else 0)

    # @api.depends('project_id')
    # def _compute_months(self):
    #     for record in self:
    #         project_code = record.code  # Assuming 'code' is the project code
    #         _logger.debug('Computing month_04 for project code: %s', project_code)
    #         if project_code == 67:
    #             domain = [
    #                 ('project_code', '=', project_code),
    #                 ('month', '=', 4)  # Assuming 'month' is stored as an integer (April)
    #             ]
    #             planned_hours_record = self.env['project.employee.assign.master'].search(domain, limit=1)
    #             planned_hours = planned_hours_record.op_hours_planned if planned_hours_record else 0
    #             _logger.debug('Planned hours for project %s, month 04: %s', project_code, planned_hours)
    #             record.month_04 = planned_hours
    #         else:
    #             record.month_04 = 5




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
    
