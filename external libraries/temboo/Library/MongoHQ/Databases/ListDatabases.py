# -*- coding: utf-8 -*-

###############################################################################
#
# ListDatabases
# Retrieves a list of all databases in your account.
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

class ListDatabases(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListDatabases Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListDatabases, self).__init__(temboo_session, '/Library/MongoHQ/Databases/ListDatabases')


    def new_input_set(self):
        return ListDatabasesInputSet()

    def _make_result_set(self, result, path):
        return ListDatabasesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListDatabasesChoreographyExecution(session, exec_id, path)

class ListDatabasesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListDatabases
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIToken(self, value):
        """
        Set the value of the APIToken input for this Choreo. ((required, string) The API Token provided by MongoHQ.)
        """
        super(ListDatabasesInputSet, self)._set_input('APIToken', value)

class ListDatabasesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListDatabases Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from MongoHQ.)
        """
        return self._output.get('Response', None)

class ListDatabasesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListDatabasesResultSet(response, path)
