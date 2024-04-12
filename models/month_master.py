from odoo import api, fields, models

class MonthMaster(models.Model):
    _name = 'month.master'
    _description = 'Month Master Table'

    month = fields.Char(string='Month', required=True, index=True, unique=True)
    order = fields.Integer(string='Order', required=True)
