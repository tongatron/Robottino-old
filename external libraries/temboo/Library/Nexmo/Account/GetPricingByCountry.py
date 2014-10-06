# -*- coding: utf-8 -*-

###############################################################################
#
# GetPricingByCountry
# Retrieve Nexmo's outbound pricing for the specified country.
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

class GetPricingByCountry(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetPricingByCountry Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetPricingByCountry, self).__init__(temboo_session, '/Library/Nexmo/Account/GetPricingByCountry')


    def new_input_set(self):
        return GetPricingByCountryInputSet()

    def _make_result_set(self, result, path):
        return GetPricingByCountryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetPricingByCountryChoreographyExecution(session, exec_id, path)

class GetPricingByCountryInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetPricingByCountry
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) Your API Key provided to you by Nexmo.)
        """
        super(GetPricingByCountryInputSet, self)._set_input('APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((required, string) Your API Secret provided to you by Nexmo.)
        """
        super(GetPricingByCountryInputSet, self)._set_input('APISecret', value)
    def set_Country(self, value):
        """
        Set the value of the Country input for this Choreo. ((required, string) A 2 letter country code.  (e.g. CA))
        """
        super(GetPricingByCountryInputSet, self)._set_input('Country', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "json" (the default) and "xml".)
        """
        super(GetPricingByCountryInputSet, self)._set_input('ResponseFormat', value)

class GetPricingByCountryResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetPricingByCountry Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Nexmo. Corresponds to the ResponseFormat input. Defaults to json.)
        """
        return self._output.get('Response', None)

class GetPricingByCountryChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetPricingByCountryResultSet(response, path)
