# -*- coding: utf-8 -*-

###############################################################################
#
# Substitute
# Replaces all instances of the specified sub-string within the specified text with a new sub-string. 
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

class Substitute(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Substitute Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Substitute, self).__init__(temboo_session, '/Library/Utilities/Text/Substitute')


    def new_input_set(self):
        return SubstituteInputSet()

    def _make_result_set(self, result, path):
        return SubstituteResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SubstituteChoreographyExecution(session, exec_id, path)

class SubstituteInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Substitute
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_New(self, value):
        """
        Set the value of the New input for this Choreo. ((required, string) New sub-string to replace with.)
        """
        super(SubstituteInputSet, self)._set_input('New', value)
    def set_Old(self, value):
        """
        Set the value of the Old input for this Choreo. ((required, string) Old sub-string to replace.)
        """
        super(SubstituteInputSet, self)._set_input('Old', value)
    def set_Text(self, value):
        """
        Set the value of the Text input for this Choreo. ((required, string) Text to peform substitution.)
        """
        super(SubstituteInputSet, self)._set_input('Text', value)

class SubstituteResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Substitute Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((string) The result after the substitution.)
        """
        return self._output.get('Response', None)

class SubstituteChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SubstituteResultSet(response, path)
