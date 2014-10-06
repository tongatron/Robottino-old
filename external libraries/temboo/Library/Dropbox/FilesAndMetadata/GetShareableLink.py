# -*- coding: utf-8 -*-

###############################################################################
#
# GetShareableLink
# Retrieves a shareable link to files or folders.
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

class GetShareableLink(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetShareableLink Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetShareableLink, self).__init__(temboo_session, '/Library/Dropbox/FilesAndMetadata/GetShareableLink')


    def new_input_set(self):
        return GetShareableLinkInputSet()

    def _make_result_set(self, result, path):
        return GetShareableLinkResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetShareableLinkChoreographyExecution(session, exec_id, path)

class GetShareableLinkInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetShareableLink
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(GetShareableLinkInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(GetShareableLinkInputSet, self)._set_input('AccessToken', value)
    def set_AppKey(self, value):
        """
        Set the value of the AppKey input for this Choreo. ((required, string) The App Key provided by Dropbox (AKA the OAuth Consumer Key).)
        """
        super(GetShareableLinkInputSet, self)._set_input('AppKey', value)
    def set_AppSecret(self, value):
        """
        Set the value of the AppSecret input for this Choreo. ((required, string) The App Secret provided by Dropbox (AKA the OAuth Consumer Secret).)
        """
        super(GetShareableLinkInputSet, self)._set_input('AppSecret', value)
    def set_Path(self, value):
        """
        Set the value of the Path input for this Choreo. ((required, string) The path to the file or folder you want to return a shareable link for (i.e. /RootFolder/SubFolder/MyFile.txt).)
        """
        super(GetShareableLinkInputSet, self)._set_input('Path', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(GetShareableLinkInputSet, self)._set_input('ResponseFormat', value)
    def set_Root(self, value):
        """
        Set the value of the Root input for this Choreo. ((conditional, string) The root relative to which path is specified. Valid values are "sandbox" and "dropbox" (the default). When your access token has the App folder level of access, this should be set to "sandbox".)
        """
        super(GetShareableLinkInputSet, self)._set_input('Root', value)

class GetShareableLinkResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetShareableLink Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Dropbox. Corresponds to the ResponseFormat input. Defaults to json.)
        """
        return self._output.get('Response', None)

class GetShareableLinkChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetShareableLinkResultSet(response, path)
