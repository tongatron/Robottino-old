# -*- coding: utf-8 -*-

###############################################################################
#
# ViewAccountProfile
# Display account profile information.
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

class ViewAccountProfile(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ViewAccountProfile Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ViewAccountProfile, self).__init__(temboo_session, '/Library/SendGrid/WebAPI/Profile/ViewAccountProfile')


    def new_input_set(self):
        return ViewAccountProfileInputSet()

    def _make_result_set(self, result, path):
        return ViewAccountProfileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ViewAccountProfileChoreographyExecution(session, exec_id, path)

class ViewAccountProfileInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ViewAccountProfile
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key obtained from SendGrid.)
        """
        super(ViewAccountProfileInputSet, self)._set_input('APIKey', value)
    def set_APIUser(self, value):
        """
        Set the value of the APIUser input for this Choreo. ((required, string) The username registered with SendGrid.)
        """
        super(ViewAccountProfileInputSet, self)._set_input('APIUser', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format of the response from SendGrid, in either json, or xml.  Default is set to json.)
        """
        super(ViewAccountProfileInputSet, self)._set_input('ResponseFormat', value)


class ViewAccountProfileResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ViewAccountProfile Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from SendGrid. The format corresponds to the ResponseFormat input. Default is json.)
        """
        return self._output.get('Response', None)

class ViewAccountProfileChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ViewAccountProfileResultSet(response, path)
