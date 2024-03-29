from __future__ import unicode_literals
from frappe import _

def get_data():
    return[
        {
            "label": _("Selling"),
            "icon": "fa fa-tools",
            "items": [
				{
                   "type": "doctype",
                   "name": "Item",
                   "label": _("Item"),
                   "description": _("Item")
                },
                {
                   "type": "doctype",
                   "name": "Customer",
                   "label": _("Customer"),
                   "description": _("Customer")
                },
                {
                   "type": "doctype",
                   "name": "Quotation",
                   "label": _("Quotation"),
                   "description": _("Quotation")
                },
                {
                   "type": "doctype",
                   "name": "Sales Order",
                   "label": _("Sales Order"),
                   "description": _("Sales Order")
                },
                {
                   "type": "doctype",
                   "name": "Delivery Note",
                   "label": _("Delivery Note"),
                   "description": _("Delivery Note")
                },
                {
                   "type": "doctype",
                   "name": "Sales Invoice",
                   "label": _("Sales Invoice"),
                   "description": _("Sales Invoice")
                }
            ]
        },
        {
            "label": _("Paul Schenk AG"),
            "icon": "fa fa-tools",
            "items": [
                {
                   "type": "doctype",
                   "name": "Facility",
                   "label": _("Facility"),
                   "description": _("Facility")
                },
                {
                   "type": "page",
                   "name": "facility-overview",
                   "label": _("Facility Overview"),
                   "description": _("Facility Overview")
                },
                {
                   "type": "doctype",
                   "name": "Inspection",
                   "label": _("Inspection"),
                   "description": _("Inspection")
                }
            ]
        }
    ]
