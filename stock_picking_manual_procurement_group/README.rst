[![Build Status](https://travis-ci.org/zeroincombenze/stock-logistics-workflow.svg?branch=8.0)](https://travis-ci.org/zeroincombenze/stock-logistics-workflow)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/zeroincombenze/stock-logistics-workflow/badge.svg?branch=8.0)](https://coveralls.io/github/zeroincombenze/stock-logistics-workflow?branch=8.0)
[![codecov](https://codecov.io/gh/zeroincombenze/stock-logistics-workflow/branch/8.0/graph/badge.svg)](https://codecov.io/gh/zeroincombenze/stock-logistics-workflow/branch/8.0)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-8.svg)](https://github.com/OCA/stock-logistics-workflow/tree/8.0)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-8.svg)](http://wiki.zeroincombenze.org/en/Odoo/8.0/dev)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-8.svg)](http://wiki.zeroincombenze.org/en/Odoo/8.0/man/LO)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-8.svg)](http://erp8.zeroincombenze.it)






















































[![en](http://www.shs-av.com/wp-content/en_US.png)](http://wiki.zeroincombenze.org/it/Odoo/7.0/man)

.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

Picking List Manual Procurement Group Creation
==============================================

This module gives ability to create procurement group for
manually created picking list.

Example Use Case

A company has 2 warehouse: (1) Main Warehouse, and (2) Chicago Warehouse.
Chicago warehouse replenish its stock from Main Warehouse.

Replenish Routes:

#. **Chicago Stock location**  pull from **Transit Location** using **internal transfer**
#. **Transit location** pull from **Main Warehouse Stock** using **internal transfer**

On 01-Jan-2016 (WH-02/INT/0001):

Internal transfer manually created to replenish. Procurement method using **Apply procurement rule**.
Source location **Transit Location**. Destination location **Chicago Stock Location**

On 02-Jan-2016 (WH-02/INT/0002):

Second internal transfer manually created to replenish. Procurement method using **Apply procurement rule**.
Source location **Transit Location**. Destination location **Chicago Stock Location**

Without **Create Procurement Group** activated:

Odoo will create one internal transfer from **Main Warehouse Stock** to **Transit Location**.
This internal transfer will be contained all items from WH-02/INT/0001 and WH-02/INT/0002.

With **Create Procurement Group** activated:

Odoo will create internal transfer from **Main Warehouse Stock** to **Transit Location**
for each WH-02/INT/0001 and WH-02/INT/0002

Installation
------------





To install this module, you need to:

#.  Go to menu *Setting -> Modules -> Local Modules*
#.  Search For *Picking List Manual Procurement Group Creation*
#.  Install the module


Configuration
-------------




Usage
-----







=====

To create procurement group for manually created picking, you need to:

#. Create picking list manually
#. Activate *Create Procurement Group* option on *Other Info* tab
#. Confirm picking

A procurement group will be created with name equal to picking name

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/154/8.0

Known issues / Roadmap
----------------------




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





### Contributors





* Andhitia Rama <andhitia.r@gmail.com>

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
