# -*- coding: utf-8 -*-

###############################################################################
#
# GetWordList
# Retrieves a word list by its ID.
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

class GetWordList(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetWordList Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetWordList, self).__init__(temboo_session, '/Library/Wordnik/WordList/GetWordList')


    def new_input_set(self):
        return GetWordListInputSet()

    def _make_result_set(self, result, path):
        return GetWordListResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetWordListChoreographyExecution(session, exec_id, path)

class GetWordListInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetWordList
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key obtained from Wordnik.)
        """
        super(GetWordListInputSet, self)._set_input('APIKey', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, string) The Password of the Wordnik account.)
        """
        super(GetWordListInputSet, self)._set_input('Password', value)
    def set_ResponseType(self, value):
        """
        Set the value of the ResponseType input for this Choreo. ((optional, string) Response can be either JSON or XML. Defaults to JSON.)
        """
        super(GetWordListInputSet, self)._set_input('ResponseType', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) The Username of the Wordnik account.)
        """
        super(GetWordListInputSet, self)._set_input('Username', value)
    def set_WordList(self, value):
        """
        Set the value of the WordList input for this Choreo. ((required, string) The perma-link for the Word List to retrieve.)
        """
        super(GetWordListInputSet, self)._set_input('WordList', value)

class GetWordListResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetWordList Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Wordnik.)
        """
        return self._output.get('Response', None)

class GetWordListChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetWordListResultSet(response, path)
