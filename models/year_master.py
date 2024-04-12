from odoo import api, fields, models

class YearMaster(models.Model):
    _name = 'year.master'
    _description = 'Year Master Table'

    year = fields.Char(string='Year', required=True, index=True, unique=True)
    order = fields.Integer(string='Order', required=True)
    default_flag = fields.Boolean(string='Default Flag', default=False)
    delete_flag = fields.Boolean(string='Delete Flag', default=False)
