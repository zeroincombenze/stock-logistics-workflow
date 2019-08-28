# -*- coding: utf-8 -*-
#    Author: Francesco Apruzzese
#    Copyright 2015    Apulia Software srl
#    Copyright 2015-18 Lorenzo Battistini - Agile Business Group
#    Copyright 2016    Alessio Gerace - Agile Business Group
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Stock Picking Package Preparation Line',
    'version': '10.0.1.0.4',
    'category': 'Warehouse Management',
    'author': 'Odoo Community Association (OCA), SHS-AV s.r.l., other subjects',
    'website': 'https://www.zeroincombenze.it/servizi-le-imprese/software-gestionale/',
    'license': 'AGPL-3',
    'depends': [
        'stock',
        'product',
        'stock_picking_package_preparation',
    ],
    'data': [
        'views/ir_config_view.xml',
        'views/stock_picking_package_preparation_line.xml',
        'security/ir.model.access.csv',
        'security/package_preparation_line_security.xml',
    ],
    'installable': True,
    'maintainer': 'Antonio Maria Vigliotti',
    'auto_install': False,
}
