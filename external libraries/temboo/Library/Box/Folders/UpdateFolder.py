# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateFolder
# Updates the information about a folder.
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

class UpdateFolder(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateFolder Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateFolder, self).__init__(temboo_session, '/Library/Box/Folders/UpdateFolder')


    def new_input_set(self):
        return UpdateFolderInputSet()

    def _make_result_set(self, result, path):
        return UpdateFolderResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateFolderChoreographyExecution(session, exec_id, path)

class UpdateFolderInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateFolder
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_FolderObject(self, value):
        """
        Set the value of the FolderObject input for this Choreo. ((required, json) A JSON object representing the new folder information. See documentation for formatting examples.)
        """
        super(UpdateFolderInputSet, self)._set_input('FolderObject', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved during the OAuth2 process.)
        """
        super(UpdateFolderInputSet, self)._set_input('AccessToken', value)
    def set_AsUser(self, value):
        """
        Set the value of the AsUser input for this Choreo. ((optional, string) The ID of the user. Only used for enterprise administrators to make API calls for their managed users.)
        """
        super(UpdateFolderInputSet, self)._set_input('AsUser', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) A comma-separated list of fields to include in the response.)
        """
        super(UpdateFolderInputSet, self)._set_input('Fields', value)
    def set_FolderID(self, value):
        """
        Set the value of the FolderID input for this Choreo. ((required, string) The id of the folder to update.)
        """
        super(UpdateFolderInputSet, self)._set_input('FolderID', value)

class UpdateFolderResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateFolder Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Box.)
        """
        return self._output.get('Response', None)

class UpdateFolderChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateFolderResultSet(response, path)
