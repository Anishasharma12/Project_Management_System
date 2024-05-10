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
   

