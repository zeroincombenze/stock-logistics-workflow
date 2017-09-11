[![Build Status](https://travis-ci.org/zeroincombenze/stock-logistics-workflow.svg?branch=10.0)](https://travis-ci.org/zeroincombenze/stock-logistics-workflow)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/zeroincombenze/stock-logistics-workflow/badge.svg?branch=10.0)](https://coveralls.io/github/zeroincombenze/stock-logistics-workflow?branch=10.0)
[![codecov](https://codecov.io/gh/zeroincombenze/stock-logistics-workflow/branch/10.0/graph/badge.svg)](https://codecov.io/gh/zeroincombenze/stock-logistics-workflow/branch/10.0)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-10.svg)](https://github.com/OCA/stock-logistics-workflow/tree/10.0)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-10.svg)](http://wiki.zeroincombenze.org/en/Odoo/10.0/dev)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-10.svg)](http://wiki.zeroincombenze.org/en/Odoo/10.0/man/LO)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-10.svg)](http://erp10.zeroincombenze.it)


[![en](https://github.com/zeroincombenze/grymb/blob/master/flags/en_US.png)](https://www.facebook.com/groups/openerp.italia/)

.. image:: https://img.shields.io/badge/license-LGPL--3-blue.svg
================================================================
   :target: http://www.gnu.org/licenses/lgpl-3.0-standalone.html
   :alt: License: LGPL-3

Stock Delivery Internal

This module adds the concept of an internal delivery carrier to `delivery
.carrier`. When the `delivery_type` of a carrier is set to `Internal`, any
pickings shipped from that carrier will create `Requests For Pickup`. These
requests for pickup will in-turn create two pickings, one for the carrier to
pick up and one for the buyer to receive.

The Requests for pickup can also be configured to allow for Cash On
Delivery. Choosing this method will create two more pickings for the cash
pickup and subsequent delivery.



Installation
------------



Configuration
-------------



Usage
-----

-----

-----

=====

To use, simply add a Delivery Carrier with the Type set to Internal.

Known issues / Roadmap
----------------------




Bug Tracker
-----------




Bugs are tracked on `GitHub Issues
<https://github.com/OCA/stock-logistics-workflow/issues>`_. In case of
trouble, please check there if your issue has already been reported. If you
spotted it first, help us smash it by providing detailed and welcomed feedback.

Credits
-------




Images

* Odoo Community Association: `Icon <https://github.com/OCA/maintainer-tools/blob/master/template/module/static/description/icon.svg>`_.

[![Odoo Italia Associazione]]



### Contributors




* Ted Salmon <tsalmon@laslabs.com>

### Funders

### Maintainer






.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit https://odoo-community.org.

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
