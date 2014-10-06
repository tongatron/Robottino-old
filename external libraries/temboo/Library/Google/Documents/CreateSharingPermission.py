# -*- coding: utf-8 -*-

###############################################################################
#
# CreateSharingPermission
# Grants a new user read/write access to an existing document.
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

class CreateSharingPermission(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateSharingPermission Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateSharingPermission, self).__init__(temboo_session, '/Library/Google/Documents/CreateSharingPermission')


    def new_input_set(self):
        return CreateSharingPermissionInputSet()

    def _make_result_set(self, result, path):
        return CreateSharingPermissionResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateSharingPermissionChoreographyExecution(session, exec_id, path)

class CreateSharingPermissionInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateSharingPermission
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_NewUserEmail(self, value):
        """
        Set the value of the NewUserEmail input for this Choreo. ((required, string) The email address of the user to whom you want to grant permission.)
        """
        super(CreateSharingPermissionInputSet, self)._set_input('NewUserEmail', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Google passsword.)
        """
        super(CreateSharingPermissionInputSet, self)._set_input('Password', value)
    def set_Role(self, value):
        """
        Set the value of the Role input for this Choreo. ((optional, string) The role that will be given to the new user permission (i.e., writer, reader, etc). Defaults to "writer".)
        """
        super(CreateSharingPermissionInputSet, self)._set_input('Role', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your full Google email address e.g., martha.temboo@gmail.com.)
        """
        super(CreateSharingPermissionInputSet, self)._set_input('Username', value)

class CreateSharingPermissionResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateSharingPermission Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Google.)
        """
        return self._output.get('Response', None)
    def get_ResourceID(self):
        """
        Retrieve the value for the "ResourceID" output from this Choreo execution. ((string) The resource ID of the document to which you want to add a user.)
        """
        return self._output.get('ResourceID', None)

class CreateSharingPermissionChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateSharingPermissionResultSet(response, path)
