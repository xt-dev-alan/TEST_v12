# -*- encoding: UTF-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2018-Today XETECHS, S.A.
#    (<https://xetechs.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################
from odoo import fields, models, api, _
#from odoo.addons.power_check_rural import numero_a_texto

class ProductTemplate(models.Model):
	_inherit = "product.template"
	tipo_gasto = fields.Selection([
		('compra', 'Compra/Venta'),
		('servicio', 'Servicios/Honorarios'),
		('combustibles', 'Combustibles/Lubricantes'),
		('importacion', 'Importaciones'),
		('exportacion', 'Exportaciones'), 
		('n/a', 'N/A')],'Tipo Gasto', required=False, default='compra', help="Tipo de gasto que se reflejara en el libro de Ventas/Compras del IVA")

ProductTemplate()