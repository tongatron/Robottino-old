# -*- coding: utf-8 -*-

###############################################################################
#
# DeletePost
# Deletes a specified post from a Tumblr blog.
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

class DeletePost(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeletePost Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DeletePost, self).__init__(temboo_session, '/Library/Tumblr/Post/DeletePost')


    def new_input_set(self):
        return DeletePostInputSet()

    def _make_result_set(self, result, path):
        return DeletePostResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeletePostChoreographyExecution(session, exec_id, path)

class DeletePostInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeletePost
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Tumblr (AKA the OAuth Consumer Key).)
        """
        super(DeletePostInputSet, self)._set_input('APIKey', value)
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(DeletePostInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(DeletePostInputSet, self)._set_input('AccessToken', value)
    def set_BaseHostname(self, value):
        """
        Set the value of the BaseHostname input for this Choreo. ((required, string) The standard or custom blog hostname (i.e. temboo.tumblr.com).)
        """
        super(DeletePostInputSet, self)._set_input('BaseHostname', value)
    def set_ID(self, value):
        """
        Set the value of the ID input for this Choreo. ((required, integer) The ID of the post you want to delete.)
        """
        super(DeletePostInputSet, self)._set_input('ID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(DeletePostInputSet, self)._set_input('ResponseFormat', value)
    def set_SecretKey(self, value):
        """
        Set the value of the SecretKey input for this Choreo. ((required, string) The Secret Key provided by Tumblr (AKA the OAuth Consumer Secret).)
        """
        super(DeletePostInputSet, self)._set_input('SecretKey', value)

class DeletePostResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeletePost Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Tumblr. Default is JSON, can be set to XML by entering 'xml' in ResponseFormat.)
        """
        return self._output.get('Response', None)

class DeletePostChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeletePostResultSet(response, path)
