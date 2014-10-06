# -*- coding: utf-8 -*-

###############################################################################
#
# GetMessageByID
# Retrieves a single direct message, specified by an id.
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

class GetMessageByID(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetMessageByID Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetMessageByID, self).__init__(temboo_session, '/Library/Twitter/DirectMessages/GetMessageByID')


    def new_input_set(self):
        return GetMessageByIDInputSet()

    def _make_result_set(self, result, path):
        return GetMessageByIDResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetMessageByIDChoreographyExecution(session, exec_id, path)

class GetMessageByIDInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetMessageByID
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret provided by Twitter or retrieved during the OAuth process.)
        """
        super(GetMessageByIDInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token provided by Twitter or retrieved during the OAuth process.)
        """
        super(GetMessageByIDInputSet, self)._set_input('AccessToken', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The Consumer Key provided by Twitter.)
        """
        super(GetMessageByIDInputSet, self)._set_input('ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The Consumer Secret provided by Twitter.)
        """
        super(GetMessageByIDInputSet, self)._set_input('ConsumerSecret', value)
    def set_ID(self, value):
        """
        Set the value of the ID input for this Choreo. ((required, string) The ID of the direct message.)
        """
        super(GetMessageByIDInputSet, self)._set_input('ID', value)

class GetMessageByIDResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetMessageByID Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Twitter.)
        """
        return self._output.get('Response', None)
    def get_Limit(self):
        """
        Retrieve the value for the "Limit" output from this Choreo execution. ((integer) The rate limit ceiling for this particular request.)
        """
        return self._output.get('Limit', None)
    def get_Remaining(self):
        """
        Retrieve the value for the "Remaining" output from this Choreo execution. ((integer) The number of requests left for the 15 minute window.)
        """
        return self._output.get('Remaining', None)
    def get_Reset(self):
        """
        Retrieve the value for the "Reset" output from this Choreo execution. ((date) The remaining window before the rate limit resets in UTC epoch seconds.)
        """
        return self._output.get('Reset', None)

class GetMessageByIDChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetMessageByIDResultSet(response, path)
