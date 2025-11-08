from odoo import models, fields, api

class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    stock_after_movement = fields.Float(string="Stock After Movement", store=True)
    move_value = fields.Float(string="Move Value", store=True)
    stock_value = fields.Float(string="Stock Value", store=True)
    unit_cost = fields.Float(string="Unit Cost", store=True)
    partner_name = fields.Char(string="Partner", store=True)
    #from_server_action = fields.Boolean(string="From Server Action", default=False)
    operation_type = fields.Selection([
        ('incoming', 'Incoming'),
        ('outgoing', 'Outgoing'),
        ('internal', 'Internal Transfer')
    ], string="Operation Type", store=True)

