# -*- coding: utf-8 -*-

###############################################################################
#
# AcceptInvite
# Accepts or rejects an invite to become friends with inviting user.
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

class AcceptInvite(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AcceptInvite Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(AcceptInvite, self).__init__(temboo_session, '/Library/Fitbit/Social/AcceptInvite')


    def new_input_set(self):
        return AcceptInviteInputSet()

    def _make_result_set(self, result, path):
        return AcceptInviteResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AcceptInviteChoreographyExecution(session, exec_id, path)

class AcceptInviteInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AcceptInvite
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Accept(self, value):
        """
        Set the value of the Accept input for this Choreo. ((required, boolean) Accept or reject an invite; (true or false).)
        """
        super(AcceptInviteInputSet, self)._set_input('Accept', value)
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(AcceptInviteInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(AcceptInviteInputSet, self)._set_input('AccessToken', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The Consumer Key provided by Fitbit.)
        """
        super(AcceptInviteInputSet, self)._set_input('ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The Consumer Secret provided by Fitbit.)
        """
        super(AcceptInviteInputSet, self)._set_input('ConsumerSecret', value)
    def set_FromUserID(self, value):
        """
        Set the value of the FromUserID input for this Choreo. ((required, string) The user's id to indicate user to accept or reject invite from.)
        """
        super(AcceptInviteInputSet, self)._set_input('FromUserID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that you want the response to be in: xml or json. Defaults to json.)
        """
        super(AcceptInviteInputSet, self)._set_input('ResponseFormat', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((optional, string) The user's encoded id. Defaults to "-" (dash) which will return data for the user associated with the token credentials provided.)
        """
        super(AcceptInviteInputSet, self)._set_input('UserID', value)

class AcceptInviteResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AcceptInvite Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Fitbit.)
        """
        return self._output.get('Response', None)

class AcceptInviteChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return AcceptInviteResultSet(response, path)
