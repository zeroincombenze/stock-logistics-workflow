
==============================================
|Zeroincombenze| stock-logistics-workflow 10.0
==============================================
|Build Status| |Codecov Status| |license gpl| |Try Me|


.. contents::


Overview / Panoramica
=====================

|en| This project aims to deal with modules related to manage logistic flows. You'll find modules that:

 - Bring support for picking dispatch
 - Hold picking (adding a step in their workflow)
 - Ease the flow creation for the stock_location official module
 - Add filter to manage packing and deliveries

Please don't hesitate to suggest one of your module to this project. Also, you may want to have a look on those other projects here:

 - https://github.com/OCA/stock-logistics-tracking
 - https://github.com/OCA/stock-logistics-barcode
 - https://github.com/OCA/stock-logistics-warehouse

|it| Moduli per la gestione del magazzino.

Avaiable Addons / Moduli disponibili
------------------------------------

+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| Name / Nome                          | Version    | OCA Ver.   | Description / Descrizione                                                        |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| mrp_stock_picking_restrict_cancel    | |no_check| | 10.0.11.0. | Restrict cancellation with MRP.                                                  |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| picking_dispatch_wave                | |halt|     | |halt|     | Picking Dispatch Wave                                                            |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| product_customer_code_picking        | |halt|     | |no_check| | Product Customer code for stock picking                                          |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| product_expiry_simple                | 10.0.1.0.0 | 10.0.1.0.1 | Simpler and better alternative to the official product_expiry module             |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| product_serial                       | |halt|     | |halt|     | Enhance Serial Number management                                                 |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| product_supplierinfo_for_customer_pi | |no_check| | 10.0.1.0.0 | This module makes the product customer code visible in the stock moves of a pick |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| purchase_stock_picking_restrict_canc | |no_check| | 10.0.11.0. | Restrict cancellation with Purchase.                                             |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_auto_move                      | 10.0.1.0.0 | |same|     | Automatic Move Processing                                                        |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_batch_picking                  | |halt|     | |halt|     | Stock batch picking                                                              |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_cancel                         | |halt|     | 10.0.0.1.0 | Stock Cancel                                                                     |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_cancel_delivery                | |no_check| | 10.0.0.1.0 |                                                                                  |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_change_price_at_date           | |no_check| | 10.0.1.0.0 |  This module allows to fill in a date in the standard wizard that changes produc |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_cost_method_last               | |no_check| | 10.0.1.0.0 | Add a new Costing Method 'Last Price'                                            |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_delivery_internal              | 10.0.1.0.0 | |same|     | Adds an internal carrier to delivery options                                     |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_delivery_note                  | |no_check| | 10.0.1.0.0 |  This module allows to fill in a delivery note that will be displayed on deliver |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_disable_force_availability_but | 10.0.1.0.0 | |same|     | Disable force availability button                                                |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_dropshipping_dual_invoice      | |halt|     | |halt|     | Create both Supplier and Customer Invoices from a Dropshipping Delivery          |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_exclude_to_remove_lot          | |no_check| | 10.0.1.0.0 |  This modules allows to exclude lots based on their removal date                 |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_inventory_retry_assign         | |halt|     | |halt|     | Check Availability after Inventories                                             |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_location_flow_creator          | |halt|     | |halt|     | Create configuration of stock location flow                                      |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_lot_scrap                      | |no_check| | 10.0.11.0. | This module adds a button in Production Lot/Serial Number view form to Scrap all |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_move_backdating                | |halt|     | 10.0.1.0.0 | Allows back-dating of stock moves                                                |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_move_description               | |halt|     | |halt|     | Stock move description                                                           |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_move_on_hold                   | |halt|     | |halt|     | Stock On Hold Status                                                             |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_move_quick_lot                 | |no_check| | 10.0.11.0. | Set lot name and end date directly on picking operations                         |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_no_negative                    | |no_check| | 10.0.1.0.1 | Disallow negative stock levels by default                                        |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_obsolete                       | |halt|     | |halt|     | Add product depreciation                                                         |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_ownership_availability_rules   | 10.0.1.0.0 | 10.0.1.0.2 | Enforce ownership on stock availability                                          |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_ownership_by_move              | 10.0.0.1.0 | |same|     | Preserve Ownership of moves (not pickings) on reception.                         |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_pack_operation_auto_fill       | |no_check| | 10.0.1.0.1 | Stock pack operation auto fill                                                   |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_picking_auto_create_lot        | |no_check| | 10.0.11.0. | Auto create lots for incoming pickings                                           |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_picking_back2draft             | |no_check| | 10.0.1.0.0 | Reopen cancelled pickings                                                        |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_picking_backorder_strategy     | |halt|     | 10.0.0.1.1 | Picking backordering strategies                                                  |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_picking_compute_delivery_date  | |halt|     | |halt|     | Stock Picking Compute Delivery Date                                              |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_picking_customer_ref           | 10.0.1.0.0 | 10.0.11.0. | This module displays the sale reference/description in the pickings              |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_picking_deactivate_immediate_t | |no_check| | 10.0.11.0. | Deactivates immediate transferssticking only to planned ones                     |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_picking_deliver_uos            | |halt|     | |halt|     | Adds fields uos and uos_quantity to Stock Transfer Details                       |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_picking_filter_lot             | |no_check| | 10.0.1.0.0 | In picking out lots' selection, filter lots based on their location              |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_picking_invoice_link           | |halt|     | 10.0.1.0.0 | Adds link between pickings and generated invoices                                |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_picking_line_sequence          | |no_check| | 10.0.1.1.0 | Manages the order of stock moves by displaying its sequence                      |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_picking_mass_action            | |no_check| | 10.0.1.0.0 | Stock Picking Mass Action                                                        |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_picking_mass_assign            | |halt|     | |halt|     | Delivery Orders Mass Assign                                                      |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_picking_operation_quick_change | |no_check| | 10.0.1.0.0 | Change location of all picking operations                                        |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_picking_package_preparation    | 10.0.1.0.1 | 10.0.11.0. | Stock Picking Package Preparation                                                |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_picking_package_preparation_li | 10.0.1.0.1 | 10.0.1.0.4 | Stock Picking Package Preparation Line                                           |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_picking_priority               | |halt|     | |halt|     | Picking Priority                                                                 |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_picking_purchase_propagate     | |no_check| | 10.0.11.0. | Propagate procurement group and quantity from purchase order                     |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_picking_reorder_lines          | |halt|     | |no_check| |  Provide a new field on stock moves, allowing to manage the orders of moves in a |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_picking_restrict_cancel_with_o | |no_check| | 10.0.11.0. | Restrict cancellation of dest moves according to origin.                         |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_picking_sale_order_link        | |no_check| | 10.0.11.0. | Link between picking and sale order                                              |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_picking_send_by_mail           | |no_check| | 10.0.11.0. | Send stock picking by email                                                      |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_picking_show_backorder         | |no_check| | 10.0.11.0. | Provides a new field on stock pickings, allowing to display the corresponding ba |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_picking_show_return            | 10.0.1.0.0 | 10.0.11.0. | Show returns on stock pickings                                                   |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_picking_transfer_lot_autoassig | |no_check| | 10.0.1.0.0 | Auto-assignation of lots on pickings                                             |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_picking_whole_scrap            | |no_check| | 10.0.11.0. | Create whole scrap from a picking for move lines                                 |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_sale_filters                   | |halt|     | |halt|     | SO related filters on stock.picking and sale.order                               |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_split_picking                  | 10.0.1.0.0 | 10.0.11.0. | Split a picking in two not transferred pickings                                  |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| stock_transfer_split_multi           | |halt|     | |halt|     | In the stock transfer wizard, you can split by multiple units                    |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+


