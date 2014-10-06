# -*- coding: utf-8 -*-

###############################################################################
#
# SearchJobsByZipcodeAndCountryCode
# Retrieve jobs filtered by zipcode (postal code) and country code.
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

class SearchJobsByZipcodeAndCountryCode(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchJobsByZipcodeAndCountryCode Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(SearchJobsByZipcodeAndCountryCode, self).__init__(temboo_session, '/Library/LinkedIn/Jobs/SearchJobsByZipcodeAndCountryCode')


    def new_input_set(self):
        return SearchJobsByZipcodeAndCountryCodeInputSet()

    def _make_result_set(self, result, path):
        return SearchJobsByZipcodeAndCountryCodeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchJobsByZipcodeAndCountryCodeChoreographyExecution(session, exec_id, path)

class SearchJobsByZipcodeAndCountryCodeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchJobsByZipcodeAndCountryCode
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by LinkedIn (AKA the OAuth Consumer Key).)
        """
        super(SearchJobsByZipcodeAndCountryCodeInputSet, self)._set_input('APIKey', value)
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(SearchJobsByZipcodeAndCountryCodeInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(SearchJobsByZipcodeAndCountryCodeInputSet, self)._set_input('AccessToken', value)
    def set_Count(self, value):
        """
        Set the value of the Count input for this Choreo. ((optional, integer) Specify the number of jobs to be returned.  Default is 10.  The maximum is 20.)
        """
        super(SearchJobsByZipcodeAndCountryCodeInputSet, self)._set_input('Count', value)
    def set_CountryCode(self, value):
        """
        Set the value of the CountryCode input for this Choreo. ((optional, string) Enter an ISO 3166 country code.  Default is set to U.S. (US).)
        """
        super(SearchJobsByZipcodeAndCountryCodeInputSet, self)._set_input('CountryCode', value)
    def set_PostalCode(self, value):
        """
        Set the value of the PostalCode input for this Choreo. ((required, string) Enter a postal (zip) code.  Don't forget to also set the CountryCode variable.)
        """
        super(SearchJobsByZipcodeAndCountryCodeInputSet, self)._set_input('PostalCode', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml (the default) and json.)
        """
        super(SearchJobsByZipcodeAndCountryCodeInputSet, self)._set_input('ResponseFormat', value)
    def set_SecretKey(self, value):
        """
        Set the value of the SecretKey input for this Choreo. ((required, string) The Secret Key provided by LinkedIn (AKA the OAuth Consumer Secret).)
        """
        super(SearchJobsByZipcodeAndCountryCodeInputSet, self)._set_input('SecretKey', value)
    def set_Sort(self, value):
        """
        Set the value of the Sort input for this Choreo. ((optional, string) Specify the ordering of results. Enter R (for relationship from job to member); DA (dated posted in ascending order); DO (job posted in descending order).)
        """
        super(SearchJobsByZipcodeAndCountryCodeInputSet, self)._set_input('Sort', value)

class SearchJobsByZipcodeAndCountryCodeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchJobsByZipcodeAndCountryCode Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from LinkedIn.)
        """
        return self._output.get('Response', None)

class SearchJobsByZipcodeAndCountryCodeChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SearchJobsByZipcodeAndCountryCodeResultSet(response, path)
