from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

@frappe.whitelist(allow_guest=True)
def getStock(item_code):
	stock = frappe.db.sql("""select item_code, warehouse, actual_qty from `tabBin`
                where item_code = %s and actual_qty != 0;""",(item_code),as_list = True)

	return stock[0][0] if stock else 0

@frappe.whitelist(allow_guest=True)
def getBuyingPrice(item_code):
	cost = frappe.db.sql("""select price_list_rate,buying_discount from `tabItem Price` where item_code = %s and buying = 1 
		order by valid_from desc limit 1;""",(item_code),as_list = True)

	return cost if cost else False
