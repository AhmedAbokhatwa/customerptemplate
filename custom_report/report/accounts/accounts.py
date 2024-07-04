# Copyright (c) 2024, Ahmed Reda and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
	# columns, data = [], []
	columns =[
	_("parent_account") + "::200",
	_("account_name") + "::200"
	]


	parent_account = filters.get("parent_account")
	account_name = filters.get("account_name")

	sql =""" 
			SELECT 
				`tabAccount`.`parent_account`,
				`tabAccount`.`account_name`
			FROM `tabAccount`
			WHERE 
				(%(parent_account)s IS NULL OR `tabAccount`.`parent_account` Like %(parent_account)s)
				AND (%(account_name)s IS NULL OR `tabAccount`.`account_name` Like %(account_name)s)
			

	
	"""
	mydata= frappe.db.sql(sql,{
							"parent_account": f"%{parent_account}%" if parent_account else None,
							"account_name": f"%{account_name}%" if account_name else None,
							'indent': 0, 
							'has_value': True,
								},as_dict=True)
	return columns, mydata





