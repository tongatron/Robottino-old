# -*- coding: utf-8 -*-

###############################################################################
#
# TranslateArray
# Translates multiple source texts.
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

class TranslateArray(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the TranslateArray Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(TranslateArray, self).__init__(temboo_session, '/Library/Microsoft/Translator/TranslateArray')


    def new_input_set(self):
        return TranslateArrayInputSet()

    def _make_result_set(self, result, path):
        return TranslateArrayResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TranslateArrayChoreographyExecution(session, exec_id, path)

class TranslateArrayInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the TranslateArray
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token. This can be retrieved by running the GetToken Choreo. Required unless providing the ClientID and ClientSecret.)
        """
        super(TranslateArrayInputSet, self)._set_input('AccessToken', value)
    def set_Category(self, value):
        """
        Set the value of the Category input for this Choreo. ((optional, string) A string containing the category (domain) of the translation. Defaults to "general".)
        """
        super(TranslateArrayInputSet, self)._set_input('Category', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID obtained when signing up for Microsoft Translator on Azure Marketplace. This is required unless providing an AccessToken.)
        """
        super(TranslateArrayInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret obtained when signing up for Microsoft Translator on Azure Marketplace. This is required unless providing an AccessToken.)
        """
        super(TranslateArrayInputSet, self)._set_input('ClientSecret', value)
    def set_ContentType(self, value):
        """
        Set the value of the ContentType input for this Choreo. ((optional, string) The format of the text being translated. The supported formats are "text/plain" (the default) and "text/html".)
        """
        super(TranslateArrayInputSet, self)._set_input('ContentType', value)
    def set_From(self, value):
        """
        Set the value of the From input for this Choreo. ((optional, string) A string representing the language code of the translation text (e.g., en). If not provided auto-detection is used.)
        """
        super(TranslateArrayInputSet, self)._set_input('From', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(TranslateArrayInputSet, self)._set_input('ResponseFormat', value)
    def set_Texts(self, value):
        """
        Set the value of the Texts input for this Choreo. ((required, json) An array containing the texts for translation. All strings must be of the same language. The total of all texts must not exceed 10000 characters. The max number of array items is 2000.)
        """
        super(TranslateArrayInputSet, self)._set_input('Texts', value)
    def set_To(self, value):
        """
        Set the value of the To input for this Choreo. ((required, string) A string representing the ISO 639-1 language code to translate the text into (e.g., es).)
        """
        super(TranslateArrayInputSet, self)._set_input('To', value)
    def set_URI(self, value):
        """
        Set the value of the URI input for this Choreo. ((optional, string) Filter results by this URI. Default: all)
        """
        super(TranslateArrayInputSet, self)._set_input('URI', value)
    def set_User(self, value):
        """
        Set the value of the User input for this Choreo. ((optional, multiline) Filter results by this user. Default: all)
        """
        super(TranslateArrayInputSet, self)._set_input('User', value)

class TranslateArrayResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the TranslateArray Choreo.
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

class TranslateArrayChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return TranslateArrayResultSet(response, path)
