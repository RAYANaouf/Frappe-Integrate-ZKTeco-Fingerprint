import frappe

def get_context(context):
    data = frappe.request.data.decode("utf-8", errors="ignore")
    table = frappe.request.args.get("table")

    frappe.logger().info(f"K50 DATA RECEIVED: {data}")

    if table == "ATTLOG":
        lines = data.strip().split("\n")
        for line in lines:
            fields = line.split("\t")
            if len(fields) >= 2:
                user_id = fields[0]
                timestamp = fields[1]
                frappe.logger().info(f"User {user_id} at {timestamp}")

    frappe.response["type"] = "text/plain"
    frappe.response["message"] = "OK"