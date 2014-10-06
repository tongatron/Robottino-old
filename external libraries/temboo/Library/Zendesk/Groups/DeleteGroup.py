# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteGroup
# Deletes an existing group.
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

class DeleteGroup(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteGroup Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DeleteGroup, self).__init__(temboo_session, '/Library/Zendesk/Groups/DeleteGroup')


    def new_input_set(self):
        return DeleteGroupInputSet()

    def _make_result_set(self, result, path):
        return DeleteGroupResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteGroupChoreographyExecution(session, exec_id, path)

class DeleteGroupInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteGroup
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((required, string) The email address you use to login to your Zendesk account.)
        """
        super(DeleteGroupInputSet, self)._set_input('Email', value)
    def set_GroupID(self, value):
        """
        Set the value of the GroupID input for this Choreo. ((required, string) The ID of group to delete.)
        """
        super(DeleteGroupInputSet, self)._set_input('GroupID', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Zendesk password.)
        """
        super(DeleteGroupInputSet, self)._set_input('Password', value)
    def set_Server(self, value):
        """
        Set the value of the Server input for this Choreo. ((required, string) Your Zendesk domain and subdomain (e.g., temboocare.zendesk.com).)
        """
        super(DeleteGroupInputSet, self)._set_input('Server', value)

class DeleteGroupResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteGroup Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Zendesk.)
        """
        return self._output.get('Response', None)
    def get_ResponseStatusCode(self):
        """
        Retrieve the value for the "ResponseStatusCode" output from this Choreo execution. ((integer) The response status code returned from Zendesk.)
        """
        return self._output.get('ResponseStatusCode', None)

class DeleteGroupChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeleteGroupResultSet(response, path)
