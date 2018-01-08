[![Build Status](https://travis-ci.org/zeroincombenze/stock-logistics-workflow.svg?branch=10.0)](https://travis-ci.org/zeroincombenze/stock-logistics-workflow)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/zeroincombenze/stock-logistics-workflow/badge.svg?branch=10.0)](https://coveralls.io/github/zeroincombenze/stock-logistics-workflow?branch=10.0)
[![codecov](https://codecov.io/gh/zeroincombenze/stock-logistics-workflow/branch/10.0/graph/badge.svg)](https://codecov.io/gh/zeroincombenze/stock-logistics-workflow/branch/10.0)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-10.svg)](https://github.com/OCA/stock-logistics-workflow/tree/10.0)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-10.svg)](http://wiki.zeroincombenze.org/en/Odoo/10.0/dev)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-10.svg)](http://wiki.zeroincombenze.org/en/Odoo/10.0/man/LO)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-10.svg)](http://erp10.zeroincombenze.it)




















[![en](http://www.shs-av.com/wp-content/en_US.png)](http://wiki.zeroincombenze.org/it/Odoo/7.0/man)

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

[//]: # (addons)


Available addons
----------------
addon | version | OCA version | summary
--- | --- | --- | ---
[product_expiry_simple](product_expiry_simple/) | 10.0.1.0.0 | :repeat: | Simpler and better alternative to the official product_expiry module
[stock_auto_move](stock_auto_move/) | 10.0.1.0.0 | :repeat: | Automatic Move Processing
[stock_delivery_internal](stock_delivery_internal/) | 10.0.1.0.0 | :repeat: | Adds an internal carrier to delivery options
[stock_disable_force_availability_button](stock_disable_force_availability_button/) | 10.0.1.0.0 | :repeat: | Disable force availability button
[stock_ownership_availability_rules](stock_ownership_availability_rules/) | 10.0.1.0.0 | :repeat: | Enforce ownership on stock availability
[stock_ownership_by_move](stock_ownership_by_move/) | 10.0.0.1.0 | :repeat: | Preserve Ownership of moves (not pickings) on reception.
[stock_picking_customer_ref](stock_picking_customer_ref/) | 10.0.1.0.0 | :repeat: | This module displays the sale reference/description in the pickings
[stock_picking_package_preparation](stock_picking_package_preparation/) | 10.0.1.0.1 | :repeat: | Stock Picking Package Preparation
[stock_picking_package_preparation_line](stock_picking_package_preparation_line/) | 10.0.1.0.1 | :repeat: | Stock Picking Package Preparation Line
[stock_picking_show_return](stock_picking_show_return/) | 10.0.1.0.0 | :repeat: | Show returns on stock pickings
[stock_split_picking](stock_split_picking/) | 10.0.1.0.0 | :repeat: | Split a picking in two not transferred pickings


Unported addons
---------------
addon | version | OCA version | summary
--- | --- | --- | ---
[picking_dispatch_wave](picking_dispatch_wave/) | 0.1 (unported) | :repeat: | Picking Dispatch Wave
[product_customer_code_picking](product_customer_code_picking/) | 1.0 (unported) | :repeat: | Product Customer code for stock picking
[product_serial](product_serial/) | 1.0 (unported) | :repeat: | Enhance Serial Number management
[stock_batch_picking](stock_batch_picking/) | 9.0.1.0.0 (unported) | :repeat: | Stock batch picking
[stock_cancel](stock_cancel/) | 1.2 (unported) | :repeat: | Stock Cancel
[stock_dropshipping_dual_invoice](stock_dropshipping_dual_invoice/) | 8.0.0.1.0 (unported) | :repeat: | Create both Supplier and Customer Invoices from a Dropshipping Delivery
[stock_inventory_retry_assign](stock_inventory_retry_assign/) | 1.0 (unported) | :repeat: | Check Availability after Inventories
[stock_location_flow_creator](stock_location_flow_creator/) | 1.0 (unported) | :repeat: | Create configuration of stock location flow
[stock_move_backdating](stock_move_backdating/) | 1.0 (unported) | :repeat: | Allows back-dating of stock moves
[stock_move_description](stock_move_description/) | 8.0.1.0.0 (unported) | :repeat: | Stock move description
[stock_move_on_hold](stock_move_on_hold/) | 1.0 (unported) | :repeat: | Stock On Hold Status
[stock_obsolete](stock_obsolete/) | 1.0 (unported) | :repeat: | Add product depreciation
[stock_picking_backorder_strategy](stock_picking_backorder_strategy/) | 8.0.0.1.0 (unported) | :repeat: | Picking backordering strategies
[stock_picking_compute_delivery_date](stock_picking_compute_delivery_date/) | 8.0.1.1.0 (unported) | :repeat: | Stock Picking Compute Delivery Date
[stock_picking_deliver_uos](stock_picking_deliver_uos/) | 8.0.1.0.0 (unported) | :repeat: | Adds fields uos and uos_quantity to Stock Transfer Details
[stock_picking_invoice_link](stock_picking_invoice_link/) | 8.0.1.0.0 (unported) | 10.0.1.0.0 | Adds link between pickings and generated invoices
[stock_picking_mass_assign](stock_picking_mass_assign/) | 9.0.1.0.0 (unported) | :repeat: | Delivery Orders Mass Assign
[stock_picking_priority](stock_picking_priority/) | 0.2 (unported) | :repeat: | Picking Priority
[stock_picking_reorder_lines](stock_picking_reorder_lines/) | 8.0.0.1.0 (unported) | :x: | Provide a new field on stock moves, allowing to manage the orders of moves in a picking.
[stock_sale_filters](stock_sale_filters/) | 1.3 (unported) | :repeat: | SO related filters on stock.picking and sale.order
[stock_transfer_split_multi](stock_transfer_split_multi/) | 8.0.1.0.0 (unported) | :repeat: | In the stock transfer wizard, you can split by multiple units

[//]: # (end addons)

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

[![chat with us](https://www.shs-av.com/wp-content/chat_with_us.gif)](https://tawk.to/85d4f6e06e68dd4e358797643fe5ee67540e408b)
