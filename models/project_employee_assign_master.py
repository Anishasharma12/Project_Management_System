from odoo import models, fields

class ProjectEmployeeAssignMaster(models.Model):
    _name = 'project.employee.assign.master'
    _description = 'Project Employee Assign Master'

    id = fields.Integer("id")
    project_code = fields.Many2one(
        'project.master',
        string="Project Code",
        help="Select project"
    )

    employee_code = fields.Many2one(
        'employee.master',
        string="Employee Code",
        help="Select employee"
    )
    # employee_code=fields.Integer("Employee Code")
    year = fields.Many2one(
        'year.master',
        string="Year",
        help="Select year"
    )
    month = fields.Many2one(
        'month.master',
        string="Month",
        help="Select month"
    )
    employee_project_per_month = fields.Many2one('project_list_per_month', string="project employee assigned to per month")
    op_hours_planned=fields.Integer("OP hours Planned")
    op_hours_actual=fields.Integer("OP hours Actual")

    # def create(self, vals):
    #     record = super().create(vals)

    #     record = self._create_project_list_per_month(record, vals)

    #     return record

    # def write(self, vals):
    #     res = super().write(vals)

    #     for record in self:
    #         search_created_record = self.env['project_list_per_month'].search(
    #             [('employee_relation', '=', id)])
    #         vals = {
    #             'employee_relation': id,
    #             'project_code': record.project_code,
    #             'month': record.month.month,
    #             'op_planned_hours': record.op_hours_planned,
    #             'op_actual_hours': record.op_hours_actual,
    #             'planned_cost': None,
    #             'actual_cost': None,
    #         }
    #         if search_created_record:
    #             record._create_project_list_per_month.write(vals)

    #         self._create_project_list_per_month(record, vals)
        
    #     return res

    # def _create_project_list_per_month(self, record, vals):
    #     id = record._origin.id
    #     for records in record:
    #         check_record = self.env['project_list_per_month'].search(
    #             [('employee_relation', '=', id)])
    #         vals = {
    #             'employee_relation': id,
    #             'project_code': records.project_code,
    #             'month': records.month.month,
    #             'op_planned_hours': records.op_hours_planned,
    #             'op_actual_hours': records.op_hours_actual,
    #             'planned_cost': None,
    #             'actual_cost': None,
    #         }

    #         if not check_record:
    #             print("creating new records for selected employee")

    #             record.employee_project_per_month.sudo().create(vals)
    #         else:
    #             print("records already created")
    #     return record
