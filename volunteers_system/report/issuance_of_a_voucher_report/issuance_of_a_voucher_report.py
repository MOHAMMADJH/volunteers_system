# Copyright (c) 2013, mohammad jasim hijji and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt
# import frappe

def execute(filters=None):
	if not filters: filters = {}

	columns = get_columns()
	data = get_data(filters)

	return columns, data

def get_columns():
	return [
		_("Receipt number") + ":Select:120", 
		_("Date of receipt") + ":date:100",
		_("Statement")+ ":Long Text:100",
		_("Amount in Saudi Riyals") + ":Flot:100", 
		_("Partner name") + ":Select:120",
		_("Created by") + ":Data:120", 
		_("Status") + ":Select:60", 
		_("Project name") + ":Link/Project:100",
		_("Asset name") + ":Data:100"
	]

def get_data(filters):
	conditions = get_conditions(filters)
	return frappe.db.sql("""select naming_series, date_of_receipt, statement,
	amount_saudiriyals, partner_name, created_by,
	status, project_name ,asset_name 
	from `tabIssuance Of a Voucher` where  status = 'فعال' %s""" % conditions, as_list=1)

def get_conditions(filters):
	conditions = ""
	if filters.get("naming_series"): conditions += " and naming_series = '%s'" % \
		filters["naming_series"].replace("'", "\\'")

	if filters.get("date_of_receipt"): conditions += " and date_of_receipt = '%s'" % \
		filters["date_of_receipt"].replace("'", "\\'")

	if filters.get("statement"): conditions += " and statement = '%s'" % \
		filters["statement"].replace("'", "\\'")

	if filters.get("amount_saudiriyals"): conditions += " and amount_saudiriyals = '%s'" % \
		filters["amount_saudiriyals"].replace("'", "\\'")

	if filters.get("partner_name"): conditions += " and partner_name = '%s'" % \
		filters["partner_name"].replace("'", "\\'")

	if filters.get("created_by"): conditions += " and created_by = '%s'" % \
		filters["created_by"].replace("'", "\\'")

	if filters.get("status"): conditions += " and status = '%s'" % \
		filters["status"].replace("'", "\\'")

	if filters.get("project_name"): conditions += " and project_name = '%s'" % \
		filters["project_name"].replace("'", "\\'")

	if filters.get("asset_name"): conditions += " and asset_name = '%s'" % \
		filters["asset_name"].replace("'", "\\'")

	

	return conditions
