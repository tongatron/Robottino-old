# -*- coding: utf-8 -*-

###############################################################################
#
# CreateAlbum
# Creates an album.
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

class CreateAlbum(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateAlbum Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateAlbum, self).__init__(temboo_session, '/Library/Facebook/Publishing/CreateAlbum')


    def new_input_set(self):
        return CreateAlbumInputSet()

    def _make_result_set(self, result, path):
        return CreateAlbumResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateAlbumChoreographyExecution(session, exec_id, path)

class CreateAlbumInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateAlbum
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        super(CreateAlbumInputSet, self)._set_input('AccessToken', value)
    def set_Message(self, value):
        """
        Set the value of the Message input for this Choreo. ((optional, string) A message to attach to the album.)
        """
        super(CreateAlbumInputSet, self)._set_input('Message', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((required, string) The name of the album.)
        """
        super(CreateAlbumInputSet, self)._set_input('Name', value)
    def set_ProfileID(self, value):
        """
        Set the value of the ProfileID input for this Choreo. ((optional, string) The id for the profile that the album will be published to. Defaults to "me" indicating the authenticated user.)
        """
        super(CreateAlbumInputSet, self)._set_input('ProfileID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(CreateAlbumInputSet, self)._set_input('ResponseFormat', value)

class CreateAlbumResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateAlbum Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Facebook. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class CreateAlbumChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateAlbumResultSet(response, path)
