# -*- coding: utf-8 -*-

###############################################################################
#
# GetTopExample
# Retrieves the top example of a given word.
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

class GetTopExample(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetTopExample Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetTopExample, self).__init__(temboo_session, '/Library/Wordnik/Word/GetTopExample')


    def new_input_set(self):
        return GetTopExampleInputSet()

    def _make_result_set(self, result, path):
        return GetTopExampleResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTopExampleChoreographyExecution(session, exec_id, path)

class GetTopExampleInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetTopExample
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key from Wordnik.)
        """
        super(GetTopExampleInputSet, self)._set_input('APIKey', value)
    def set_Cannonical(self, value):
        """
        Set the value of the Cannonical input for this Choreo. ((optional, string) Deprecated (retained for backward compatibility only).)
        """
        super(GetTopExampleInputSet, self)._set_input('Cannonical', value)
    def set_ResponseType(self, value):
        """
        Set the value of the ResponseType input for this Choreo. ((optional, string) Response can be either JSON or XML. Defaults to JSON.)
        """
        super(GetTopExampleInputSet, self)._set_input('ResponseType', value)
    def set_UseCanonical(self, value):
        """
        Set the value of the UseCanonical input for this Choreo. ((optional, boolean) If true will try to return the correct word root ('cats' -> 'cat'). If false returns exactly what was requested. Defaults to false.)
        """
        super(GetTopExampleInputSet, self)._set_input('UseCanonical', value)
    def set_Word(self, value):
        """
        Set the value of the Word input for this Choreo. ((required, string) The word you want to look up on Wordnik.)
        """
        super(GetTopExampleInputSet, self)._set_input('Word', value)

class GetTopExampleResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetTopExample Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Wordnik.)
        """
        return self._output.get('Response', None)

class GetTopExampleChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetTopExampleResultSet(response, path)
