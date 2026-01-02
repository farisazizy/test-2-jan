from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    title = fields.Char(string='Title', required=True)
    author_id = fields.Many2one('res.partner', string='Author')
    price = fields.Float(string='Price')
    
    category_id = fields.Many2one('library.category', string='Categories', required=True)

    @api.constrains('price')
    def _check_price_below_zero(self):
        for record in self:
            if record.price < 0:
                raise ValidationError("Price must be more than zero.")
            
class LibraryCategory(models.Model):
    _name = 'library.category'
    _description = 'Library Category'

    category_name = fields.Char(string='Category Name')
    description = fields.Text(string='Description')

