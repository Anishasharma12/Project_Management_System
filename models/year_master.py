from odoo import api, fields, models

class YearMaster(models.Model):
    _name = 'year.master'
    _description = 'Year Master Table'
    _rec_name = 'year'  # Set the representative field to 'code'
    
    # Generate a list of years for selection
    def _get_years(self):
        year_list = [(str(num), str(num)) for num in range(1900, 2101)]  # Adjust the range as needed
        return year_list

    year = fields.Selection(
        selection=_get_years,
        string='Year',
        required=True,
        index=True,
        unique=True
    )
    
    order = fields.Integer(string='Order', required=True)
    default_flag = fields.Boolean(string='Default Flag', default=False)
    delete_flag = fields.Boolean(string='Delete Flag', default=False)
