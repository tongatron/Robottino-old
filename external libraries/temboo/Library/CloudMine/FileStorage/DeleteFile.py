# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteFile
# Deletes one or more files from the CloudMine server using the keys provided.
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

class DeleteFile(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteFile Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DeleteFile, self).__init__(temboo_session, '/Library/CloudMine/FileStorage/DeleteFile')


    def new_input_set(self):
        return DeleteFileInputSet()

    def _make_result_set(self, result, path):
        return DeleteFileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteFileChoreographyExecution(session, exec_id, path)

class DeleteFileInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteFile
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by CloudMine after registering your app.)
        """
        super(DeleteFileInputSet, self)._set_input('APIKey', value)
    def set_ApplicationIdentifier(self, value):
        """
        Set the value of the ApplicationIdentifier input for this Choreo. ((required, string) The application identifier provided by CloudMine after registering your app.)
        """
        super(DeleteFileInputSet, self)._set_input('ApplicationIdentifier', value)
    def set_Keys(self, value):
        """
        Set the value of the Keys input for this Choreo. ((required, string) A comma-separated list of keys to delete.)
        """
        super(DeleteFileInputSet, self)._set_input('Keys', value)
    def set_SessionToken(self, value):
        """
        Set the value of the SessionToken input for this Choreo. ((conditional, string) The session token for an existing user (returned by the AccountLogin Choreo). This is only required if your app is performing this operation on behalf of another user.)
        """
        super(DeleteFileInputSet, self)._set_input('SessionToken', value)


class DeleteFileResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteFile Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from CloudMine.)
        """
        return self._output.get('Response', None)

class DeleteFileChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeleteFileResultSet(response, path)
