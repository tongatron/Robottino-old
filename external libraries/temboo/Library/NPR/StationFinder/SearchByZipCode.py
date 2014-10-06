# -*- coding: utf-8 -*-

###############################################################################
#
# SearchByZipCode
# Retrieves local NPR member stations based on zip code.
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

class SearchByZipCode(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchByZipCode Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(SearchByZipCode, self).__init__(temboo_session, '/Library/NPR/StationFinder/SearchByZipCode')


    def new_input_set(self):
        return SearchByZipCodeInputSet()

    def _make_result_set(self, result, path):
        return SearchByZipCodeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchByZipCodeChoreographyExecution(session, exec_id, path)

class SearchByZipCodeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchByZipCode
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by NPR.)
        """
        super(SearchByZipCodeInputSet, self)._set_input('APIKey', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are xml (the default), and json.)
        """
        super(SearchByZipCodeInputSet, self)._set_input('ResponseFormat', value)
    def set_Zip(self, value):
        """
        Set the value of the Zip input for this Choreo. ((required, string) Enter a five-digit zip code.)
        """
        super(SearchByZipCodeInputSet, self)._set_input('Zip', value)

class SearchByZipCodeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchByZipCode Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from NPR.)
        """
        return self._output.get('Response', None)

class SearchByZipCodeChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SearchByZipCodeResultSet(response, path)
