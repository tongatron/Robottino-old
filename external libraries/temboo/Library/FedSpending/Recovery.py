# -*- coding: utf-8 -*-

###############################################################################
#
# Recovery
# Allows access to the information in the Recovery Act Recipient Reports database.
#
# Python versions 2.6, 2.7, 3.x
#
# Copyright 2014, Temboo Inc.
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Recovery(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Recovery Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Recovery, self).__init__(temboo_session, '/Library/FedSpending/Recovery')


    def new_input_set(self):
        return RecoveryInputSet()

    def _make_result_set(self, result, path):
        return RecoveryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RecoveryChoreographyExecution(session, exec_id, path)

class RecoveryInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Recovery
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Activity(self, value):
        """
        Set the value of the Activity input for this Choreo. ((conditional, string) Whether or not to search by activity. (Will provide a select list if "y"). y = yes, n = no. Defaults to n if not set.)
        """
        super(RecoveryInputSet, self)._set_input('Activity', value)
    def set_AwardAmount(self, value):
        """
        Set the value of the AwardAmount input for this Choreo. ((conditional, string) Grants: total Federal dollars. Loans: face value of loan obligated by the Federal Agency. Contracts: total amount obligated by Federal Agency. Vendors: payment amount. Recipients:  amount of award.)
        """
        super(RecoveryInputSet, self)._set_input('AwardAmount', value)
    def set_AwardNumber(self, value):
        """
        Set the value of the AwardNumber input for this Choreo. ((conditional, integer) Identifying number assigned by the awarding Federal Agency. e.g. federal grant number, federal contract number or federal loan number. For grants and loans, this is assigned by the prime recipient.)
        """
        super(RecoveryInputSet, self)._set_input('AwardNumber', value)
    def set_AwardType(self, value):
        """
        Set the value of the AwardType input for this Choreo. ((conditional, string) Acceptable values: G = Grants only,L = Loans only, C = Contracts only.)
        """
        super(RecoveryInputSet, self)._set_input('AwardType', value)
    def set_AwardingAgency(self, value):
        """
        Set the value of the AwardingAgency input for this Choreo. ((conditional, string) The 4-digit code for a specific governmental awarding agency that awarded and is administering the award on behalf of the funding agency.)
        """
        super(RecoveryInputSet, self)._set_input('AwardingAgency', value)
    def set_CFDA(self, value):
        """
        Set the value of the CFDA input for this Choreo. ((conditional, string) The Catalog of Federal Domestic Number is the number associated with the published description of a Federal Assistance program in the CFDA.)
        """
        super(RecoveryInputSet, self)._set_input('CFDA', value)
    def set_Detail(self, value):
        """
        Set the value of the Detail input for this Choreo. ((optional, string) Controls the level of detail of the output. Acceptable values: -1 (summary), 0 (low), 1 (medium), 2 (high), and 3 (extensive). Defaults to -1. See docs for more information.)
        """
        super(RecoveryInputSet, self)._set_input('Detail', value)
    def set_EntityDun(self, value):
        """
        Set the value of the EntityDun input for this Choreo. ((conditional, string) The prime recipient for the award's Dun & Bradstreet number (no vendor information).)
        """
        super(RecoveryInputSet, self)._set_input('EntityDun', value)
    def set_FirstYearRange(self, value):
        """
        Set the value of the FirstYearRange input for this Choreo. ((conditional, integer) Specifies the first year in a range of years from 2000-2006; if used, must be used with LastYearRange and without FiscalYear.)
        """
        super(RecoveryInputSet, self)._set_input('FirstYearRange', value)
    def set_FiscalYear(self, value):
        """
        Set the value of the FiscalYear input for this Choreo. ((conditional, integer) Specifies a single year; defaults to all years.)
        """
        super(RecoveryInputSet, self)._set_input('FiscalYear', value)
    def set_FundingAgency(self, value):
        """
        Set the value of the FundingAgency input for this Choreo. ((conditional, string) The 4-digit code for a specific governmental agency that is responsible for funding/distributing the ARRA funds to recipients.)
        """
        super(RecoveryInputSet, self)._set_input('FundingAgency', value)
    def set_FundingTAS(self, value):
        """
        Set the value of the FundingTAS input for this Choreo. ((conditional, string) The Agency Treasury Account Symbol (TAS) that identifies the funding Program Source. The Program Source is based out of the OMB TAS list.)
        """
        super(RecoveryInputSet, self)._set_input('FundingTAS', value)
    def set_GovtContractOffice(self, value):
        """
        Set the value of the GovtContractOffice input for this Choreo. ((conditional, string) The agency supplied code of the government contracting office that executed the transaction. (For prime recipients only.))
        """
        super(RecoveryInputSet, self)._set_input('GovtContractOffice', value)
    def set_LastYearRange(self, value):
        """
        Set the value of the LastYearRange input for this Choreo. ((conditional, integer) Specifies the last year in a range of years; if used, must be used with FirstYearRange and without FiscalYear.)
        """
        super(RecoveryInputSet, self)._set_input('LastYearRange', value)
    def set_MaxRecords(self, value):
        """
        Set the value of the MaxRecords input for this Choreo. ((optional, integer) Allows you to set the maximum number of records retrieved. Defaults to 100.)
        """
        super(RecoveryInputSet, self)._set_input('MaxRecords', value)
    def set_NumberOfJobs(self, value):
        """
        Set the value of the NumberOfJobs input for this Choreo. ((conditional, integer) The number of Full-Time Equivalent (FTE) jobs created and retained.)
        """
        super(RecoveryInputSet, self)._set_input('NumberOfJobs', value)
    def set_OfficerComp(self, value):
        """
        Set the value of the OfficerComp input for this Choreo. ((conditional, integer) Total compensation of first highly compensated officer.)
        """
        super(RecoveryInputSet, self)._set_input('OfficerComp', value)
    def set_OrderNumber(self, value):
        """
        Set the value of the OrderNumber input for this Choreo. ((conditional, string) This is an identifying number assigned to the contract.)
        """
        super(RecoveryInputSet, self)._set_input('OrderNumber', value)
    def set_PopCity(self, value):
        """
        Set the value of the PopCity input for this Choreo. ((conditional, string) The city in which work was performed.)
        """
        super(RecoveryInputSet, self)._set_input('PopCity', value)
    def set_PopCountry(self, value):
        """
        Set the value of the PopCountry input for this Choreo. ((conditional, string) The two-letter country code for the country in which work was performed.)
        """
        super(RecoveryInputSet, self)._set_input('PopCountry', value)
    def set_PopDistrict(self, value):
        """
        Set the value of the PopDistrict input for this Choreo. ((conditional, string) The Congressional District in which work was performed.)
        """
        super(RecoveryInputSet, self)._set_input('PopDistrict', value)
    def set_PopState(self, value):
        """
        Set the value of the PopState input for this Choreo. ((conditional, string) The two-letter code for the state in which in which work was performed (the "place of performance").)
        """
        super(RecoveryInputSet, self)._set_input('PopState', value)
    def set_PopZip(self, value):
        """
        Set the value of the PopZip input for this Choreo. ((conditional, integer) The ZIP code in which work was performed.)
        """
        super(RecoveryInputSet, self)._set_input('PopZip', value)
    def set_ProjectDescription(self, value):
        """
        Set the value of the ProjectDescription input for this Choreo. ((conditional, string) A description of the project under which the award is funded.)
        """
        super(RecoveryInputSet, self)._set_input('ProjectDescription', value)
    def set_RecipientDistrict(self, value):
        """
        Set the value of the RecipientDistrict input for this Choreo. ((conditional, string) A 4-character numeric designation for the Congressional District within which a recipient or vendor is located. (For prime recipients and sub-recipients only.))
        """
        super(RecoveryInputSet, self)._set_input('RecipientDistrict', value)
    def set_RecipientName(self, value):
        """
        Set the value of the RecipientName input for this Choreo. ((conditional, string) The name of the recipient (prime recipient, sub-recipient, or vendor); value given is used as a text search.)
        """
        super(RecoveryInputSet, self)._set_input('RecipientName', value)
    def set_RecipientStateCode(self, value):
        """
        Set the value of the RecipientStateCode input for this Choreo. ((conditional, string) The postal state abbreviation for the state in the recipient's address (can be for prime recipient, sub-recipient, or vendor).)
        """
        super(RecoveryInputSet, self)._set_input('RecipientStateCode', value)
    def set_RecipientType(self, value):
        """
        Set the value of the RecipientType input for this Choreo. ((conditional, string) Recipient or vendor type: p = Prime recipients only, s = Sub-recipients only, v = Vendors only.)
        """
        super(RecoveryInputSet, self)._set_input('RecipientType', value)
    def set_RecipientZip(self, value):
        """
        Set the value of the RecipientZip input for this Choreo. ((conditional, integer) The ZIP code of the recipient (prime recipient, sub-recipient, or vendor).)
        """
        super(RecoveryInputSet, self)._set_input('RecipientZip', value)
    def set_Sort(self, value):
        """
        Set the value of the Sort input for this Choreo. ((optional, string) Determines the order in which records are sorted. The default value sorts by Recipient/Vendor Name. See doc for all other values.)
        """
        super(RecoveryInputSet, self)._set_input('Sort', value)
    def set_TextSearch(self, value):
        """
        Set the value of the TextSearch input for this Choreo. ((conditional, string) Full text search.)
        """
        super(RecoveryInputSet, self)._set_input('TextSearch', value)

class RecoveryResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Recovery Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from FedSpending.org.)
        """
        return self._output.get('Response', None)

class RecoveryChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RecoveryResultSet(response, path)
