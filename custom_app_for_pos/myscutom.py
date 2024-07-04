import frappe

@frappe.whitelist(allow_guest=True)
def update_membership(item_name, qty, rate , income_account):
    # Load the sales invoice document
    doc = frappe.get_doc("Sales Invoice","ACC-SINV-2024-00025")
        
        # Check if the document is submitted
        #if doc.docstatus == 1:
            #frappe.throw("Cannot modify items after {name}submission. Please unsubmit the invoice or create a new one.")
            # Append item to the Items table
    doc.append("items", {
        "item_name": item_name,
        "qty": qty,
        "rate": rate,
        # "description":description,
        # "stock_uom":stock_uom,
        # "uom":"Box",
        # "uom_conversion_factor": 1,  # Example: Assuming no conversion needed
        # "amount": 1000,  # Example: Calculating amount based on qty and rate
        # "rate_with_company_currency": 0,  # Example: Rate in company's currency
        # "amount_with_company_currency": 1000,  # Example: Amount in company's currency
        "income_account": income_account,  # Example: Specify the income account
    })

    # Save the document 
    doc.save()

    # Commit the changes
    frappe.db.commit()
    return "Success"



