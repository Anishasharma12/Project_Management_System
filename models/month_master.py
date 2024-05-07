from odoo import api, fields, models
import calendar


class MonthMaster(models.Model):
    _name = 'month.master'
    _description = 'Month Master Table'
    _rec_name = 'month' 


    id = fields.Integer("id")
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