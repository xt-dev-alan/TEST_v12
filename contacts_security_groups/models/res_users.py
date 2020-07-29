from odoo import api, models, fields


class Users(models.Model):
    _name = 'res.users'
    _inherit = 'res.users'

    is_salesman = fields.Boolean(string="Es vendedor?")


class Partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    def _is_salesman(self):
        user = self.env['res.users'].browse(self._uid)
        self.is_salesman = user.is_salesman


    is_salesman = fields.Boolean(string="Es vendedor?", compute=_is_salesman, store=False)

