# -*- coding: utf-8 -*-

###############################################################################
#
# GetCompanyByEIN
# Returns a company record for a given IRS Employer Identification Number (tax ID).
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

class GetCompanyByEIN(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetCompanyByEIN Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetCompanyByEIN, self).__init__(temboo_session, '/Library/CorpWatch/Company/GetCompanyByEIN')


    def new_input_set(self):
        return GetCompanyByEINInputSet()

    def _make_result_set(self, result, path):
        return GetCompanyByEINResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetCompanyByEINChoreographyExecution(session, exec_id, path)

class GetCompanyByEINInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetCompanyByEIN
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((optional, string) The APIKey from CorpWatch if you have one.)
        """
        super(GetCompanyByEINInputSet, self)._set_input('APIKey', value)
    def set_EIN(self, value):
        """
        Set the value of the EIN input for this Choreo. ((required, string) The IRS Employer Identification Number (tax ID) of a company.)
        """
        super(GetCompanyByEINInputSet, self)._set_input('EIN', value)
    def set_Index(self, value):
        """
        Set the value of the Index input for this Choreo. ((optional, integer) Set the index number of the first result to be returned. The index of the first result is 0.)
        """
        super(GetCompanyByEINInputSet, self)._set_input('Index', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number of results to be returned. Defaults to 100. Maximum is 5000.)
        """
        super(GetCompanyByEINInputSet, self)._set_input('Limit', value)
    def set_ResponseType(self, value):
        """
        Set the value of the ResponseType input for this Choreo. ((optional, string) Specify json or xml for the type of response to be returned. Defaults to xml.)
        """
        super(GetCompanyByEINInputSet, self)._set_input('ResponseType', value)
    def set_Year(self, value):
        """
        Set the value of the Year input for this Choreo. ((optional, integer) If a year is specified, only records for that year will be returned and the data in the company objects returned will be set appropriately for the request year. Defaults to most recent.)
        """
        super(GetCompanyByEINInputSet, self)._set_input('Year', value)

class GetCompanyByEINResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetCompanyByEIN Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from CorpWatch.)
        """
        return self._output.get('Response', None)

class GetCompanyByEINChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetCompanyByEINResultSet(response, path)
