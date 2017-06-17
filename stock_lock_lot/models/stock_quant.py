# -*- coding: utf-8 -*-
# © 2015 Serv. Tec. Avanzados - Pedro M. Baeza (http://www.serviciosbaeza.com)
# © 2015 AvanzOsc (http://www.avanzosc.es)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api, exceptions, _


class StockQuant(models.Model):
    _inherit = 'stock.quant'

    locked = fields.Boolean(
        string='Blocked', related="lot_id.locked", default=False,
        store=True)

    @api.model
    def quants_get(self, location, product, qty, domain=None,
                   restrict_lot_id=False, restrict_partner_id=False):
        if domain is None:
            domain = []
        if not self.env.context.get('allow_not_blocked', False):
            domain += [('locked', '=', False)]
        return super(StockQuant, self).quants_get(
            location, product, qty, domain=domain,
            restrict_lot_id=restrict_lot_id,
            restrict_partner_id=restrict_partner_id)

    @api.model
    def quants_move(self, quants, move, location_to, location_from=False,
                    lot_id=False, owner_id=False, src_package_id=False,
                    dest_package_id=False):
        """Refuse to move a blocked lot if strict locking is demanded"""
        if lot_id and self.env['stock.config.settings']._get_parameter(
                'stock.lock.lot.strict', False):
            lot = self.env['stock.production.lot'].browse(lot_id)
            if lot.locked:
                raise exceptions.ValidationError(
                    _("The following lots/serial number is blocked and "
                      "cannot be moved:\n%s") % lot.name)
        super(StockQuant, self).quants_move(
            quants, move, location_to, location_from=location_from,
            lot_id=lot_id, owner_id=owner_id, src_package_id=src_package_id,
            dest_package_id=dest_package_id)

    @api.model
    def _quant_reconcile_negative(self, quant, move):
        return super(StockQuant, self.with_context(
            allow_not_blocked=move.location_dest_id.allow_locked)
            )._quant_reconcile_negative(quant, move)
