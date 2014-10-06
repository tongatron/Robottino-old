# -*- coding: utf-8 -*-

###############################################################################
#
# SubstituteRegex
# Finds all instances of the specified regular expression pattern within the given string and passes the specified new sub-string to the result variable. 
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

class SubstituteRegex(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SubstituteRegex Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(SubstituteRegex, self).__init__(temboo_session, '/Library/Utilities/Text/SubstituteRegex')


    def new_input_set(self):
        return SubstituteRegexInputSet()

    def _make_result_set(self, result, path):
        return SubstituteRegexResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SubstituteRegexChoreographyExecution(session, exec_id, path)

class SubstituteRegexInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SubstituteRegex
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_New(self, value):
        """
        Set the value of the New input for this Choreo. ((required, string) New sub-string to replace with.)
        """
        super(SubstituteRegexInputSet, self)._set_input('New', value)
    def set_Pattern(self, value):
        """
        Set the value of the Pattern input for this Choreo. ((required, string) Regex pattern to use.)
        """
        super(SubstituteRegexInputSet, self)._set_input('Pattern', value)
    def set_Text(self, value):
        """
        Set the value of the Text input for this Choreo. ((required, string) Text to peform substitution.)
        """
        super(SubstituteRegexInputSet, self)._set_input('Text', value)

class SubstituteRegexResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SubstituteRegex Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((string) The result after the substitution.)
        """
        return self._output.get('Response', None)

class SubstituteRegexChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SubstituteRegexResultSet(response, path)
