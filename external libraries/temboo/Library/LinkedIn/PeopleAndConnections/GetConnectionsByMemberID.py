# -*- coding: utf-8 -*-

###############################################################################
#
# GetConnectionsByMemberID
# Retrieve all connections linked to a  member ID.
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

class GetConnectionsByMemberID(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetConnectionsByMemberID Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetConnectionsByMemberID, self).__init__(temboo_session, '/Library/LinkedIn/PeopleAndConnections/GetConnectionsByMemberID')


    def new_input_set(self):
        return GetConnectionsByMemberIDInputSet()

    def _make_result_set(self, result, path):
        return GetConnectionsByMemberIDResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetConnectionsByMemberIDChoreographyExecution(session, exec_id, path)

class GetConnectionsByMemberIDInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetConnectionsByMemberID
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by LinkedIn (AKA the OAuth Consumer Key).)
        """
        super(GetConnectionsByMemberIDInputSet, self)._set_input('APIKey', value)
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(GetConnectionsByMemberIDInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(GetConnectionsByMemberIDInputSet, self)._set_input('AccessToken', value)
    def set_MemberID(self, value):
        """
        Set the value of the MemberID input for this Choreo. ((required, integer) Enter a LinkedIn Member ID.)
        """
        super(GetConnectionsByMemberIDInputSet, self)._set_input('MemberID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml (the default) and json.)
        """
        super(GetConnectionsByMemberIDInputSet, self)._set_input('ResponseFormat', value)
    def set_SecretKey(self, value):
        """
        Set the value of the SecretKey input for this Choreo. ((required, string) The Secret Key provided by LinkedIn (AKA the OAuth Consumer Secret).)
        """
        super(GetConnectionsByMemberIDInputSet, self)._set_input('SecretKey', value)

class GetConnectionsByMemberIDResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetConnectionsByMemberID Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from LinkedIn.)
        """
        return self._output.get('Response', None)

class GetConnectionsByMemberIDChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetConnectionsByMemberIDResultSet(response, path)
