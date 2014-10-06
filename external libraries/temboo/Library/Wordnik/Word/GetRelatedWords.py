# -*- coding: utf-8 -*-

###############################################################################
#
# GetRelatedWords
# Retrieves the related words of a given word.
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

class GetRelatedWords(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetRelatedWords Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetRelatedWords, self).__init__(temboo_session, '/Library/Wordnik/Word/GetRelatedWords')


    def new_input_set(self):
        return GetRelatedWordsInputSet()

    def _make_result_set(self, result, path):
        return GetRelatedWordsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetRelatedWordsChoreographyExecution(session, exec_id, path)

class GetRelatedWordsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetRelatedWords
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key from Wordnik.)
        """
        super(GetRelatedWordsInputSet, self)._set_input('APIKey', value)
    def set_Cannonical(self, value):
        """
        Set the value of the Cannonical input for this Choreo. ((optional, string) Deprecated (retained for backward compatibility only).)
        """
        super(GetRelatedWordsInputSet, self)._set_input('Cannonical', value)
    def set_LimitPerType(self, value):
        """
        Set the value of the LimitPerType input for this Choreo. ((optional, integer) Limits the amount of results returned for each relationship type included in the output. Defaults to 10.)
        """
        super(GetRelatedWordsInputSet, self)._set_input('LimitPerType', value)
    def set_RelationshipType(self, value):
        """
        Set the value of the RelationshipType input for this Choreo. ((optional, string) Limits the total results per type of relationship. Acceptable values inlcude adjective, noun, etc. See docs for complete list.)
        """
        super(GetRelatedWordsInputSet, self)._set_input('RelationshipType', value)
    def set_ResponseType(self, value):
        """
        Set the value of the ResponseType input for this Choreo. ((optional, string) Response can be either JSON or XML. Defaults to JSON.)
        """
        super(GetRelatedWordsInputSet, self)._set_input('ResponseType', value)
    def set_UseCanonical(self, value):
        """
        Set the value of the UseCanonical input for this Choreo. ((optional, boolean) If true will try to return the correct word root ('cats' -> 'cat'). If false returns exactly what was requested. Defaults to false.)
        """
        super(GetRelatedWordsInputSet, self)._set_input('UseCanonical', value)
    def set_Word(self, value):
        """
        Set the value of the Word input for this Choreo. ((required, string) The word you want to look up on Wordnik.)
        """
        super(GetRelatedWordsInputSet, self)._set_input('Word', value)

class GetRelatedWordsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetRelatedWords Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Wordnik.)
        """
        return self._output.get('Response', None)

class GetRelatedWordsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetRelatedWordsResultSet(response, path)
