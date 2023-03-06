# -*- coding: utf-8 -*-
# License, author and contributors information in:
# __openerp__.py file at the root folder of this module.

from openerp import api, models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    custom_list_line_ids = fields.One2many(
        comodel_name='custom.list.line',
        inverse_name='product_tmpl_id',
        string='Custom list lines'
    )
