# -*- coding: utf-8 -*-

###############################################################################
#
# GetCompanyFilings
# Returns the official SEC documents from which a company's information was extracted in order to check the accuracy of data.
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

class GetCompanyFilings(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetCompanyFilings Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetCompanyFilings, self).__init__(temboo_session, '/Library/CorpWatch/Company/GetCompanyFilings')


    def new_input_set(self):
        return GetCompanyFilingsInputSet()

    def _make_result_set(self, result, path):
        return GetCompanyFilingsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetCompanyFilingsChoreographyExecution(session, exec_id, path)

class GetCompanyFilingsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetCompanyFilings
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((optional, string) The APIKey from CorpWatch if you have one.)
        """
        super(GetCompanyFilingsInputSet, self)._set_input('APIKey', value)
    def set_CWID(self, value):
        """
        Set the value of the CWID input for this Choreo. ((required, string) CoprWatch ID for the company. Format looks like: cw_8484.)
        """
        super(GetCompanyFilingsInputSet, self)._set_input('CWID', value)
    def set_Index(self, value):
        """
        Set the value of the Index input for this Choreo. ((optional, integer) Set the index number of the first result to be returned. The index of the first result is 0.)
        """
        super(GetCompanyFilingsInputSet, self)._set_input('Index', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number of results to be returned. Defaults to 100. Maximum is 5000.)
        """
        super(GetCompanyFilingsInputSet, self)._set_input('Limit', value)
    def set_ResponseType(self, value):
        """
        Set the value of the ResponseType input for this Choreo. ((optional, string) Specify json or xml for the type of response to be returned. Defaults to xml.)
        """
        super(GetCompanyFilingsInputSet, self)._set_input('ResponseType', value)

class GetCompanyFilingsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetCompanyFilings Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from CorpWatch.)
        """
        return self._output.get('Response', None)

class GetCompanyFilingsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetCompanyFilingsResultSet(response, path)
