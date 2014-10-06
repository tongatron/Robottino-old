# -*- coding: utf-8 -*-

###############################################################################
#
# CreateThread
# Creates a new thread.
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

class CreateThread(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateThread Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateThread, self).__init__(temboo_session, '/Library/Disqus/Threads/CreateThread')


    def new_input_set(self):
        return CreateThreadInputSet()

    def _make_result_set(self, result, path):
        return CreateThreadResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateThreadChoreographyExecution(session, exec_id, path)

class CreateThreadInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateThread
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) A valid OAuth 2.0 access token.)
        """
        super(CreateThreadInputSet, self)._set_input('AccessToken', value)
    def set_Category(self, value):
        """
        Set the value of the Category input for this Choreo. ((optional, string) The id of a category associated with the thread being created.)
        """
        super(CreateThreadInputSet, self)._set_input('Category', value)
    def set_Date(self, value):
        """
        Set the value of the Date input for this Choreo. ((optional, date) The date to be associated with this thread (as a unix timestamp or ISO datetime format).)
        """
        super(CreateThreadInputSet, self)._set_input('Date', value)
    def set_Forum(self, value):
        """
        Set the value of the Forum input for this Choreo. ((required, string) Forum Short Name (i.e., the subdomain of the Disqus Site URL).)
        """
        super(CreateThreadInputSet, self)._set_input('Forum', value)
    def set_Identifier(self, value):
        """
        Set the value of the Identifier input for this Choreo. ((optional, string) An optional string identifier for the thread. Maximum length is 300.)
        """
        super(CreateThreadInputSet, self)._set_input('Identifier', value)
    def set_Message(self, value):
        """
        Set the value of the Message input for this Choreo. ((optional, string) A message for the new thread.)
        """
        super(CreateThreadInputSet, self)._set_input('Message', value)
    def set_PublicKey(self, value):
        """
        Set the value of the PublicKey input for this Choreo. ((required, string) The Public Key provided by Disqus (AKA the API Key).)
        """
        super(CreateThreadInputSet, self)._set_input('PublicKey', value)
    def set_Title(self, value):
        """
        Set the value of the Title input for this Choreo. ((required, string) The title of the thread.)
        """
        super(CreateThreadInputSet, self)._set_input('Title', value)
    def set_URL(self, value):
        """
        Set the value of the URL input for this Choreo. ((optional, string) A URL to be associated with the thread. Maximum length is 500.)
        """
        super(CreateThreadInputSet, self)._set_input('URL', value)

class CreateThreadResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateThread Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) )
        """
        return self._output.get('Response', None)

class CreateThreadChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateThreadResultSet(response, path)
