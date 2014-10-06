# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteFiles
# Delete one or more files from RapidShare.
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

class DeleteFiles(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteFiles Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DeleteFiles, self).__init__(temboo_session, '/Library/RapidShare/DeleteFiles')


    def new_input_set(self):
        return DeleteFilesInputSet()

    def _make_result_set(self, result, path):
        return DeleteFilesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteFilesChoreographyExecution(session, exec_id, path)

class DeleteFilesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteFiles
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_File(self, value):
        """
        Set the value of the File input for this Choreo. ((required, integer) The id of the file to delete. Can be a commas separated list of ids.)
        """
        super(DeleteFilesInputSet, self)._set_input('File', value)
    def set_Login(self, value):
        """
        Set the value of the Login input for this Choreo. ((required, string) Your RapidShare username)
        """
        super(DeleteFilesInputSet, self)._set_input('Login', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your RapidShare password)
        """
        super(DeleteFilesInputSet, self)._set_input('Password', value)

class DeleteFilesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteFiles Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((string) The response from RapidShare)
        """
        return self._output.get('Response', None)

class DeleteFilesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeleteFilesResultSet(response, path)
