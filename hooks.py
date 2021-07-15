# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "volunteers_system"
app_title = "Volunteers System"
app_publisher = "mohammad jasim hijji"
app_description = "Through this procedure the representative can identify the data of the volunteers in the system."
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "mohjas20121997@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/volunteers_system/css/volunteers_system.css"
# app_include_js = "/assets/volunteers_system/js/volunteers_system.js"

# include js, css files in header of web template
# web_include_css = "/assets/volunteers_system/css/volunteers_system.css"
# web_include_js = "/assets/volunteers_system/js/volunteers_system.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "volunteers_system.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "volunteers_system.install.before_install"
# after_install = "volunteers_system.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "volunteers_system.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"volunteers_system.tasks.all"
# 	],
# 	"daily": [
# 		"volunteers_system.tasks.daily"
# 	],
# 	"hourly": [
# 		"volunteers_system.tasks.hourly"
# 	],
# 	"weekly": [
# 		"volunteers_system.tasks.weekly"
# 	]
# 	"monthly": [
# 		"volunteers_system.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "volunteers_system.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "volunteers_system.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "volunteers_system.task.get_dashboard_data"
# }

