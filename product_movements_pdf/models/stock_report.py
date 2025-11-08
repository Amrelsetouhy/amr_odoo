# product_movements_pdf/models/stock_report.py
from odoo import models, api

class StockReport(models.AbstractModel):
    _name = 'report.product_movements_pdf.stock_report_template'
    _description = 'Stock Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        wizard = self.env['stock.report.wizard'].browse(docids)
        product_id = wizard.product_id.id
        product_name = wizard.product_id.name  # Fetch the product's name from the product_id field
        start_date = wizard.start_date
        end_date = wizard.end_date

        query = """
select  sml.id,sml.reference,to_char(sml.date, 'DD/MM/YY') AS date,sml.qty_done,sml.move_value,sml.unit_cost,sml.partner_name,sl_src.name AS source_location,
    sl_dest.name AS dest_location,
sml.stock_after_movement,sml.stock_value
from public.stock_move_line sml
LEFT JOIN stock_location sl_src 
    ON sl_src.id = sml.location_id
LEFT JOIN stock_location sl_dest 
    ON sl_dest.id = sml.location_dest_id
WHERE sml.product_id = %s
AND sml.create_date BETWEEN %s AND %s
and sml.state ='done'
order by id
        """

        self.env.cr.execute(query, (product_id, start_date, end_date))
        results = self.env.cr.dictfetchall()

        return {
            'doc_ids': docids,
            'doc_model': 'stock.report.wizard',
            'data': data,
            'results': results,
            'product_name': product_name,  # Pass the product's name to the template
        }