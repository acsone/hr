import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo8-addons-oca-hr",
    description="Meta package for oca-hr Odoo addons",
    version=version,
    install_requires=[
        'odoo8-addon-hr_contract_default_trial_length',
        'odoo8-addon-hr_contract_hourly_rate',
        'odoo8-addon-hr_contract_multi_jobs',
        'odoo8-addon-hr_contract_reference',
        'odoo8-addon-hr_department_sequence',
        'odoo8-addon-hr_emergency_contact',
        'odoo8-addon-hr_employee_age',
        'odoo8-addon-hr_employee_benefit',
        'odoo8-addon-hr_employee_data_from_work_address',
        'odoo8-addon-hr_employee_firstname',
        'odoo8-addon-hr_employee_gravatar',
        'odoo8-addon-hr_employee_id',
        'odoo8-addon-hr_employee_identification',
        'odoo8-addon-hr_employee_legacy_id',
        'odoo8-addon-hr_employee_no_welcome',
        'odoo8-addon-hr_employee_phone_extension',
        'odoo8-addon-hr_employee_reference',
        'odoo8-addon-hr_expense_account_period',
        'odoo8-addon-hr_expense_analytic_default',
        'odoo8-addon-hr_expense_analytic_plans',
        'odoo8-addon-hr_expense_invoice',
        'odoo8-addon-hr_expense_move_date',
        'odoo8-addon-hr_expense_product_policy',
        'odoo8-addon-hr_expense_sequence',
        'odoo8-addon-hr_experience',
        'odoo8-addon-hr_family',
        'odoo8-addon-hr_holidays_compute_days',
        'odoo8-addon-hr_holidays_legal_leave',
        'odoo8-addon-hr_holidays_validity_date',
        'odoo8-addon-hr_job_categories',
        'odoo8-addon-hr_language',
        'odoo8-addon-hr_payroll_cancel',
        'odoo8-addon-hr_payroll_email_slip',
        'odoo8-addon-hr_payslip_change_state',
        'odoo8-addon-hr_payslip_input_policy',
        'odoo8-addon-hr_payslip_move_date',
        'odoo8-addon-hr_public_holidays',
        'odoo8-addon-hr_recruitment_partner',
        'odoo8-addon-hr_salary_rule_reference',
        'odoo8-addon-hr_security',
        'odoo8-addon-hr_skill',
        'odoo8-addon-hr_webcam',
        'odoo8-addon-hr_worked_days_from_timesheet',
        'odoo8-addon-resource_calendar_rrule',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
