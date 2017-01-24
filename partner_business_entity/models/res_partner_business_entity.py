# -*- coding: utf-8 -*-
# Copyright 2017 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResPartnerBusinessEntity(models.Model):

    _name = 'res.partner.business.entity'
    _description = 'Partner business Entity'

    name = fields.Char(string='Title', required=True, translate=True)
    shortcut = fields.Char(string='Abbreviation', translate=True)

    _sql_constraints = [('name_uniq', 'unique (name)',
                         "Partner Business Entity already exists !")]
