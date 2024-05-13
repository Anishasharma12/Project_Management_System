from odoo import api, fields, models
import calendar


class ProjectsPerMonth(models.Model):
    _name = 'project_list_per_month'
    _description = 'project per month Master Table'
   #  _inherit = 'project_list_per_month'  # Assuming your model inherits from 'project.list.per.month'
    
 # Assuming the project.master has fields 'name' and 'code'
    id = fields.Integer("id")
   #  name = fields.Char("name", compute = '_compute_month')
    employee_relation = fields.Many2one('wb.projectemployeemaster', ondelete="set null", string="employee_relation") 
    # month_id = fields.Many2one('month.master', string='Month id')
    project_code = fields.Integer(related='employee_relation.project_code.code', string='code')
    month = fields.Many2one(
        'month.master',
        string="Month",
        help="Select month",
    )
    op_planned_hours = fields.Integer(string='Unit Price')
    op_actual_hours = fields.Integer(string='op actual hours')
    planned_cost = fields.Float(string='planned cost')
    actual_cost = fields.Float(string='actual cost')

    # employee_project_per_month = fields.One2many('project_list_per_month', 'employee_relation', string="project employee assigned to per month")



    def create(self, vals):
        record = super().create(vals)

        record = self._create_project_list_per_month(record, vals)

        return record

    def write(self, vals):
        res = super().write(vals)

        for record in self:
            search_created_record = self.env.search(
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



# this _compute_actual_hours is for function of planned hours
   #  @api.depends('id')  # Method depends on these fields
   #  def _compute_month(self):
   #      for record in self:
   #          record.name = 'summery'   
    # @api.model
    # def _auto_fill_month(self):
    #     # Get records to update
    #     records = self.search([])
    #     for record in records:
    #         # Assuming 'month_id' is the field linking to month.master
    #         month_data = self.env['month.master'].browse(record.id)
    #         if month_data:
    #             record.month = month_data.month  # Set month name from month.master
    #     return records
   

