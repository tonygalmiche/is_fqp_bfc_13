# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class EventRegistration(models.Model):
    _inherit = 'event.registration'

    is_societe     = fields.Char(string='Société')
    is_fonction    = fields.Char(string='Fonction')
    is_adherent    = fields.Selection([('Oui', 'Oui'),('Non', 'Non')], string='Adhérent')
    is_commentaire = fields.Char(string='Avez-vous des besoins spécifiques?')