OCA comparation / Confronto con OCA
-----------------------------------


+-----------------------------------------------------------------+-------------------+----------------+--------------------------------+
| Description / Descrizione                                       | Zeroincombenze    | OCA            | Notes / Note                   |
+-----------------------------------------------------------------+-------------------+----------------+--------------------------------+
| Coverage / Copertura test                                       |  |Codecov Status| | |OCA Codecov|  |                                |
+-----------------------------------------------------------------+-------------------+----------------+--------------------------------+


Getting started / Come iniziare
===============================

|Try Me|


Prerequisites / Prerequisiti
----------------------------


* python 2.7+ (best 2.7.5+)
* postgresql 9.2+ (best 9.5)


Installation / Installazione
----------------------------

+---------------------------------+------------------------------------------+
| |en|                            | |it|                                     |
+---------------------------------+------------------------------------------+
| These instruction are just an   | Istruzioni di esempio valide solo per    |
| example to remember what        | distribuzioni Linux CentOS 7, Ubuntu 14+ |
| you have to do on Linux.        | e Debian 8+                              |
|                                 |                                          |
| Installation is built with:     | L'installazione è costruita con:         |
+---------------------------------+------------------------------------------+
| `Zeroincombenze Tools <https://github.com/zeroincombenze/tools>`__         |
+---------------------------------+------------------------------------------+
| Suggested deployment is:        | Posizione suggerita per l'installazione: |
+---------------------------------+------------------------------------------+
| /opt/odoo/10.0/stock-logistics-workflow/                                   |
+----------------------------------------------------------------------------+

