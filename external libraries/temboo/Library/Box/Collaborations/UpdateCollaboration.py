# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateCollaboration
# Edits an existing collaboration.
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

class UpdateCollaboration(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateCollaboration Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateCollaboration, self).__init__(temboo_session, '/Library/Box/Collaborations/UpdateCollaboration')


    def new_input_set(self):
        return UpdateCollaborationInputSet()

    def _make_result_set(self, result, path):
        return UpdateCollaborationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateCollaborationChoreographyExecution(session, exec_id, path)

class UpdateCollaborationInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateCollaboration
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved during the OAuth2 process.)
        """
        super(UpdateCollaborationInputSet, self)._set_input('AccessToken', value)
    def set_AsUser(self, value):
        """
        Set the value of the AsUser input for this Choreo. ((optional, string) The ID of the user. Only used for enterprise administrators to make API calls for their managed users.)
        """
        super(UpdateCollaborationInputSet, self)._set_input('AsUser', value)
    def set_CollaborationID(self, value):
        """
        Set the value of the CollaborationID input for this Choreo. ((required, string) The id of the collaboration to edit.)
        """
        super(UpdateCollaborationInputSet, self)._set_input('CollaborationID', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) A comma-separated list of fields to include in the response.)
        """
        super(UpdateCollaborationInputSet, self)._set_input('Fields', value)
    def set_Role(self, value):
        """
        Set the value of the Role input for this Choreo. ((conditional, string) The access level of the collaboration. Valid values are "viewer" or "editor". Defaults to "viewer". This value can only be updated by the owner of the folder.)
        """
        super(UpdateCollaborationInputSet, self)._set_input('Role', value)
    def set_Status(self, value):
        """
        Set the value of the Status input for this Choreo. ((conditional, string) Whether this collaboration has been accepted. Valid values are: "accepted" or "rejected". This value can only be updated by the user who has been invited to the collaboration.)
        """
        super(UpdateCollaborationInputSet, self)._set_input('Status', value)


class UpdateCollaborationResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateCollaboration Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Box.)
        """
        return self._output.get('Response', None)

class UpdateCollaborationChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateCollaborationResultSet(response, path)
