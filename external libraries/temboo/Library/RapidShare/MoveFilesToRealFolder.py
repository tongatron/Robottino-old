# -*- coding: utf-8 -*-

###############################################################################
#
# MoveFilesToRealFolder
# Move an existing file to a new folder in RapidShare.
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

class MoveFilesToRealFolder(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the MoveFilesToRealFolder Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(MoveFilesToRealFolder, self).__init__(temboo_session, '/Library/RapidShare/MoveFilesToRealFolder')


    def new_input_set(self):
        return MoveFilesToRealFolderInputSet()

    def _make_result_set(self, result, path):
        return MoveFilesToRealFolderResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return MoveFilesToRealFolderChoreographyExecution(session, exec_id, path)

class MoveFilesToRealFolderInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the MoveFilesToRealFolder
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Files(self, value):
        """
        Set the value of the Files input for this Choreo. ((required, integer) The id of the file to move. Can be a commas separated list of ids.)
        """
        super(MoveFilesToRealFolderInputSet, self)._set_input('Files', value)
    def set_Login(self, value):
        """
        Set the value of the Login input for this Choreo. ((required, string) Your RapidShare username)
        """
        super(MoveFilesToRealFolderInputSet, self)._set_input('Login', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your RapidShare password)
        """
        super(MoveFilesToRealFolderInputSet, self)._set_input('Password', value)
    def set_RealFolder(self, value):
        """
        Set the value of the RealFolder input for this Choreo. ((optional, integer) The ID of the parent folder. Defaults to 0 for 'root'.)
        """
        super(MoveFilesToRealFolderInputSet, self)._set_input('RealFolder', value)

class MoveFilesToRealFolderResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the MoveFilesToRealFolder Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((string) The response from RapidShare. The id of the newly created folder should be returned in the response upon a successful execution.)
        """
        return self._output.get('Response', None)

class MoveFilesToRealFolderChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return MoveFilesToRealFolderResultSet(response, path)
