# -*- coding: utf-8 -*-

###############################################################################
#
# BulkUpdate
# Updates multiple documents by criteria.
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

class BulkUpdate(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the BulkUpdate Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(BulkUpdate, self).__init__(temboo_session, '/Library/MongoHQ/Documents/BulkUpdate')


    def new_input_set(self):
        return BulkUpdateInputSet()

    def _make_result_set(self, result, path):
        return BulkUpdateResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return BulkUpdateChoreographyExecution(session, exec_id, path)

class BulkUpdateInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the BulkUpdate
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Object(self, value):
        """
        Set the value of the Object input for this Choreo. ((required, json) The JSON document update command. This accepts standard MongoDB syntax such as $set or $inc.)
        """
        super(BulkUpdateInputSet, self)._set_input('Object', value)
    def set_APIToken(self, value):
        """
        Set the value of the APIToken input for this Choreo. ((required, string) The API Token provided by MongoHQ.)
        """
        super(BulkUpdateInputSet, self)._set_input('APIToken', value)
    def set_CollectionName(self, value):
        """
        Set the value of the CollectionName input for this Choreo. ((required, string) The name of the collection associated with the document being updated.)
        """
        super(BulkUpdateInputSet, self)._set_input('CollectionName', value)
    def set_Criteria(self, value):
        """
        Set the value of the Criteria input for this Choreo. ((required, json) The JSON criteria used to match which documents will be updated.)
        """
        super(BulkUpdateInputSet, self)._set_input('Criteria', value)
    def set_DatabaseName(self, value):
        """
        Set the value of the DatabaseName input for this Choreo. ((required, string) The name of the database associated with the document being updated.)
        """
        super(BulkUpdateInputSet, self)._set_input('DatabaseName', value)
    def set_Multiple(self, value):
        """
        Set the value of the Multiple input for this Choreo. ((optional, boolean) Indicates that all documents matching the criteria should be updated. Setting to false (the default) will update just one.)
        """
        super(BulkUpdateInputSet, self)._set_input('Multiple', value)
    def set_Safe(self, value):
        """
        Set the value of the Safe input for this Choreo. ((optional, boolean) When set to true, the operation will wait until the document is saved before returning. When set to false (the default) documents are saved asynchronously.)
        """
        super(BulkUpdateInputSet, self)._set_input('Safe', value)
    def set_Upsert(self, value):
        """
        Set the value of the Upsert input for this Choreo. ((optional, boolean) Indicates that the operation will create records that do not already exist. Set to true to enable this feature. Defaults to false.)
        """
        super(BulkUpdateInputSet, self)._set_input('Upsert', value)

class BulkUpdateResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the BulkUpdate Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from MongoHQ.)
        """
        return self._output.get('Response', None)

class BulkUpdateChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return BulkUpdateResultSet(response, path)
