# -*- coding: utf-8 -*-
from odoo import api, fields, models


class PurchaseOrderInherit(models.Model):
    """Purchase Order Inherit Model"""
    _inherit = 'purchase.order'


    approval_block_id = fields.Many2one('approval.block',
                                        string='Approval Block',
                                        readonly=True,
                                        compute='_compute_approval_block_id',
                                        )

    @api.depends('amount_total')
    def _compute_approval_block_id(self):
        """Compute approval block id"""
        block = self.env['approval.block'].search([('min_amount', '<', self.amount_total),
                                                           ('max_amount', '>=', self.amount_total)])

        self.approval_block_id = block
