# -*- coding: utf-8 -*-

###############################################################################
#
# LinkLookup
# Used to lookup a bitly link with a given long URL.
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

class LinkLookup(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the LinkLookup Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(LinkLookup, self).__init__(temboo_session, '/Library/Bitly/Links/LinkLookup')


    def new_input_set(self):
        return LinkLookupInputSet()

    def _make_result_set(self, result, path):
        return LinkLookupResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return LinkLookupChoreographyExecution(session, exec_id, path)

class LinkLookupInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the LinkLookup
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The oAuth access token provided by Bitly.)
        """
        super(LinkLookupInputSet, self)._set_input('AccessToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that you want the response to be in. Accepted values are "json" or "xml". Defaults to "json".)
        """
        super(LinkLookupInputSet, self)._set_input('ResponseFormat', value)
    def set_URL(self, value):
        """
        Set the value of the URL input for this Choreo. ((required, string) One or more long URLs to lookup.)
        """
        super(LinkLookupInputSet, self)._set_input('URL', value)

class LinkLookupResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the LinkLookup Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Bitly.)
        """
        return self._output.get('Response', None)

class LinkLookupChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return LinkLookupResultSet(response, path)
