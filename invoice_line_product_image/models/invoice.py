# -*- coding: utf-8 -*-
# Part of Browseinfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models,_

class AccountInvoiceLine(models.Model):
    _inherit = "account.invoice.line"

    image_small = fields.Binary(string="Image")

    @api.multi
    @api.onchange('product_id')
    def onchange_invoice_product_image(self):
    	for product in self:
    		product.image_small = product.product_id.image_small
        