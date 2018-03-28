[![Build Status](https://travis-ci.org/zeroincombenze/stock-logistics-workflow.svg?branch=7.0)](https://travis-ci.org/zeroincombenze/stock-logistics-workflow)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/zeroincombenze/stock-logistics-workflow/badge.svg?branch=7.0)](https://coveralls.io/github/zeroincombenze/stock-logistics-workflow?branch=7.0)
[![codecov](https://codecov.io/gh/zeroincombenze/stock-logistics-workflow/branch/7.0/graph/badge.svg)](https://codecov.io/gh/zeroincombenze/stock-logistics-workflow/branch/7.0)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-7.svg)](https://github.com/OCA/stock-logistics-workflow/tree/7.0)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-7.svg)](http://wiki.zeroincombenze.org/en/Odoo/7.0/dev)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-7.svg)](http://wiki.zeroincombenze.org/en/Odoo/7.0/man/LO)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-7.svg)](http://erp7.zeroincombenze.it)


[![en](https://github.com/zeroincombenze/grymb/blob/master/flags/en_US.png)](https://www.facebook.com/groups/openerp.italia/)
================================================================================================
================================================================================================

Odoo Stock Logistic Workflow
============================

This project aims to deal with modules related to manage logistic flows. You'll find modules that:

 - Bring support for picking dispatch
 - Hold picking (adding a step in their workflow)
 - Ease the flow creation for the stock_location official module
 - Add filter to manage packing and deliveries

Please don't hesitate to suggest one of your module to this project. Also, you may want to have a look on those other projects here:

 - https://github.com/OCA/stock-logistics-tracking
 - https://github.com/OCA/stock-logistics-barcode
 - https://github.com/OCA/stock-logistics-warehouse

[//]: # (copyright)

----

**Odoo** is a trademark of [Odoo S.A.](https://www.odoo.com/) (formerly OpenERP, formerly TinyERP)

**OCA**, or the [Odoo Community Association](http://odoo-community.org/), is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

**zeroincombenze®** is a trademark of [SHS-AV s.r.l.](http://www.shs-av.com/)
which distributes and promotes **Odoo** ready-to-use on its own cloud infrastructure.
[Zeroincombenze® distribution](http://wiki.zeroincombenze.org/en/Odoo)
is mainly designed for Italian law and markeplace.
Everytime, every Odoo DB and customized code can be deployed on local server too.

[//]: # (end copyright)
[//]: # (addons)


Available addons
----------------
addon | version | OCA version | summary
--- | --- | --- | ---
[picking_dispatch](picking_dispatch/) | 1.2.4 | :repeat: | Picking dispatch
[picking_dispatch_wave](picking_dispatch_wave/) | 0.1 | :repeat: | Picking Dispatch Wave
[picking_line_description](picking_line_description/) | 1.0 | :repeat: | Picking line description
[product_customer_code_picking](product_customer_code_picking/) | 1.0 | :repeat: | Product Customer code for stock picking
[product_serial](product_serial/) | 1.0 | :repeat: | Enhance Serial Number management
[stock_cancel](stock_cancel/) | 1.2 | :repeat: | Stock Cancel
[stock_filter_none_zero_qty](stock_filter_none_zero_qty/) | 1.0 | :repeat: | Filter products in stock
[stock_inventory_retry_assign](stock_inventory_retry_assign/) | 1.0 | :repeat: | Check Availability after Inventories
[stock_move_backdating](stock_move_backdating/) | 1.0 | :repeat: | Stock Move Backdating
[stock_obsolete](stock_obsolete/) | 1.0 | :repeat: | Add product depreciation
[stock_picking_compute_delivery_date](stock_picking_compute_delivery_date/) | 1.0 | :repeat: | Stock Picking Compute Delivery Date
[stock_picking_deliver_uos](stock_picking_deliver_uos/) | 1.0 | :repeat: | Add fields uos and uos_quantity on Stock Partial Picking
[stock_picking_invoice_link](stock_picking_invoice_link/) | 0.2 | :repeat: | Adds link between pickings and generated invoices
[stock_picking_mass_assign](stock_picking_mass_assign/) | 0.2 | :repeat: | Delivery Orders Mass Assign
[stock_picking_priority](stock_picking_priority/) | 0.2 | :repeat: | Picking Priority
[stock_picking_show_returns](stock_picking_show_returns/) | 1.0 | :repeat: | Show returns on stock pickings
[stock_picking_update_date](stock_picking_update_date/) | 1.0 | :repeat: | Stock Picking Update Date
[stock_split_picking](stock_split_picking/) | version | :repeat: | Stock picking no confirm split


Unported addons
---------------
addon | version | OCA version | summary
--- | --- | --- | ---
[stock_location_flow_creator](__unported__/stock_location_flow_creator/) | 1.0 (unported) | :x: | Create configuration of stock location flow
[stock_move_on_hold](__unported__/stock_move_on_hold/) | 1.0 (unported) | :x: | Stock On Hold Status
[stock_sale_filters](__unported__/stock_sale_filters/) | 1.3 (unported) | :x: | SO related filters on stock.picking and sale.order

[//]: # (end addons)

[![chat with us](https://www.shs-av.com/wp-content/chat_with_us.gif)](https://tawk.to/85d4f6e06e68dd4e358797643fe5ee67540e408b)
