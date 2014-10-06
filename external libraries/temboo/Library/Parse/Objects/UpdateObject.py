# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateObject
# Updates an existing object.
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

class UpdateObject(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateObject Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdateObject, self).__init__(temboo_session, '/Library/Parse/Objects/UpdateObject')


    def new_input_set(self):
        return UpdateObjectInputSet()

    def _make_result_set(self, result, path):
        return UpdateObjectResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateObjectChoreographyExecution(session, exec_id, path)

class UpdateObjectInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateObject
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ObjectContents(self, value):
        """
        Set the value of the ObjectContents input for this Choreo. ((required, json) A JSON string containing the object contents.)
        """
        super(UpdateObjectInputSet, self)._set_input('ObjectContents', value)
    def set_ApplicationID(self, value):
        """
        Set the value of the ApplicationID input for this Choreo. ((required, string) The Application ID provided by Parse.)
        """
        super(UpdateObjectInputSet, self)._set_input('ApplicationID', value)
    def set_ClassName(self, value):
        """
        Set the value of the ClassName input for this Choreo. ((required, string) The class name for the object being updated.)
        """
        super(UpdateObjectInputSet, self)._set_input('ClassName', value)
    def set_ObjectID(self, value):
        """
        Set the value of the ObjectID input for this Choreo. ((required, string) The ID of the object to update.)
        """
        super(UpdateObjectInputSet, self)._set_input('ObjectID', value)
    def set_RESTAPIKey(self, value):
        """
        Set the value of the RESTAPIKey input for this Choreo. ((required, string) The REST API Key provided by Parse.)
        """
        super(UpdateObjectInputSet, self)._set_input('RESTAPIKey', value)

class UpdateObjectResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateObject Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Parse.)
        """
        return self._output.get('Response', None)

class UpdateObjectChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdateObjectResultSet(response, path)
