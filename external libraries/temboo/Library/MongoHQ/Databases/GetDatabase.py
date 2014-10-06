# -*- coding: utf-8 -*-

###############################################################################
#
# GetDatabase
# Retrieves information about a specified database.
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

class GetDatabase(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetDatabase Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetDatabase, self).__init__(temboo_session, '/Library/MongoHQ/Databases/GetDatabase')


    def new_input_set(self):
        return GetDatabaseInputSet()

    def _make_result_set(self, result, path):
        return GetDatabaseResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetDatabaseChoreographyExecution(session, exec_id, path)

class GetDatabaseInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetDatabase
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIToken(self, value):
        """
        Set the value of the APIToken input for this Choreo. ((required, string) The API Token provided by MongoHQ.)
        """
        super(GetDatabaseInputSet, self)._set_input('APIToken', value)
    def set_DatabaseName(self, value):
        """
        Set the value of the DatabaseName input for this Choreo. ((required, string) The name of the database to retrieve.)
        """
        super(GetDatabaseInputSet, self)._set_input('DatabaseName', value)

class GetDatabaseResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetDatabase Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from MongoHQ.)
        """
        return self._output.get('Response', None)

class GetDatabaseChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetDatabaseResultSet(response, path)