::

    cd $HOME
    git clone https://github.com/zeroincombenze/tools.git
    cd ./tools
    ./install_tools.sh -p
    export PATH=$HOME/dev:$PATH
    odoo_install_repository stock-logistics-workflow -b 10.0 -O zero
    for pkg in os0 z0lib; do
        pip install $pkg -U
    done
    sudo manage_odoo requirements -b 10.0 -vsy -o /opt/odoo/10.0


Upgrade / Aggiornamento
-----------------------

+---------------------------------+------------------------------------------+
| |en|                            | |it|                                     |
+---------------------------------+------------------------------------------+
| When you want upgrade and you   | Per aggiornare, se avete installato con  |
| installed using above           | le istruzioni di cui sopra:              |
| statements:                     |                                          |
+---------------------------------+------------------------------------------+

::

    odoo_install_repository stock-logistics-workflow -b 10.0 -O zero -U
    # Adjust following statements as per your system
    sudo systemctl restart odoo


Support / Supporto
------------------


|Zeroincombenze| This project is mainly maintained by the `SHS-AV s.r.l. <https://www.zeroincombenze.it/>`__



Get involved / Ci mettiamo in gioco
===================================

Bug reports are welcome! You can use the issue tracker to report bugs,
and/or submit pull requests on `GitHub Issues
<https://github.com/zeroincombenze/stock-logistics-workflow/issues>`_.

In case of trouble, please check there if your issue has already been reported.

Proposals for enhancement
-------------------------


|en| If you have a proposal to change on oh these modules, you may want to send an email to <cc@shs-av.com> for initial feedback.
An Enhancement Proposal may be submitted if your idea gains ground.

|it| Se hai proposte per migliorare uno dei moduli, puoi inviare una mail a <cc@shs-av.com> per un iniziale contatto.

Credits / Didascalie
====================

Copyright
---------

Odoo is a trademark of `Odoo S.A. <https://www.odoo.com/>`__ (formerly OpenERP)


----------------


|en| **zeroincombenze®** is a trademark of `SHS-AV s.r.l. <https://www.shs-av.com/>`__
which distributes and promotes ready-to-use **Odoo** on own cloud infrastructure.
`Zeroincombenze® distribution of Odoo <https://wiki.zeroincombenze.org/en/Odoo>`__
is mainly designed to cover Italian law and markeplace.

|it| **zeroincombenze®** è un marchio registrato da `SHS-AV s.r.l. <https://www.shs-av.com/>`__
che distribuisce e promuove **Odoo** pronto all'uso sulla propria infrastuttura.
La distribuzione `Zeroincombenze® <https://wiki.zeroincombenze.org/en/Odoo>`__ è progettata per le esigenze del mercato italiano.


