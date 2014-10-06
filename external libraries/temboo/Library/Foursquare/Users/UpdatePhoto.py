# -*- coding: utf-8 -*-

###############################################################################
#
# UpdatePhoto
# Updates the user's profile photo.
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

class UpdatePhoto(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdatePhoto Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(UpdatePhoto, self).__init__(temboo_session, '/Library/Foursquare/Users/UpdatePhoto')


    def new_input_set(self):
        return UpdatePhotoInputSet()

    def _make_result_set(self, result, path):
        return UpdatePhotoResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdatePhotoChoreographyExecution(session, exec_id, path)

class UpdatePhotoInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdatePhoto
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ContentType(self, value):
        """
        Set the value of the ContentType input for this Choreo. ((required, string) The content type of the image. Valid types are: image/jpeg, image/gif, or image/png.)
        """
        super(UpdatePhotoInputSet, self)._set_input('ContentType', value)
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((required, string) The Foursquare API Oauth token string.)
        """
        super(UpdatePhotoInputSet, self)._set_input('OauthToken', value)
    def set_Photo(self, value):
        """
        Set the value of the Photo input for this Choreo. ((conditional, string) The Base64-encoded contents of the image you want to upload. Total Image size (before encoding) must be under 100KB.)
        """
        super(UpdatePhotoInputSet, self)._set_input('Photo', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(UpdatePhotoInputSet, self)._set_input('ResponseFormat', value)


class UpdatePhotoResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdatePhoto Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class UpdatePhotoChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return UpdatePhotoResultSet(response, path)
