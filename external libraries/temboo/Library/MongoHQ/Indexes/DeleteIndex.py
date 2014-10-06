# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteIndex
# Deletes a specified index within a collection.
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

class DeleteIndex(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteIndex Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DeleteIndex, self).__init__(temboo_session, '/Library/MongoHQ/Indexes/DeleteIndex')


    def new_input_set(self):
        return DeleteIndexInputSet()

    def _make_result_set(self, result, path):
        return DeleteIndexResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteIndexChoreographyExecution(session, exec_id, path)

class DeleteIndexInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteIndex
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIToken(self, value):
        """
        Set the value of the APIToken input for this Choreo. ((required, string) The API Token provided by MongoHQ.)
        """
        super(DeleteIndexInputSet, self)._set_input('APIToken', value)
    def set_CollectionName(self, value):
        """
        Set the value of the CollectionName input for this Choreo. ((required, string) The name of the collection associated with the index being deleted.)
        """
        super(DeleteIndexInputSet, self)._set_input('CollectionName', value)
    def set_DatabaseName(self, value):
        """
        Set the value of the DatabaseName input for this Choreo. ((required, string) The name of the database associated with the index being deleted.)
        """
        super(DeleteIndexInputSet, self)._set_input('DatabaseName', value)
    def set_IndexName(self, value):
        """
        Set the value of the IndexName input for this Choreo. ((required, string) The name of the index to delete.)
        """
        super(DeleteIndexInputSet, self)._set_input('IndexName', value)

class DeleteIndexResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteIndex Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from MongoHQ.)
        """
        return self._output.get('Response', None)

class DeleteIndexChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeleteIndexResultSet(response, path)
