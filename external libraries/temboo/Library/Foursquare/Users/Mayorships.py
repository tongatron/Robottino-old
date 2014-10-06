# -*- coding: utf-8 -*-

###############################################################################
#
# Mayorships
# Returns a user's mayorships.
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

class Mayorships(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Mayorships Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Mayorships, self).__init__(temboo_session, '/Library/Foursquare/Users/Mayorships')


    def new_input_set(self):
        return MayorshipsInputSet()

    def _make_result_set(self, result, path):
        return MayorshipsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return MayorshipsChoreographyExecution(session, exec_id, path)

class MayorshipsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Mayorships
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((required, string) The Foursquare API OAuth token string.)
        """
        super(MayorshipsInputSet, self)._set_input('OauthToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(MayorshipsInputSet, self)._set_input('ResponseFormat', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((optional, string) Identity of the user to get mayorships for. Defaults to "self" to get lists of the acting user.)
        """
        super(MayorshipsInputSet, self)._set_input('UserID', value)

class MayorshipsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Mayorships Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class MayorshipsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return MayorshipsResultSet(response, path)
