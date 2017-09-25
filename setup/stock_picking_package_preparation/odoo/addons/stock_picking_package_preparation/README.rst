[![Build Status](https://travis-ci.org/zeroincombenze/addons.svg?branch=10.0)](https://travis-ci.org/zeroincombenze/addons)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/zeroincombenze/addons/badge.svg?branch=10.0)](https://coveralls.io/github/zeroincombenze/addons?branch=10.0)
[![codecov](https://codecov.io/gh/zeroincombenze/addons/branch/10.0/graph/badge.svg)](https://codecov.io/gh/zeroincombenze/addons/branch/10.0)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-10.svg)](https://github.com/OCA/addons/tree/10.0)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-10.svg)](http://wiki.zeroincombenze.org/en/Odoo/10.0/dev)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-10.svg)](http://wiki.zeroincombenze.org/en/Odoo/10.0/man/)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-10.svg)](http://erp10.zeroincombenze.it)


[![en](https://github.com/zeroincombenze/grymb/blob/master/flags/en_US.png)](https://www.facebook.com/groups/openerp.italia/)

   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
================================================================
   :alt: License: AGPL-3

Stock Picking Package Preparation

This module adds a new document in the Warehouse menu: **Package
Preparation**. It works on a selection of pickings and allows to add
them all in the same package, then to transfer all the pickings at once.

A possible use case is to put all the selected pickings on a pallet.

Installation
------------






 * This module depends only on the **stock** module.

Configuration
-------------






 * No special setup

Usage
-----

-----

-----

-----

-----

=====

To use this module, you need to:

 * Go to Warehouse > Package Preparation

From there, you can create a new preparation.
Choose a partner then the selection of pickings you want in the package.
You can choose a logistic unit or a packaging, they will be set on the
generated package.

When you click on **Put in pack**, it generates the pack, which is not
finalized yet (no quants), but you can verify the operations in the
**Operations** tab.
Eventually, when you click on **Done**, all the pickings will be
transfered and the package operations will be performed.

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/154/10.0

Known issues / Roadmap
----------------------






 * No printed document for the preparation


Bug Tracker
-----------






Bugs are tracked on `GitHub Issues
<https://github.com/OCA/stock-logistics-workflow/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smashing it by providing a detailed and welcomed feedback.


Credits
-------





Images

* Odoo Community Association: `Icon <https://github.com/OCA/maintainer-tools/blob/master/template/module/static/description/icon.svg>`_.

[![Odoo Italia Associazione]]





### Contributors






* Guewen Baconnier <guewen.baconnier@camptocamp.com>
* Lorenzo Battistini <lorenzo.battistini@agilebg.com>
* Alessio Gerace <alessio.gerace@agilebg.com>

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