|chat_with_us|


|


Last Update / Ultimo aggiornamento: 2019-08-28

.. |Maturity| image:: https://img.shields.io/badge/maturity-Alfa-red.png
    :target: https://odoo-community.org/page/development-status
    :alt: Alfa
.. |Build Status| image:: https://travis-ci.org/zeroincombenze/stock-logistics-workflow.svg?branch=10.0
    :target: https://travis-ci.org/zeroincombenze/stock-logistics-workflow
    :alt: github.com
.. |license gpl| image:: https://img.shields.io/badge/licence-LGPL--3-7379c3.svg
    :target: http://www.gnu.org/licenses/lgpl-3.0-standalone.html
    :alt: License: LGPL-3
.. |license opl| image:: https://img.shields.io/badge/licence-OPL-7379c3.svg
    :target: https://www.odoo.com/documentation/user/9.0/legal/licenses/licenses.html
    :alt: License: OPL
.. |Coverage Status| image:: https://coveralls.io/repos/github/zeroincombenze/stock-logistics-workflow/badge.svg?branch=10.0
    :target: https://coveralls.io/github/zeroincombenze/stock-logistics-workflow?branch=10.0
    :alt: Coverage
.. |Codecov Status| image:: https://codecov.io/gh/zeroincombenze/stock-logistics-workflow/branch/10.0/graph/badge.svg
    :target: https://codecov.io/gh/zeroincombenze/stock-logistics-workflow/branch/10.0
    :alt: Codecov
.. |Tech Doc| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-10.svg
    :target: https://wiki.zeroincombenze.org/en/Odoo/10.0/dev
    :alt: Technical Documentation
.. |Help| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-10.svg
    :target: https://wiki.zeroincombenze.org/it/Odoo/10.0/man
    :alt: Technical Documentation
.. |Try Me| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-10.svg
    :target: https://erp10.zeroincombenze.it
    :alt: Try Me
.. |OCA Codecov| image:: https://codecov.io/gh/OCA/stock-logistics-workflow/branch/10.0/graph/badge.svg
    :target: https://codecov.io/gh/OCA/stock-logistics-workflow/branch/10.0
    :alt: Codecov
.. |Odoo Italia Associazione| image:: https://www.odoo-italia.org/images/Immagini/Odoo%20Italia%20-%20126x56.png
   :target: https://odoo-italia.org
   :alt: Odoo Italia Associazione
.. |Zeroincombenze| image:: https://avatars0.githubusercontent.com/u/6972555?s=460&v=4
   :target: https://www.zeroincombenze.it/
   :alt: Zeroincombenze
.. |en| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/flags/en_US.png
   :target: https://www.facebook.com/Zeroincombenze-Software-gestionale-online-249494305219415/
.. |it| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/flags/it_IT.png
   :target: https://www.facebook.com/Zeroincombenze-Software-gestionale-online-249494305219415/
.. |check| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/check.png
.. |no_check| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/no_check.png
.. |menu| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/menu.png
.. |right_do| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/right_do.png
.. |exclamation| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/exclamation.png
.. |warning| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/warning.png
.. |same| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/same.png
.. |late| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/late.png
.. |halt| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/halt.png
.. |info| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/info.png
.. |xml_schema| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/iso/icons/xml-schema.png
   :target: https://github.com/zeroincombenze/grymb/blob/master/certificates/iso/scope/xml-schema.md
.. |DesktopTelematico| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/ade/icons/DesktopTelematico.png
   :target: https://github.com/zeroincombenze/grymb/blob/master/certificates/ade/scope/Desktoptelematico.md
.. |FatturaPA| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/ade/icons/fatturapa.png
   :target: https://github.com/zeroincombenze/grymb/blob/master/certificates/ade/scope/fatturapa.md
.. |chat_with_us| image:: https://www.shs-av.com/wp-content/chat_with_us.gif
   :target: https://tawk.to/85d4f6e06e68dd4e358797643fe5ee67540e408b
