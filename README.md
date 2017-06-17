[![Build Status](https://travis-ci.org/zeroincombenze/stock-logistics-workflow.svg?branch=8.0)](https://travis-ci.org/zeroincombenze/stock-logistics-workflow)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/zeroincombenze/stock-logistics-workflow/badge.svg?branch=8.0)](https://coveralls.io/github/zeroincombenze/stock-logistics-workflow?branch=8.0)
[![codecov](https://codecov.io/gh/zeroincombenze/stock-logistics-workflow/branch/8.0/graph/badge.svg)](https://codecov.io/gh/zeroincombenze/stock-logistics-workflow/branch/8.0)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-8.svg)](https://github.com/OCA/stock-logistics-workflow/tree/8.0)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-8.svg)](http://wiki.zeroincombenze.org/en/Odoo/dev/8.0)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-8.svg)](http://wiki.zeroincombenze.org/en/Odoo/8.0/stock-)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-8.svg)](http://erp8.zeroincombenze.it)

Odoo Stock Logistic Workflow
===========================

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
addon | version | summary
--- | --- | ---
[mrp_lock_lot](mrp_lock_lot/) | 8.0.3.0.0 | MRP Lock Lot
[picking_dispatch](picking_dispatch/) | 8.0.1.2.3 | Picking dispatch
[procurement_jit_assign_move](procurement_jit_assign_move/) | 8.0.1.0.0 | Change the behavior of procurement_jit to assign stock moves
[product_unique_serial](product_unique_serial/) | 8.0.1.0.1 | Product Serial Unique Number
[sale_stock_auto_move](sale_stock_auto_move/) | 8.0.1.0.0 | Automatic Move Processing For Sale Delivery
[sale_stock_picking_back2draft](sale_stock_picking_back2draft/) | 8.0.1.0.0 | Pickings back to draft - Sale integration
[stock_auto_move](stock_auto_move/) | 8.0.1.0.0 | Automatic Move Processing
[stock_disable_force_availability_button](stock_disable_force_availability_button/) | 8.0.1.0.0 | Disable force availability button
[stock_dropshipping_dual_invoice](stock_dropshipping_dual_invoice/) | 8.0.0.1.0 | Create both Supplier and Customer Invoices from a Dropshipping Delivery
[stock_lock_lot](stock_lock_lot/) | 8.0.2.0.0 | Stock Lock Lot
[stock_lot_scrap](stock_lot_scrap/) | 8.0.1.0.0 | This module adds a button in Production Lot/Serial Number view form to Scrap all products contained.
[stock_move_backdating](stock_move_backdating/) | 8.0.1.0.0 | Stock Move Backdating
[stock_move_description](stock_move_description/) | 8.0.1.0.0 | Stock move description
[stock_no_negative](stock_no_negative/) | 8.0.1.0.1 | Stock Check No Negative
[stock_ownership_availability_rules](stock_ownership_availability_rules/) | 8.0.0.2.0 | Enforce ownership on stock availability
[stock_ownership_by_move](stock_ownership_by_move/) | 8.0.0.1.0 | Preserve Ownership of moves (not pickings) on reception.
[stock_picking_back2draft](stock_picking_back2draft/) | 8.0.1.0.0 | Reopen cancelled pickings
[stock_picking_backorder_strategy](stock_picking_backorder_strategy/) | 8.0.0.1.0 | Picking backordering strategies
[stock_picking_backorder_to_sale](stock_picking_backorder_to_sale/) | 8.0.1.0.0 | Create sale order from backorder an cancel backorder
[stock_picking_compute_delivery_date](stock_picking_compute_delivery_date/) | 8.0.1.1.0 | Stock Picking Compute Delivery Date
[stock_picking_deliver_uos](stock_picking_deliver_uos/) | 8.0.1.0.0 | Adds fields uos and uos_quantity to Stock Transfer Details
[stock_picking_invoice_link](stock_picking_invoice_link/) | 8.0.2.1.0 | Adds link between pickings and generated invoices
[stock_picking_manual_procurement_group](stock_picking_manual_procurement_group/) | 8.0.1.0.0 | Picking List Manual Procurement Group Creation
[stock_picking_mass_action](stock_picking_mass_action/) | 8.0.1.0.0 | Stock Picking Mass Action
[stock_picking_package_preparation](stock_picking_package_preparation/) | 8.0.1.0.0 | Stock Picking Package Preparation
[stock_picking_package_preparation_line](stock_picking_package_preparation_line/) | 8.0.1.0.0 | Stock Picking Package Preparation Line
[stock_picking_reorder_lines](stock_picking_reorder_lines/) | 8.0.0.1.0 | Provide a new field on stock moves, allowing to manage the orders of moves in a picking.
[stock_picking_show_return](stock_picking_show_return/) | 8.0.1.0.0 | Show returns on stock pickings
[stock_route_sales_team](stock_route_sales_team/) | 8.0.1.0.0 | Stock Route Sales Teams
[stock_scanner](stock_scanner/) | 8.0.1.0.0 | Allows managing barcode readers with simple scenarios
[stock_split_picking](stock_split_picking/) | 8.0.1.0.0 | Split a picking in two unconfirmed pickings
[stock_transfer_split_multi](stock_transfer_split_multi/) | 8.0.1.0.0 | In the stock transfer wizard, you can split by multiple units


Unported addons
---------------
addon | version | summary
--- | --- | ---
[picking_dispatch_wave](picking_dispatch_wave/) | 0.1 (unported) | Picking Dispatch Wave
[product_customer_code_picking](product_customer_code_picking/) | 1.0 (unported) | Product Customer code for stock picking
[product_serial](product_serial/) | 1.0 (unported) | Enhance Serial Number management
[stock_cancel](stock_cancel/) | 1.2 (unported) | Stock Cancel
[stock_inventory_retry_assign](stock_inventory_retry_assign/) | 1.0 (unported) | Check Availability after Inventories
[stock_location_flow_creator](stock_location_flow_creator/) | 1.0 (unported) | Create configuration of stock location flow
[stock_move_on_hold](stock_move_on_hold/) | 1.0 (unported) | Stock On Hold Status
[stock_obsolete](stock_obsolete/) | 1.0 (unported) | Add product depreciation
[stock_picking_priority](stock_picking_priority/) | 0.2 (unported) | Picking Priority
[stock_sale_filters](stock_sale_filters/) | 1.3 (unported) | SO related filters on stock.picking and sale.order

[//]: # (end addons)

Translation status
------------------

[![Transifex Status](https://www.transifex.com/projects/p/OCA-stock-logistics-workflow-8-0/chart/image_png)](https://www.transifex.com/projects/p/OCA-stock-logistics-workflow-8-0)

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
