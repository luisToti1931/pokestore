{
    "name": "Pokestore",
    "version": "18.0.1.0.0",
    "summary": "Gestion de figuras coleccionables Pokémon",
    "category": "Sales",
    "license": "LGPL-3",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/pokestore_figure_views.xml",
        "views/pokestore_menus.xml",
        "data/pokestore_collection_data.xml",
    ],
    "demo": [
        "demo/pokestore_demo.xml",
    ],
    "application": True,
    "installable": True,
}
