from odoo import api, fields, models

class MonthMaster(models.Model):
    _name = 'month.master'
    _description = 'Month Master Table'
    
    # Generate a list of months
    def _get_months(self):
        month_list = [(str(num), str(num)) for num in range(1, 13)]
        return month_list

    month = fields.Selection(
        selection=_get_months,
        string='Month',
        required=True,
        index=True,
        unique=True
    )

    order = fields.Integer(string='Order', required=True)