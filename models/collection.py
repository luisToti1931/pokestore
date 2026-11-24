from odoo import models, fields

class PokestoreCollection(models.Model):
    _name = "pokestore.collection"
    _description = "Coleccion de figuras"
    _order = "name"

    name = fields.Char(string = "Nombre", required = True)
    pokemon = fields.Char(string = "Pokémon", required = False)
    price = fields.Float(string = "Precio", required = False)
    stock = fields.Integer(string = "Stock", default = 0)
    generation = fields.Integer(string="Generación")
    release_date = fields.Date(string="Fecha de lanzamiento")
    active = fields.Boolean(default = True)

    figure_ids = fields.One2many(
        "pokestore.figure", "collection_id", string="Figuras"
    )