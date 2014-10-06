# -*- coding: utf-8 -*-

###############################################################################
#
# ListModerators
# Retrieves a list of all moderators on a forum.
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

class ListModerators(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListModerators Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListModerators, self).__init__(temboo_session, '/Library/Disqus/Forums/ListModerators')


    def new_input_set(self):
        return ListModeratorsInputSet()

    def _make_result_set(self, result, path):
        return ListModeratorsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListModeratorsChoreographyExecution(session, exec_id, path)

class ListModeratorsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListModerators
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) A valid OAuth 2.0 access token.)
        """
        super(ListModeratorsInputSet, self)._set_input('AccessToken', value)
    def set_Forum(self, value):
        """
        Set the value of the Forum input for this Choreo. ((required, string) Forum Short Name (i.e., the subdomain of the Disqus Site URL).)
        """
        super(ListModeratorsInputSet, self)._set_input('Forum', value)
    def set_PublicKey(self, value):
        """
        Set the value of the PublicKey input for this Choreo. ((required, string) The Public Key provided by Disqus (AKA the API Key).)
        """
        super(ListModeratorsInputSet, self)._set_input('PublicKey', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default), jsonp, or rss.)
        """
        super(ListModeratorsInputSet, self)._set_input('ResponseFormat', value)

class ListModeratorsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListModerators Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Disqus.)
        """
        return self._output.get('Response', None)

class ListModeratorsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListModeratorsResultSet(response, path)
