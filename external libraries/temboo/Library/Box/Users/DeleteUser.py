# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteUser
# Deletes a specified user.
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

class DeleteUser(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteUser Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DeleteUser, self).__init__(temboo_session, '/Library/Box/Users/DeleteUser')


    def new_input_set(self):
        return DeleteUserInputSet()

    def _make_result_set(self, result, path):
        return DeleteUserResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteUserChoreographyExecution(session, exec_id, path)

class DeleteUserInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteUser
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved during the OAuth2 process.)
        """
        super(DeleteUserInputSet, self)._set_input('AccessToken', value)
    def set_AsUser(self, value):
        """
        Set the value of the AsUser input for this Choreo. ((optional, string) The ID of the user. Only used for enterprise administrators to make API calls for their managed users.)
        """
        super(DeleteUserInputSet, self)._set_input('AsUser', value)
    def set_Force(self, value):
        """
        Set the value of the Force input for this Choreo. ((optional, boolean) Whether or not the user should be deleted even when they still own files.)
        """
        super(DeleteUserInputSet, self)._set_input('Force', value)
    def set_Notify(self, value):
        """
        Set the value of the Notify input for this Choreo. ((optional, boolean) Indicates that the user should receive an email notification of the transfer.)
        """
        super(DeleteUserInputSet, self)._set_input('Notify', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((required, string) The id of the user whose information should be updated.)
        """
        super(DeleteUserInputSet, self)._set_input('UserID', value)

class DeleteUserResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteUser Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Box.)
        """
        return self._output.get('Response', None)

class DeleteUserChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeleteUserResultSet(response, path)
