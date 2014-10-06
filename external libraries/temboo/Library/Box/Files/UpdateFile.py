# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateFile
# Updates individual or multiple fields in the file object.
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

class UpdateFile(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateFile Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateFile, self).__init__(temboo_session, '/Library/Box/Files/UpdateFile')


    def new_input_set(self):
        return UpdateFileInputSet()

    def _make_result_set(self, result, path):
        return UpdateFileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateFileChoreographyExecution(session, exec_id, path)

class UpdateFileInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateFile
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_FileObject(self, value):
        """
        Set the value of the FileObject input for this Choreo. ((required, json) A JSON object representing the new file information. See documentation for formatting examples.)
        """
        super(UpdateFileInputSet, self)._set_input('FileObject', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved during the OAuth2 process.)
        """
        super(UpdateFileInputSet, self)._set_input('AccessToken', value)
    def set_AsUser(self, value):
        """
        Set the value of the AsUser input for this Choreo. ((optional, string) The ID of the user. Only used for enterprise administrators to make API calls for their managed users.)
        """
        super(UpdateFileInputSet, self)._set_input('AsUser', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) A comma-separated list of fields to include in the response.)
        """
        super(UpdateFileInputSet, self)._set_input('Fields', value)
    def set_FileID(self, value):
        """
        Set the value of the FileID input for this Choreo. ((required, string) The id of the file to update.)
        """
        super(UpdateFileInputSet, self)._set_input('FileID', value)

class UpdateFileResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateFile Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Box.)
        """
        return self._output.get('Response', None)

class UpdateFileChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateFileResultSet(response, path)
