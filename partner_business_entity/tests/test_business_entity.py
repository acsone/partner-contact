# -*- coding: utf-8 -*-
# Copyright 2016 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import TransactionCase
from psycopg2 import IntegrityError


class BusinessEntityTest(TransactionCase):

    def setUp(self):
        super(BusinessEntityTest, self).setUp()

        vals = {'name': 'Limited Corporation',
                'shortcut': 'Ltd.'}

        b_entity_obj = self.env['res.partner.business.entity']

        self.entity_ltd = b_entity_obj.create(vals)

    def test_00_duplicate(self):
        # Test Duplicate entity
        vals = {'name': 'Limited Corporation',
                'shortcut': 'Ltd.'}

        b_entity_obj = self.env['res.partner.business.entity']

        with self.assertRaises(IntegrityError):
            b_entity_obj.create(vals)
