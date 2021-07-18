// Copyright (c) 2016, mohammad jasim hijji and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Issuance of a Receipt Report"] = {
	"filters": [{
		"fieldname":"naming_series",
		"label": __("Receipt number"),
		"fieldtype": "Select",
		"options": "",
		"default":""
	},
	{
		"fieldname":"date_of_receipt",
		"label": __("Date of receipt"),
		"fieldtype": "Date",
		"options": "",
		"default":""
	},
	{
		"fieldname":"statement",
		"label": __("Statement"),
		"fieldtype": "Data",
		"options": "",
		"default":""
	},
	{
		"fieldname":"amount_saudiriyals",
		"label": __("Amount in Saudi Riyals"),
		"fieldtype": "Data",
		"options": "",
		"default":""
	},
	{
		"fieldname":"partner_name",
		"label": __("Partner name"),
		"fieldtype": "Select",
		"options": "",
		"default":""
	},
	{
		"fieldname":"created_by",
		"label": __("Created by"),
		"fieldtype": "Data",
		"options": "",
		"default":""
	},
	{
		"fieldname":"status",
		"label": __("Status"),
		"fieldtype": "Select",
		"options": "",
		"default":""
	},
	{
		"fieldname":"donation_classification",
		"label": __("Donation classification"),
		"fieldtype": "Select",
		"options": "",
		"default":""
	},
	{
		"fieldname":"project_name1",
		"label": __("Project name"),
		"fieldtype": "Date",
		"options": "",
		"default":""
	},
	{
		"fieldname":"affiliate_name",
		"label": __("Affiliate name"),
		"fieldtype": "Data",
		"options": "",
		"default":""
	}
	]
};

