# -*- coding: utf-8 -*-

###############################################################################
#
# TagName
# Retrieves information about a tag object.
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

class TagName(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the TagName Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(TagName, self).__init__(temboo_session, '/Library/Instagram/TagName')


    def new_input_set(self):
        return TagNameInputSet()

    def _make_result_set(self, result, path):
        return TagNameResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TagNameChoreographyExecution(session, exec_id, path)

class TagNameInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the TagName
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((conditional, string) The access token retrieved during the OAuth 2.0 process. Required unless you provide the ClientID.)
        """
        super(TagNameInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Instagram after registering your application. Required unless you provide an AccessToken.)
        """
        super(TagNameInputSet, self)._set_input('ClientID', value)
    def set_TagName(self, value):
        """
        Set the value of the TagName input for this Choreo. ((required, string) Enter a valid tag identifier, such as: nofliter)
        """
        super(TagNameInputSet, self)._set_input('TagName', value)

class TagNameResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the TagName Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Instagram.)
        """
        return self._output.get('Response', None)

class TagNameChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return TagNameResultSet(response, path)
