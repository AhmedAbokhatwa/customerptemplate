import frappe

def get_context(context):
	context.name = frappe.get_doc("Customer","Gorge - 7")
	return context
