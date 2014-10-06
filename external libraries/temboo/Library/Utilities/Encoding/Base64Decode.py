# -*- coding: utf-8 -*-

###############################################################################
#
# Base64Decode
# Returns the specified Base64 encoded string as decoded text.
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

class Base64Decode(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Base64Decode Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Base64Decode, self).__init__(temboo_session, '/Library/Utilities/Encoding/Base64Decode')


    def new_input_set(self):
        return Base64DecodeInputSet()

    def _make_result_set(self, result, path):
        return Base64DecodeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return Base64DecodeChoreographyExecution(session, exec_id, path)

class Base64DecodeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Base64Decode
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Base64EncodedText(self, value):
        """
        Set the value of the Base64EncodedText input for this Choreo. ((required, string) The Base64 encoded text to decode. Note that Base64 encoded binary data is not allowed.)
        """
        super(Base64DecodeInputSet, self)._set_input('Base64EncodedText', value)

class Base64DecodeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Base64Decode Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Text(self):
        """
        Retrieve the value for the "Text" output from this Choreo execution. ((string) The decoded text.)
        """
        return self._output.get('Text', None)

class Base64DecodeChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return Base64DecodeResultSet(response, path)
