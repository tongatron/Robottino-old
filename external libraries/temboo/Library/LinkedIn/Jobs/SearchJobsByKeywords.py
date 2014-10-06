# -*- coding: utf-8 -*-

###############################################################################
#
# SearchJobsByKeywords
# Retrieve jobs matching the specified keyword(s).
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

class SearchJobsByKeywords(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchJobsByKeywords Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(SearchJobsByKeywords, self).__init__(temboo_session, '/Library/LinkedIn/Jobs/SearchJobsByKeywords')


    def new_input_set(self):
        return SearchJobsByKeywordsInputSet()

    def _make_result_set(self, result, path):
        return SearchJobsByKeywordsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchJobsByKeywordsChoreographyExecution(session, exec_id, path)

class SearchJobsByKeywordsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchJobsByKeywords
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by LinkedIn (AKA the OAuth Consumer Key).)
        """
        super(SearchJobsByKeywordsInputSet, self)._set_input('APIKey', value)
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(SearchJobsByKeywordsInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(SearchJobsByKeywordsInputSet, self)._set_input('AccessToken', value)
    def set_Count(self, value):
        """
        Set the value of the Count input for this Choreo. ((optional, integer) Specify the number of jobs to be returned.  Default is 10.  The maximum is 20.)
        """
        super(SearchJobsByKeywordsInputSet, self)._set_input('Count', value)
    def set_Keywords(self, value):
        """
        Set the value of the Keywords input for this Choreo. ((required, string) Limit search by specified keyword(s).)
        """
        super(SearchJobsByKeywordsInputSet, self)._set_input('Keywords', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml (the default) and json.)
        """
        super(SearchJobsByKeywordsInputSet, self)._set_input('ResponseFormat', value)
    def set_SecretKey(self, value):
        """
        Set the value of the SecretKey input for this Choreo. ((required, string) The Secret Key provided by LinkedIn (AKA the OAuth Consumer Secret).)
        """
        super(SearchJobsByKeywordsInputSet, self)._set_input('SecretKey', value)
    def set_Sort(self, value):
        """
        Set the value of the Sort input for this Choreo. ((optional, string) Specify the ordering of results. Enter R (for relationship from job to member); DA (dated posted in ascending order); DO (job posted in descending order).)
        """
        super(SearchJobsByKeywordsInputSet, self)._set_input('Sort', value)

class SearchJobsByKeywordsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchJobsByKeywords Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from LinkedIn.)
        """
        return self._output.get('Response', None)

class SearchJobsByKeywordsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SearchJobsByKeywordsResultSet(response, path)
