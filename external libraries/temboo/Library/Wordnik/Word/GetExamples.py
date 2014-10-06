# -*- coding: utf-8 -*-

###############################################################################
#
# GetExamples
# Retrieves the examples of a given word.
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

class GetExamples(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetExamples Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetExamples, self).__init__(temboo_session, '/Library/Wordnik/Word/GetExamples')


    def new_input_set(self):
        return GetExamplesInputSet()

    def _make_result_set(self, result, path):
        return GetExamplesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetExamplesChoreographyExecution(session, exec_id, path)

class GetExamplesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetExamples
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key from Wordnik.)
        """
        super(GetExamplesInputSet, self)._set_input('APIKey', value)
    def set_Cannonical(self, value):
        """
        Set the value of the Cannonical input for this Choreo. ((optional, string) Deprecated (retained for backward compatibility only).)
        """
        super(GetExamplesInputSet, self)._set_input('Cannonical', value)
    def set_Duplicates(self, value):
        """
        Set the value of the Duplicates input for this Choreo. ((optional, string) Shows duplicate examples from different sources when set to true. Defaults to false.)
        """
        super(GetExamplesInputSet, self)._set_input('Duplicates', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Maximum number of results to return.)
        """
        super(GetExamplesInputSet, self)._set_input('Limit', value)
    def set_ResponseType(self, value):
        """
        Set the value of the ResponseType input for this Choreo. ((optional, string) Response can be either JSON or XML. Defaults to JSON.)
        """
        super(GetExamplesInputSet, self)._set_input('ResponseType', value)
    def set_Skip(self, value):
        """
        Set the value of the Skip input for this Choreo. ((optional, integer) Results to skip. Defaults to 0.)
        """
        super(GetExamplesInputSet, self)._set_input('Skip', value)
    def set_UseCanonical(self, value):
        """
        Set the value of the UseCanonical input for this Choreo. ((optional, boolean) If true will try to return the correct word root ('cats' -> 'cat'). If false returns exactly what was requested. Defaults to false.)
        """
        super(GetExamplesInputSet, self)._set_input('UseCanonical', value)
    def set_Word(self, value):
        """
        Set the value of the Word input for this Choreo. ((required, string) The word you want to look up on Wordnik.)
        """
        super(GetExamplesInputSet, self)._set_input('Word', value)

class GetExamplesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetExamples Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Wordnik.)
        """
        return self._output.get('Response', None)

class GetExamplesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetExamplesResultSet(response, path)
