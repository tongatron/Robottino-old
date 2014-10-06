# -*- coding: utf-8 -*-

###############################################################################
#
# GetLanguagesForTranslate
# Retrieves a list of language codes representing languages that are supported by the Translation Service.
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

class GetLanguagesForTranslate(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetLanguagesForTranslate Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetLanguagesForTranslate, self).__init__(temboo_session, '/Library/Microsoft/Translator/GetLanguagesForTranslate')


    def new_input_set(self):
        return GetLanguagesForTranslateInputSet()

    def _make_result_set(self, result, path):
        return GetLanguagesForTranslateResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetLanguagesForTranslateChoreographyExecution(session, exec_id, path)

class GetLanguagesForTranslateInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetLanguagesForTranslate
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token. This can be retrieved by running the GetToken Choreo. Required unless providing the ClientID and ClientSecret.)
        """
        super(GetLanguagesForTranslateInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID obtained when signing up for Microsoft Translator on Azure Marketplace. This is required unless providing an AccessToken.)
        """
        super(GetLanguagesForTranslateInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret obtained when signing up for Microsoft Translator on Azure Marketplace. This is required unless providing an AccessToken.)
        """
        super(GetLanguagesForTranslateInputSet, self)._set_input('ClientSecret', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(GetLanguagesForTranslateInputSet, self)._set_input('ResponseFormat', value)

class GetLanguagesForTranslateResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetLanguagesForTranslate Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Microsoft.)
        """
        return self._output.get('Response', None)
    def get_ExpiresIn(self):
        """
        Retrieve the value for the "ExpiresIn" output from this Choreo execution. ((integer) Contains the number of seconds for which the access token is valid when ClientID and ClientSecret are provided.)
        """
        return self._output.get('ExpiresIn', None)
    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) Contains a new AccessToken when the ClientID and ClientSecret are provided.)
        """
        return self._output.get('NewAccessToken', None)

class GetLanguagesForTranslateChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetLanguagesForTranslateResultSet(response, path)
