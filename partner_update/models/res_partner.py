# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class Partner(models.Model):
    _inherit = "res.partner"

    sales_of_partner_id = fields.Many2one('res.partner', string="Sales Of")

    @api.model
    def create(self, vals):
        res = super(Partner, self).create(vals)
        if res.parent_id:
            res.sales_of_partner_id = res.parent_id.id
        else:
            res.sales_of_partner_id = res.id
        return res

    @api.multi
    def write(self, vals):
        print ("\n\n vals.get('parent_id') : ",vals.get('parent_id'))
        if vals.get('parent_id'):
            vals.update({'sales_of_partner_id': vals['parent_id']})
        if vals.get('parent_id') == False:
            vals.update({'sales_of_partner_id': False})
        return super(Partner, self).write(vals)