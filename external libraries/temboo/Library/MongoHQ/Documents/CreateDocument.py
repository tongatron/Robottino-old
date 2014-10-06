# -*- coding: utf-8 -*-

###############################################################################
#
# CreateDocument
# Creates a new document within a collection.
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

class CreateDocument(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateDocument Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateDocument, self).__init__(temboo_session, '/Library/MongoHQ/Documents/CreateDocument')


    def new_input_set(self):
        return CreateDocumentInputSet()

    def _make_result_set(self, result, path):
        return CreateDocumentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateDocumentChoreographyExecution(session, exec_id, path)

class CreateDocumentInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateDocument
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Document(self, value):
        """
        Set the value of the Document input for this Choreo. ((required, json) The JSON document to be created under the collection.)
        """
        super(CreateDocumentInputSet, self)._set_input('Document', value)
    def set_APIToken(self, value):
        """
        Set the value of the APIToken input for this Choreo. ((required, string) The API Token provided by MongoHQ.)
        """
        super(CreateDocumentInputSet, self)._set_input('APIToken', value)
    def set_CollectionName(self, value):
        """
        Set the value of the CollectionName input for this Choreo. ((required, string) The name of the collection associated with the new document.)
        """
        super(CreateDocumentInputSet, self)._set_input('CollectionName', value)
    def set_DatabaseName(self, value):
        """
        Set the value of the DatabaseName input for this Choreo. ((required, string) The name of the database associated with the new document.)
        """
        super(CreateDocumentInputSet, self)._set_input('DatabaseName', value)
    def set_Safe(self, value):
        """
        Set the value of the Safe input for this Choreo. ((optional, boolean) When set to true, the operation will wait until the document is saved before returning. When set to false (the default) documents are saved asynchronously.)
        """
        super(CreateDocumentInputSet, self)._set_input('Safe', value)

class CreateDocumentResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateDocument Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from MongoHQ.)
        """
        return self._output.get('Response', None)

class CreateDocumentChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateDocumentResultSet(response, path)
