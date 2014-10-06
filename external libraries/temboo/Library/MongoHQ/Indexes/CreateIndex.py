# -*- coding: utf-8 -*-

###############################################################################
#
# CreateIndex
# Create a new index within a collection.
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

class CreateIndex(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateIndex Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateIndex, self).__init__(temboo_session, '/Library/MongoHQ/Indexes/CreateIndex')


    def new_input_set(self):
        return CreateIndexInputSet()

    def _make_result_set(self, result, path):
        return CreateIndexResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateIndexChoreographyExecution(session, exec_id, path)

class CreateIndexInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateIndex
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Specification(self, value):
        """
        Set the value of the Specification input for this Choreo. ((required, json) The index specification to be created (e.g., {"key":1}).)
        """
        super(CreateIndexInputSet, self)._set_input('Specification', value)
    def set_APIToken(self, value):
        """
        Set the value of the APIToken input for this Choreo. ((required, string) The API Token provided by MongoHQ.)
        """
        super(CreateIndexInputSet, self)._set_input('APIToken', value)
    def set_Background(self, value):
        """
        Set the value of the Background input for this Choreo. ((optional, boolean) Indicates that the index will be built in the background. Defaults to true.)
        """
        super(CreateIndexInputSet, self)._set_input('Background', value)
    def set_CollectionName(self, value):
        """
        Set the value of the CollectionName input for this Choreo. ((required, string) The name of the collection associated with the indexes to list.)
        """
        super(CreateIndexInputSet, self)._set_input('CollectionName', value)
    def set_DatabaseName(self, value):
        """
        Set the value of the DatabaseName input for this Choreo. ((required, string) The name of the database associated with the indexes to list.)
        """
        super(CreateIndexInputSet, self)._set_input('DatabaseName', value)
    def set_DropDuplicates(self, value):
        """
        Set the value of the DropDuplicates input for this Choreo. ((optional, boolean) When creating a unique index on a collection with pre-existing records, this flag will keep the first document the database indexes and drop all subsequent with duplicate values. Defaults to false.)
        """
        super(CreateIndexInputSet, self)._set_input('DropDuplicates', value)
    def set_Maximum(self, value):
        """
        Set the value of the Maximum input for this Choreo. ((optional, string) The maximum longitude and latitude for a geo index.)
        """
        super(CreateIndexInputSet, self)._set_input('Maximum', value)
    def set_Minimum(self, value):
        """
        Set the value of the Minimum input for this Choreo. ((optional, string) The minimum longitude and latitude for a geo index.)
        """
        super(CreateIndexInputSet, self)._set_input('Minimum', value)
    def set_Unique(self, value):
        """
        Set the value of the Unique input for this Choreo. ((optional, boolean) Indicates that the index should enforce a uniqueness constraint. Defaults to false.)
        """
        super(CreateIndexInputSet, self)._set_input('Unique', value)

class CreateIndexResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateIndex Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from MongoHQ.)
        """
        return self._output.get('Response', None)

class CreateIndexChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateIndexResultSet(response, path)
