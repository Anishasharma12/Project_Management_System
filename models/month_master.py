from odoo import api, fields, models
import calendar


class MonthMaster(models.Model):
    _name = 'month.master'
    _description = 'Month Master Table'
    _rec_name = 'month' 


    @api.model
    def _get_months(self):
        # Using calendar to get month names
        month_list = [(str(i), calendar.month_name[i]) for i in range(1, 13)]
        return month_list

    month = fields.Selection(
        selection=_get_months,
        string='Month',
        required=True,
        index=True,
        unique=True
    )
    order = fields.Integer(string='Order', required=True)
