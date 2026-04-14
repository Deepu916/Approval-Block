# -*- coding: utf-8 -*-
from odoo import fields, models


class ApprovalBlock(models.Model):
    """Approval Block Model"""
    _name = 'approval.block'
    _description = 'Approval Block'


    name = fields.Char(required=True)
    min_amount = fields.Float(required=True)
    max_amount = fields.Float(required=True)
    approver_id = fields.Many2one('res.users', required=True)