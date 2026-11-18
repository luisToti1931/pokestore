from odoo import models, fields

class PokestoreCollection(models.Model):
    _name = "pokestore.collection"
    _description = "Coleccion de figuras"
    _order = "name"

    name = fields.Char(string = "Nombre", required = True)
    pokemon = fields.Char(string = "Pokémon", required = True)
    price = fields.Float(string = "Precio", required = True)
    stock = fields.Integer(string = "Stock", default = 0)
    active = fields.Boolean(default = True)

    figure_ids = fields.One2many(
        "pokestore.figure", "collection_id", string="Figuras"
    )