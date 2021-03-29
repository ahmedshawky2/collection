# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo import exceptions
from odoo.exceptions import ValidationError
import json
import datetime
import string
import requests

import logging
_logger = logging.getLogger(__name__)


class lov (models.Model):
    _name = 'collection'


    account_id = fields.Char(string='Account Id',index=True)
    group = fields.Selection([ ('BKT4', 'BKT4'),('LEGAL', 'LEGAL') ,('CDRA', 'CDRA') ,('BG1DAGE125', 'BG1DAGE125') ,('LEGALEXP', 'LEGALEXP') ], string='group')
    mobile_no = fields.Char(string='Mobile No',index=True)
    name = fields.Char(string='Name',index=True)
    crn_civil_id = fields.Char(string='CRN/Civil Id',index=True)
    company_type = fields.Char(string='Company Type',index=True)
    bill_cycle_code = fields.Char(string='Bill Cycle Code',index=True)
    dealer_code = fields.Char(string='Dealer Code',index=True)
    account_manager = fields.Char(string='Account Manager',index=True)
    current_account_manager = fields.Char(string='Current Account Manager',index=True)
    class_of_defaulter = fields.Char(string='Class Of Defaulter',index=True)
    credit_class = fields.Char(string='Credit Class',index=True)
    os_amount = fields.Float(string='OS Amount',index=True)
    od_amount = fields.Float(string='OD Amount',index=True)
    write_off_amt = fields.Float(string='Write off Amt',index=True)
    bucket = fields.Char(string='Bucket',index=True)
    debt_age = fields.Integer(string='Debt Age',index=True)
    next_dunning_action = fields.Char(string='Next Dunning Action',index=True)
    next_dunning_action_date = fields.Char(string='Next Dunning Action Date',index=True)
    coll_strategy = fields.Char(string='Coll Strategy',index=True)
    collector_code = fields.Char(string='Collector Code',index=True)
    allocation_expiry_date = fields.Char(string='Allocation Expiry Date',index=True)
    workflow = fields.Char(string='WorkFlow',index=True)
    state = fields.Char(string='State',index=True)
    last_followup_action = fields.Char(string='Last Followup Action',index=True)
    last_followup_date = fields.Datetime(string='Last Followup Date',index=True)
    last_followup_feedback = fields.Char(string='Last Followup Feedback',index=True)
    last_follow_up_notes = fields.Char(string='Last Follow Up Notes',index=True)
    next_action = fields.Char(string='Next Action',index=True)
    next_action_date = fields.Char(string='Next Action Date',index=True)
    strategy_last_action = fields.Char(string='Strategy Last Action',index=True)
    action_due_date = fields.Char(string='Action Due Date',index=True)
    account_status = fields.Selection([ ('S', 'Suspended'),('D', 'Deactivated') ,('A', 'Active') ,('B', 'Bounded')  ], string='Account Status')
    allocation_id = fields.Char(string='Allocation ID',index=True)
    alternative_number = fields.Char(string='Alternative number',index=True)
    evening_time_contact_number = fields.Char(string='Evening Time Contact Number',index=True)
    day_time_contact_number = fields.Char(string='Day Time Contact Number',index=True)
    prepaid_number = fields.Char(string='Prepaid Number',index=True)
    contact_name = fields.Char(string='Contact Name',index=True)
    contact_number = fields.Char(string='Contact Number',index=True)
    contact_email_id = fields.Char(string='Contact Email ID',index=True)
    most_frequently_called_number = fields.Char(string='Most Frequently Called Number',index=True)
    register_email_id = fields.Char(string='Register EMail ID',index=True)
    bmc_contact_number = fields.Char(string='BMC Contact Number',index=True)
    activation_business_rule_type = fields.Char(string='Activation Business Rule Type',index=True)
    e_mail_id = fields.Char(string='E mail ID',index=True)
    blacklist_flag = fields.Boolean(string='Blacklist Flag',index=True)
    ptp_date = fields.Char(string='PTP Date',index=True)
    last_kept_ptp_date = fields.Char(string='Last Kept PTP date',index=True)
    last_kept_ptp_amount = fields.Char(string='Last Kept PTP Amount',index=True)
    total_customer_o_s_amt = fields.Char(string='Total Customer O/S Amt',index=True)
    total_customer_o_d_amt = fields.Char(string='Total Customer O/D Amt',index=True)
    customer_average_revenue = fields.Char(string='Customer Average Revenue',index=True)
    blacklist_receivable_amount_at_customer = fields.Char(string='Blacklist receivable amount at customer ',index=True)
    blacklist_debt_amount_at_customer = fields.Char(string='Blacklist debt amount at customer ',index=True)
    calculated_blacklist_threshold_at_customer = fields.Char(string='Calculated Blacklist threshold at customer ',index=True)

    
    

    
  
    





    _sql_constraints = [('customerexist', 'UNIQUE (account_id)', 'This customer already exists')]
    



    
  
  
