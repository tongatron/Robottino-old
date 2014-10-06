# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateDocument
# Updates a specific document within a collection.
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

class UpdateDocument(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateDocument Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateDocument, self).__init__(temboo_session, '/Library/MongoHQ/Documents/UpdateDocument')


    def new_input_set(self):
        return UpdateDocumentInputSet()

    def _make_result_set(self, result, path):
        return UpdateDocumentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateDocumentChoreographyExecution(session, exec_id, path)

class UpdateDocumentInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateDocument
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Document(self, value):
        """
        Set the value of the Document input for this Choreo. ((required, json) The JSON document update command. This accepts standard MongoDB syntax such as $set or $inc.)
        """
        super(UpdateDocumentInputSet, self)._set_input('Document', value)
    def set_APIToken(self, value):
        """
        Set the value of the APIToken input for this Choreo. ((required, string) The API Token provided by MongoHQ.)
        """
        super(UpdateDocumentInputSet, self)._set_input('APIToken', value)
    def set_CollectionName(self, value):
        """
        Set the value of the CollectionName input for this Choreo. ((required, string) The name of the collection associated with the document being updated.)
        """
        super(UpdateDocumentInputSet, self)._set_input('CollectionName', value)
    def set_DatabaseName(self, value):
        """
        Set the value of the DatabaseName input for this Choreo. ((required, string) The name of the database associated with the document being updated.)
        """
        super(UpdateDocumentInputSet, self)._set_input('DatabaseName', value)
    def set_DocumentID(self, value):
        """
        Set the value of the DocumentID input for this Choreo. ((required, string) The ID of the document being updated.)
        """
        super(UpdateDocumentInputSet, self)._set_input('DocumentID', value)
    def set_Safe(self, value):
        """
        Set the value of the Safe input for this Choreo. ((optional, boolean) When set to true, the operation will wait until the document is saved before returning. When set to false (the default) documents are saved asynchronously.)
        """
        super(UpdateDocumentInputSet, self)._set_input('Safe', value)

class UpdateDocumentResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateDocument Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from MongoHQ.)
        """
        return self._output.get('Response', None)

class UpdateDocumentChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateDocumentResultSet(response, path)
