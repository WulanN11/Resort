from odoo import api, fields,models


class Partner(models.Model):
    _inherit = 'res.partner'

    is_employee = fields.Boolean(string='Pegawai', default=False)
    is_customer = fields.Boolean(string='Customer', default=False)