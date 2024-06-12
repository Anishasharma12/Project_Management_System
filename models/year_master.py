from odoo import api, fields, models
from datetime import datetime
from odoo.exceptions import ValidationError 

class YearMaster(models.Model):
    _name = 'year.master'
    _description = 'Year Master Table'
    _rec_name = 'year'

    year = fields.Integer(string="Year", required=True)
    order = fields.Integer(string='Order', required=True)
    default_flag = fields.Boolean(string='Default Flag', default=False)
    delete_flag = fields.Boolean(string='Delete Flag', default=False)
    

    # showing year between 1900 to current year + 5
    @api.constrains('year')
    def _check_year(self):
        current_year = datetime.now().year 
        for record in self:
              if record.year < 1000 or record.year > 9999:
                raise ValidationError("The year must be a 4-digit number.")
              elif record.year < 1900 or record.year > current_year + 5:
                   raise ValidationError(f"Please enter a valid year between 1900 and {current_year + 5}.")
            # if record.year < 1900 or record.year > current_year + 5:
            #     raise ValidationError(f"Please enter a valid year between 1900 and {current_year + 5}.")