# -*- coding: utf-8 -*-

###############################################################################
#
# FindByKeyword
# Returns a list of place IDs for a query string.
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

class FindByKeyword(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FindByKeyword Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(FindByKeyword, self).__init__(temboo_session, '/Library/Flickr/Places/FindByKeyword')


    def new_input_set(self):
        return FindByKeywordInputSet()

    def _make_result_set(self, result, path):
        return FindByKeywordResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FindByKeywordChoreographyExecution(session, exec_id, path)

class FindByKeywordInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FindByKeyword
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Flickr (AKA the OAuth Consumer Key).)
        """
        super(FindByKeywordInputSet, self)._set_input('APIKey', value)
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((required, string) The query string to use for place ID lookups.)
        """
        super(FindByKeywordInputSet, self)._set_input('Query', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml and json. Defaults to json.)
        """
        super(FindByKeywordInputSet, self)._set_input('ResponseFormat', value)

class FindByKeywordResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FindByKeyword Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Flickr.)
        """
        return self._output.get('Response', None)

class FindByKeywordChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return FindByKeywordResultSet(response, path)
