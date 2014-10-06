# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteAllIndexes
# Deletes all indexes within a collection.
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

class DeleteAllIndexes(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteAllIndexes Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DeleteAllIndexes, self).__init__(temboo_session, '/Library/MongoHQ/Indexes/DeleteAllIndexes')


    def new_input_set(self):
        return DeleteAllIndexesInputSet()

    def _make_result_set(self, result, path):
        return DeleteAllIndexesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteAllIndexesChoreographyExecution(session, exec_id, path)

class DeleteAllIndexesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteAllIndexes
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIToken(self, value):
        """
        Set the value of the APIToken input for this Choreo. ((required, string) The API Token provided by MongoHQ.)
        """
        super(DeleteAllIndexesInputSet, self)._set_input('APIToken', value)
    def set_CollectionName(self, value):
        """
        Set the value of the CollectionName input for this Choreo. ((required, string) The name of the collection associated with the indexes to delete.)
        """
        super(DeleteAllIndexesInputSet, self)._set_input('CollectionName', value)
    def set_DatabaseName(self, value):
        """
        Set the value of the DatabaseName input for this Choreo. ((required, string) The name of the database associated with the indexes to delete.)
        """
        super(DeleteAllIndexesInputSet, self)._set_input('DatabaseName', value)

class DeleteAllIndexesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteAllIndexes Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from MongoHQ.)
        """
        return self._output.get('Response', None)

class DeleteAllIndexesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeleteAllIndexesResultSet(response, path)
