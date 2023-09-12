{
    "name": "Custom CSS",
    "summary": """
    Custom CSS classes
    """,
    "author": "Willians Salgado",
    "depends": ["base", "account", "sale", "sale_management"],
    "license": "AGPL-3",
    "data": [
        "views/sale_order_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "custom_css/static/src/scss/**/*"
        ]
    },
    "application": False
}