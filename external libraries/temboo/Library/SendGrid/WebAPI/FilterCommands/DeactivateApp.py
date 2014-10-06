# -*- coding: utf-8 -*-

###############################################################################
#
# DeactivateApp
# Deactivate an app.
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

class DeactivateApp(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeactivateApp Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DeactivateApp, self).__init__(temboo_session, '/Library/SendGrid/WebAPI/FilterCommands/DeactivateApp')


    def new_input_set(self):
        return DeactivateAppInputSet()

    def _make_result_set(self, result, path):
        return DeactivateAppResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeactivateAppChoreographyExecution(session, exec_id, path)

class DeactivateAppInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeactivateApp
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key obtained from SendGrid.)
        """
        super(DeactivateAppInputSet, self)._set_input('APIKey', value)
    def set_APIUser(self, value):
        """
        Set the value of the APIUser input for this Choreo. ((required, string) The username registered with SendGrid.)
        """
        super(DeactivateAppInputSet, self)._set_input('APIUser', value)
    def set_AppName(self, value):
        """
        Set the value of the AppName input for this Choreo. ((required, string) The name of the app to be activated.  A list of available apps can be obtained by running the ListAvailableApps Choreo.)
        """
        super(DeactivateAppInputSet, self)._set_input('AppName', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format of the response from SendGrid, in either json, or xml.  Default is set to json.)
        """
        super(DeactivateAppInputSet, self)._set_input('ResponseFormat', value)


class DeactivateAppResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeactivateApp Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from SendGrid. The format corresponds to the ResponseFormat input. Default is json.)
        """
        return self._output.get('Response', None)

class DeactivateAppChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeactivateAppResultSet(response, path)
