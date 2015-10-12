# -*- coding: utf-8 -*-
##############################################################################
#
#     This file is part of hr_contract_unique_calendar,
#     an Odoo module.
#
#     Copyright (c) 2015 ACSONE SA/NV (<http://acsone.eu>)
#
#     hr_contract_unique_calendar is free software:
#     you can redistribute it and/or modify it under the terms of the GNU
#     Affero General Public License as published by the Free Software
#     Foundation,either version 3 of the License, or (at your option) any
#     later version.
#
#     hr_contract_unique_calendar is distributed
#     in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
#     even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
#     PURPOSE.  See the GNU Affero General Public License for more details.
#
#     You should have received a copy of the GNU Affero General Public License
#     along with hr_contract_unique_calendar.
#     If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': "HR contract unique calendar",
    'summary': """
        Prevent to select a unique calendar on contract""",
    'author': 'ACSONE SA/NV,'
              'Odoo Community Association (OCA)',
    'website': "http://acsone.eu",
    'category': '',
    'version': '8.0.1.0.0',
    'license': 'AGPL-3',
    'depends': [
        'hr_contract',
    ],
    'data': [
        'views/resource_view.xml',
        'views/hr_contract_view.xml',
    ],
}
