# -*- coding: utf-8 -*-
# © 2016 - Eficent http://www.eficent.com/
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from openerp.tests.common import TransactionCase
from openerp.exceptions import Warning as UserWarning


class TestHrPayslipChangeState(TransactionCase):
    def setUp(self):
        result = super(TestHrPayslipChangeState, self).setUp()
        self.payslip_model = self.env['hr.payslip']
        self.contract_model = self.env['hr.contract']
        self.tested_model = self.env['hr.payslip.change.state']
        return result

    def test_change_state(self):
        payslip_model = self.payslip_model
        tested_model = self.tested_model
        contract = self.contract_model.create({'employee_id': 1,
                                               'name': 'demo',
                                               'wage': 10000,
                                               'struct_id': 1})

        payslip = payslip_model.create({'employee_id': 1,
                                        'name': 'test_payslip',
                                        'contract_id': contract.id,
                                        'struct_id': 1})

        context = {'active_ids': [payslip.id]}
        action = tested_model.with_context(context).create({'state': 'verify'})

        # By default a payslip is on draft state
        action.change_state_confirm()

        # trying to set it to wrong states
        with self.assertRaises(UserWarning):
            action.write({'state': 'draft'})
            action.change_state_confirm()

        # Now the payslip should be computed but in state draft
        self.assertEqual(payslip.state, 'draft')
        self.assertNotEqual(payslip.number, None)
        action.write({'state': 'done'})
        action.change_state_confirm()

        # Now the payslip should be confirmed
        self.assertEqual(payslip.state, 'done')

        # trying to set it to wrong states
        with self.assertRaises(UserWarning):
            action.write({'state': 'draft'})
            action.change_state_confirm()
        with self.assertRaises(UserWarning):
            action.write({'state': 'verify'})
            action.change_state_confirm()
        with self.assertRaises(UserWarning):
            action.write({'state': 'done'})
            action.change_state_confirm()

        action.write({'state': 'cancel'})
        action.change_state_confirm()

        # Now the payslip should be canceled
        self.assertEqual(payslip.state, 'cancel')

        # trying to set it to wrong states
        with self.assertRaises(UserWarning):
            action.write({'state': 'done'})
            action.change_state_confirm()
        with self.assertRaises(UserWarning):
            action.write({'state': 'verify'})
            action.change_state_confirm()
        with self.assertRaises(UserWarning):
            action.write({'state': 'cancel'})
            action.change_state_confirm()

        action.write({'state': 'draft'})
        action.change_state_confirm()
        # again, it shoud be draft. Also checking if wrong changes happened
        self.assertEqual(payslip.state, 'draft')
