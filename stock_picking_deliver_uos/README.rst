[![Build Status](https://travis-ci.org/zeroincombenze/stock-logistics-workflow.svg?branch=10.0)](https://travis-ci.org/zeroincombenze/stock-logistics-workflow)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/zeroincombenze/stock-logistics-workflow/badge.svg?branch=10.0)](https://coveralls.io/github/zeroincombenze/stock-logistics-workflow?branch=10.0)
[![codecov](https://codecov.io/gh/zeroincombenze/stock-logistics-workflow/branch/10.0/graph/badge.svg)](https://codecov.io/gh/zeroincombenze/stock-logistics-workflow/branch/10.0)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-10.svg)](https://github.com/OCA/stock-logistics-workflow/tree/10.0)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-10.svg)](http://wiki.zeroincombenze.org/en/Odoo/10.0/dev)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-10.svg)](http://wiki.zeroincombenze.org/en/Odoo/10.0/man/LO)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-10.svg)](http://erp10.zeroincombenze.it)




























[![en](http://www.shs-av.com/wp-content/en_US.png)](http://wiki.zeroincombenze.org/it/Odoo/7.0/man)

    :alt: License: AGPL-3

Stock Picking Deliver UOS
=========================

This module adds two fields, uos and uos quantity to Stock Transfer Details
wizard allowing the user to use the uos quantity (instead of the standard uom)
to specify the quantity to be delivered.

Note: the module handles only the case when one stock move leads to one
pack operation.

For example if I have to deliver 3 tables (uos qty=3 uos=pz) each one of 1,5 m²
(uom=m², uom qty=4,5), I can make a transfer specifying 2 pieces (the
system computes the internal uom qty:  3 m²)

Installation
------------





Configuration
-------------





Usage
-----







Known issues / Roadmap
----------------------





Bug Tracker
-----------






Bugs are tracked on `GitHub Issues <https://github.com/OCA/stock-logistics-workflow/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed feedback
`here <https://github.com/OCA/stock-logistics-workflow/issues/new?body=module:%20stock_picking_deliver_uos%0Aversion:%208.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Credits
-------











### Contributors






* Alex Comba <alex.comba@agilebg.com>
* Lorenzo Battistini <lorenzo.battistini@agilebg.com>

### Funders

### Maintainer










.. image:: http://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: http://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit http://odoo-community.org.

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

[//]: # (end addons)

[![chat with us](https://www.shs-av.com/wp-content/chat_with_us.gif)](https://tawk.to/85d4f6e06e68dd4e358797643fe5ee67540e408b)
