from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    title = fields.Char(string='Title')
    author_id = fields.Many2one('res.partner', string='Author')
    price = fields.Float(string='Price')

    @api.constrains('price')
    def _check_price_below_zero(self):
        for record in self:
            if record.price < 0:
                raise ValidationError("Price must be more than zero.")
