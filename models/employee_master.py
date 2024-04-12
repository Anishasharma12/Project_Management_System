from odoo import api, fields, models

class DepartmentMaster(models.Model):
    _name = 'department.master'  # This is the technical name used in Many2one fields
    _description = 'Department Master'

    # Example field, adjust according to your needs
    name = fields.Char(string="Department Name", required=True)
    # Add other department-specific fields here

class EmployeeClassMaster(models.Model):
    _name = 'employee.class.master'  # This is the technical name used in Many2one fields
    _description = 'Employee Class Master'

    # Example field, adjust as needed
    name = fields.Char(string="Class Name", required=True)
    # Additional fields for the class



class EmployeeMaster(models.Model):
    _name = 'employee.master'
    _description = 'Employee Master Table'

    code = fields.Char(string='Code', required=True, index=True, unique=True)
    name = fields.Char(string='Name', required=True)
    department_code = fields.Many2one('department.master', string='Department Code')
    class_code = fields.Many2one('employee.class.master', string='Class Code')
    delete_flag = fields.Boolean(string='Delete Flag', default=False)
    description = fields.Text(string='Description')
