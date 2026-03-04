import frappe

def get_context(context):
    frappe.response["type"] = "text/plain"
    frappe.response["message"] = "DATA QUERY USERINFO\n"