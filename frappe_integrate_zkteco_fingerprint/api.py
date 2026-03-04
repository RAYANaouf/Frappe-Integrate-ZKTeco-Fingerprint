import frappe
from werkzeug.wrappers import Response




@frappe.whitelist(allow_guest=True)
def iclock_getrequest():
    # Return plain text to avoid ERPNext JSON handling
    return Response("DATA QUERY USERINFO\n", mimetype="text/plain")




@frappe.whitelist(allow_guest=True)
def iclock_cdata():
    data = frappe.request.data.decode("utf-8", errors="ignore").strip()
    table = frappe.request.args.get("table")
    
    if table and table.upper() == "ATTLOG":
        lines = data.split("\n")
        for line in lines:
            fields = line.strip().split("\t")
            if len(fields) >= 2:
                user_id, timestamp = fields[0], fields[1]
                frappe.logger().info(f"User {user_id} at {timestamp}")

    # Return plain text
    return Response("OK", mimetype="text/plain")