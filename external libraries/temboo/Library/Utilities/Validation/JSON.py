# -*- coding: utf-8 -*-

###############################################################################
#
# JSON
# Determines if a specified JSON string is well-formed.
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

class JSON(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the JSON Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(JSON, self).__init__(temboo_session, '/Library/Utilities/Validation/JSON')


    def new_input_set(self):
        return JSONInputSet()

    def _make_result_set(self, result, path):
        return JSONResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return JSONChoreographyExecution(session, exec_id, path)

class JSONInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the JSON
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_JSON(self, value):
        """
        Set the value of the JSON input for this Choreo. ((required, multiline) The JSON string to validate.)
        """
        super(JSONInputSet, self)._set_input('JSON', value)

class JSONResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the JSON Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Result(self):
        """
        Retrieve the value for the "Result" output from this Choreo execution. ((string) The result of the JSON validation. This will return "valid" or "invalid".)
        """
        return self._output.get('Result', None)

class JSONChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return JSONResultSet(response, path)
