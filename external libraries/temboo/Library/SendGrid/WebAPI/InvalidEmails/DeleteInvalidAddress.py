# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteInvalidAddress
# Delete an address from the Invalid Email list.
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

class DeleteInvalidAddress(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteInvalidAddress Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DeleteInvalidAddress, self).__init__(temboo_session, '/Library/SendGrid/WebAPI/InvalidEmails/DeleteInvalidAddress')


    def new_input_set(self):
        return DeleteInvalidAddressInputSet()

    def _make_result_set(self, result, path):
        return DeleteInvalidAddressResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteInvalidAddressChoreographyExecution(session, exec_id, path)

class DeleteInvalidAddressInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteInvalidAddress
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key obtained from SendGrid.)
        """
        super(DeleteInvalidAddressInputSet, self)._set_input('APIKey', value)
    def set_APIUser(self, value):
        """
        Set the value of the APIUser input for this Choreo. ((required, string) The username registered with SendGrid.)
        """
        super(DeleteInvalidAddressInputSet, self)._set_input('APIUser', value)
    def set_EmailAddressToDelete(self, value):
        """
        Set the value of the EmailAddressToDelete input for this Choreo. ((required, string) The email address that is to be deleted.)
        """
        super(DeleteInvalidAddressInputSet, self)._set_input('EmailAddressToDelete', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format of the response from SendGrid, in either json, or xml.  Default is set to json.)
        """
        super(DeleteInvalidAddressInputSet, self)._set_input('ResponseFormat', value)


class DeleteInvalidAddressResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteInvalidAddress Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from SendGrid. The format corresponds to the ResponseFormat input. Default is json.)
        """
        return self._output.get('Response', None)

class DeleteInvalidAddressChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeleteInvalidAddressResultSet(response, path)
