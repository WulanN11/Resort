from odoo import api, fields, models


class jenis_kamar(models.Model):
    _name = 'resort.jenis_kamar'
    _description = 'Jenis Kamar'

    name = fields.Char(string='Nama')
    tipe = fields.Selection(string='Tipe Kamar', selection=[('standar room','Standar Room'), ('suite room','Suite Room'),  ('single room','Single Room')])
    stok = fields.Integer(string='Stok Kamar')
    harga = fields.Integer(string='Harga Sewa per Unit')
    img = fields.Binary(string='Image')
    pemesan = fields.Char(string='Pemesan')
    booking = fields.Char(string='Booking')
    checkin = fields.Char(string='Check In')
    checkout = fields.Char(string='Check Out')
    total = fields.Integer(string='Total')
    bookingkamar_ids = fields.Char(string='Booking Kamar')
    

    
    
    
    
    
    
    
    
    
