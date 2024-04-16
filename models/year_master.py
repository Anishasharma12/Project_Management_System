from odoo import api, fields, models
from datetime import datetime
from odoo.exceptions import ValidationError 

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

    
    # @api.constrains('year')
    # def _check_year(self):
    #     current_year = datetime.now().year
    #     for record in self:
    #           if record.year < 1000 or record.year > 9999:
    #             raise ValidationError("The year must be a 4-digit number.")
    #           elif record.year < 1900 or record.year > current_year + 5:
    #                raise ValidationError(f"Please enter a valid year between 1900 and {current_year + 5}.")
               
                  

            # if record.year < 1900 or record.year > current_year + 5:
            #     raise ValidationError(f"Please enter a valid year between 1900 and {current_year + 5}.")