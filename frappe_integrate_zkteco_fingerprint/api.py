import frappe
from werkzeug.wrappers import Response

# ----------------------------
# Core functions
# ----------------------------

@frappe.whitelist(allow_guest=True)
def iclock_getrequest():
    """
    Original function — returns the command for the K50 device.
    """
    frappe.logger().info("iclock_getrequest called")
    frappe.log_error("iclock_getrequest called")
    # Return plain text directly
    return Response("DATA QUERY USERINFO\n", mimetype="text/plain")


@frappe.whitelist(allow_guest=True)
def iclock_cdata():
    """
    Original function — handles POSTed attendance logs from K50.
    """
    frappe.log_error("iclock_cdata called")
    data = frappe.request.data.decode("utf-8", errors="ignore").strip()
    frappe.log_error(f"iclock_cdata data: {data}")
    table = frappe.request.args.get("table")
    frappe.log_error(f"iclock_cdata table: {table}")

    if table and table.upper() == "ATTLOG":
        lines = data.split("\n")
        for line in lines:
            fields = line.strip().split("\t")
            if len(fields) >= 2:
                user_id, timestamp = fields[0], fields[1]
                frappe.log_error(f"User {user_id} at {timestamp}")

    return Response("OK", mimetype="text/plain")

