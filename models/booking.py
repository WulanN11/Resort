from xml.dom import VALIDATION_ERR, ValidationErr
from odoo import api, fields, models


class booking(models.Model):
    _name = 'resort.booking'
    _description = 'New Description'

    bookingkamar_ids= fields.One2many(
        comodel_name='resort.bookingkamar', 
        inverse_name='kamar_id', 
        string='Booking Kamar')
    
    name = fields.Char(string='Kode Order', required=True)
    booking = fields.Datetime('Booking',default=fields.Datetime.now())
    checkin = fields.Date(string='Check In', default=fields.Date.today())
    pemesan = fields.Many2one(
        comodel_name='res.partner', 
        string='Pemesan', 
        domain=[('is_customer','=', True)],store=True)
        
    
    total = fields.Integer(compute='_compute_total', string='Total', store=True)
    
    @api.depends('bookingkamar_ids')
    def _compute_total(self):
        for record in self:
            a = sum(self.env['resort.bookingkamar'].search([('booking_id', '=', record.id)]).mapped('harga'))
            record.total = a
    checkout = fields.Boolean(string='Sudah Check Out', default=False)
    
    def invoice(self):
        invoices = self.env['account.move'].create({
            'move_type': 'out_invoice',  
            'partner_id': self.pemesan,
            'invoice_date': self.booking,
            'date': fields.Datetime.now(),
            'invoice_line_ids': [(0, 0, {
                'product_id': 0,
                'name' :'xxx' ,
                'quantity': 1,
                'name': 'product test 1',
                'discount': 0,
                'price_unit': self.total,
                'price_subtotal': self.total,
            })]            
        })
        self.checkin=True
        return invoices  
    

class BookingKamar(models.Model):
    _name = 'resort.bookingkamar'
    _description = 'New Description'
    
    booking_id = fields.Many2one(comodel_name='resort.jenis_kamar', string='Booking Kamar')
    kamar_id = fields.Many2one(
        comodel_name='resort.jenis_kamar', 
        string='Kamar',
        domain=[('stok','>','100')])
    
    name = fields.Char(string='Name')
    harga_satuan = fields.Integer(compute='_compute_harga_satuan', string='harga_satuan')
    
    @api.depends('kamar_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.kamar_id.harga
    
    qty = fields.Integer(string='Quantity')
    
    @api.constrains('qty')
    def _check_stok(self):
        for record in self:
            tipe = self.env['resort.jenis_kamar'].search([('stok', '<',record.qty),('id', '=',record.id)])
            if tipe:
                raise ValidationErr("Stok kamar yang dipilih tidak cukup")
    
    harga = fields.Integer(compute='_compute_harga', string='harga')
    
    @api.depends('harga_satuan','qty')
    def _compute_harga(self):
        for record in self:
               record.harga = record.harga_satuan * record.qty
               
    
    @api.model
    def create(self,vals):
        record = super(BookingKamar, self).create(vals) 
        if record.qty:
            self.env['resort.jenis_kamar'].search([('id','=',record.kamar_id.id)]).write({'stok':record.kamar_id.stok-record.qty})
            return record