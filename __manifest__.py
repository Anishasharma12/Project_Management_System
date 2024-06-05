{
    'name': 'CSI Project Management',
    'sequence': 1,
    'author': 'Creation Software and IT Solutions',
    'summary': 'Project Management for CSI Solutions',
    'application': True,
    'installable': True,
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/employee_master.xml',
        'views/project_master.xml',
        'views/employee_class_master.xml',
        'views/department_master.xml',
        'views/year_master.xml',
        'views/month_master.xml',
        "views/project_employee_assign_master.xml",
        "views/project_list_view.xml",
        "views/project_list_per_month.xml",
        "views/project_list_per_month_per_employee.xml",
        "views/employee_assign_per_month.xml",
        # "data/employee_assign_per_month_actions.xml",

    ],
        'assets': {
        'web.assets_backend': [
            # 'Project_Management/static/src/js/my_custom_script.js',
        ],
        'web.assets_qweb': [
            # 'Project_Management/static/src/xml/template.xml',
        ],
    },
}