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
    op_hours_planned=fields.Integer("OP hours Planned")
    op_hours_actual=fields.Integer("OP hours Actual")
