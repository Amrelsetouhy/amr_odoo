# product_movements_pdf/models/stock_report_wizard.py
from odoo import models, fields, api

class StockReportWizard(models.TransientModel):
    _name = 'stock.report.wizard'
    _description = 'Stock Report Wizard'

    product_id = fields.Many2one('product.product', string='Product', required=True)
    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)

    def generate_report(self):
        self.ensure_one()
        return self.env.ref('product_movements_pdf.stock_report_action').report_action(self)