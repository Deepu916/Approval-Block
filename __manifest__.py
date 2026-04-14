# -*- coding: utf-8 -*-
{
    'name': 'Approval Block',
    'version': '19.0.1.0.0',
    'application': True,
    'summary': 'Approval Block',
    'data': [
        'security/ir.model.access.csv',
        'data/approval_data.xml',
        'views/purchase_order_inherit_views.xml',
        'views/approval_block_views.xml',
        'views/approval_block_model_menus.xml',
    ],
    'depends': ['purchase'],
}
