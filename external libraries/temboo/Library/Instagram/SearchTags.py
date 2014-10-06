# -*- coding: utf-8 -*-

###############################################################################
#
# SearchTags
# Searches for tags by name.
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

class SearchTags(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchTags Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(SearchTags, self).__init__(temboo_session, '/Library/Instagram/SearchTags')


    def new_input_set(self):
        return SearchTagsInputSet()

    def _make_result_set(self, result, path):
        return SearchTagsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchTagsChoreographyExecution(session, exec_id, path)

class SearchTagsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchTags
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((conditional, string) The access token retrieved during the OAuth 2.0 process. Required unless you provide the ClientID.)
        """
        super(SearchTagsInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Instagram after registering your application. Required unless you provide an AccessToken.)
        """
        super(SearchTagsInputSet, self)._set_input('ClientID', value)
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((required, string) A tag name to search for (e.g., snow, beach). Do not include a leading hash symbol in your query.)
        """
        super(SearchTagsInputSet, self)._set_input('Query', value)

class SearchTagsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchTags Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Instagram.)
        """
        return self._output.get('Response', None)

class SearchTagsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SearchTagsResultSet(response, path)
