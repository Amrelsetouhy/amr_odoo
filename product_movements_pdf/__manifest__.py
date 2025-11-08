{
    'name': 'Stock Report Module',
    'version': '1.0',
    'summary': 'Generate stock reports based on product and date range',
    'description': 'This module allows users to generate stock reports by selecting a product and a date range.',
    'author': 'Your Name',
    'website': 'https://yourwebsite.com',
    'category': 'Inventory',
    'depends': ['stock', 'product'],  # Dependencies on Odoo modules
    'data': [
        'views/stock_report_wizard_views.xml',  # Wizard view
        'reports/stock_report_template.xml',   # Report template
        'views/stock_report_action.xml',    # Report action
        'views/stock_move_line_view.xml', # move line
    ],
    'installable': True,
    'application': True,
}