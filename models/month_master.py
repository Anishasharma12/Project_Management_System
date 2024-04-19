from odoo import api, fields, models
import calendar


class MonthMaster(models.Model):
    _name = 'month.master'
    _description = 'Month Master Table'
    _rec_name = 'month' 


    @api.model
    def _get_months(self):
        # Using calendar to get month names
        # Here both the key and the display value are set to the month name
        month_list = [(calendar.month_name[i], calendar.month_name[i]) for i in range(1, 13)]
        return month_list

    month = fields.Selection(
        selection=_get_months,
        string='Month',
        required=True,
        index=True,
    )
    order = fields.Integer(string='Order', required=True)