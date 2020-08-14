from odoo import api, models, fields, _
from datetime import datetime, timedelta
from odoo.tools.misc import formatLang, format_date
from odoo.tools import append_content_to_html, DEFAULT_SERVER_DATE_FORMAT
from odoo.exceptions import UserError


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
        ctx = {
            'is_salesman': 'self.is_salesman'
        }
        return {
            'name': _("Overdue Payments for %s") % self.display_name,
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'views': [[self.env.ref('account_reports.customer_statements_form_view').id, 'form']],
            'res_model': 'res.partner',
            'res_id': self.id,
            'context': ctx,
        }




    is_salesman = fields.Boolean(string="Es vendedor?", compute=_is_salesman, store=False)




class AccountFollowupReport(models.AbstractModel):
    _inherit = 'account.report'

    @api.multi
    def get_html(self, options, line_id=None, additional_context=None):
        """
        Override
        Compute and return the content in HTML of the followup for the partner_id in options
        """
        if additional_context is None:
            additional_context = {}
        partner = self.env['res.partner'].browse(options['partner_id'])
        additional_context['partner'] = partner
        additional_context['is_salesman'] = partner.is_salesman
        additional_context['lang'] = partner.lang or self.env.user.lang or 'en_US'
        additional_context['invoice_address_id'] = self.env['res.partner'].browse(
            partner.address_get(['invoice'])['invoice'])
        additional_context['today'] = fields.date.today().strftime(DEFAULT_SERVER_DATE_FORMAT)
        return super(AccountFollowupReport, self).get_html(options, line_id=line_id,
                                                           additional_context=additional_context)

