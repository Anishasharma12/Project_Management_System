from odoo import models, fields

class ProjectEmployeeAssignMaster(models.Model):
    _name = 'wb.projectemployeemaster'
    _description = 'Project Employee Assign Master'

    id = fields.Integer("id")
    # project_code = fields.Integer("Project Code") 
    project_code = fields.Many2one(
        'project.master',  # This is the model you are referencing
        string="Project Code",   # Label of the field
        required=True,      # If the field is mandatory
        help="Select project",  # Help tooltip
        index=True  # Creates an index on this column in the database for faster querying
    )

    employee_code = fields.Many2one(
        'employee.master',  # This is the model you are referencing
        string="Employee Code",  # Label of the field
        required=True,
        help="Select employee",
        index=True
    )
    # employee_code=fields.Integer("Employee Code")
    year = fields.Many2one(
        'year.master',  # This is the model you are referencing
        string="Year",  # Label of the field
        required=True,
        help="Select year",
        index=True
    )
    month = fields.Many2one(
        'month.master',  # This is the model you are referencing
        string="Month",  # Label of the field
        required=True,
        help="Select month",
        index=True
    )
    employee_project_per_month = fields.One2many('project_list_per_month', 'employee_relation', string="project employee assigned to per month")
    op_hours_planned=fields.Integer("OP hours Planned")
    op_hours_actual=fields.Integer("OP hours Actual")

    def create(self, vals):
        record = super().create(vals)

        record = self._create_project_list_per_month(record, vals)

        return record

    def write(self, vals):
        res = super().write(vals)

        for record in self:
            search_created_record = self.env['project_list_per_month'].search(
                [('employee_relation', '=', id)])
            vals = {
                'employee_relation': id,
                'project_code': record.project_code,
                'month': record.month.month,
                'op_planned_hours': record.op_hours_planned,
                'op_actual_hours': record.op_hours_actual,
                'planned_cost': None,
                'actual_cost': None,
            }
            if search_created_record:
                record._create_project_list_per_month.write(vals)

            self._create_project_list_per_month(record, vals)
        
        return res

    def _create_project_list_per_month(self, record, vals):
        id = record._origin.id
        for records in record:
            check_record = self.env['project_list_per_month'].search(
                [('employee_relation', '=', id)])
            vals = {
                'employee_relation': id,
                'project_code': records.project_code,
                'month': records.month.month,
                'op_planned_hours': records.op_hours_planned,
                'op_actual_hours': records.op_hours_actual,
                'planned_cost': None,
                'actual_cost': None,
            }

            if not check_record:
                print("creating new records for selected employee")

                record.employee_project_per_month.sudo().create(vals)
            else:
                print("records already created")
        return record
