from odoo import api, models, fields, _


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

    def open_action_followup_sales(self):
        self.ensure_one()
        return {
            'name': _("Overdue Payments for %s") % self.display_name,
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'views': [[self.env.ref('account_reports.customer_statements_form_view').id, 'form']],
            'res_model': 'res.partner',
            'res_id': self.id,
        }


    is_salesman = fields.Boolean(string="Es vendedor?", compute=_is_salesman, store=False)

