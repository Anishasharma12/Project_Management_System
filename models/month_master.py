from odoo import api, fields, models
import calendar


class MonthMaster(models.Model):
    _name = 'month.master'
    _description = 'Month Master Table'
    _rec_name = 'month' 


    id = fields.Integer("id")

    # this _get_months function is to get month names in numbers like 01, 02, 03 
    @api.model
    def _get_months(self):
        # Define the custom order for the months
        months_order = ['04', '05', '06', '07', '08', '09', '10', '11', '12', '01', '02', '03']
        month_list = [(month, month) for month in months_order]
        return month_list
    

    
    month = fields.Selection(
        selection=_get_months,
        string='Month',
        required=True,
        index=True,
        unique=True
    )
 
    order = fields.Integer(string='Order', required=True)

    _sql_constraints = [
        ('month_unique', 'UNIQUE(month)', "The month must be unique across all ,onth record"),
    ]
