# -*- coding: utf-8 -*-
# Author: Guewen Baconnier
# Copyright 2015 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Stock Picking Package Preparation',
    'version': '10.0.1.0.2',
    'category': 'Warehouse Management',
    'author': 'Odoo Community Association (OCA) and other subjects',
    'website': 'https://www.zeroincombenze.it/servizi-le-imprese/',
    'license': 'AGPL-3',
    'depends': ['stock'],
    'data': [
        'views/stock_picking_package_preparation_view.xml',
        'security/ir.model.access.csv',
        'security/package_preparation_security.xml',
    ],
    'installable': True,
    'maintainer': 'Antonio Maria Vigliotti',
    'auto_install': False,
}
