# -*- coding: utf-8 -*-

###############################################################################
#
# SetPhotoLocation
# Sets the geo data (including latitude and longitude) for a specified photo.
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

class SetPhotoLocation(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SetPhotoLocation Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(SetPhotoLocation, self).__init__(temboo_session, '/Library/Flickr/Geo/SetPhotoLocation')


    def new_input_set(self):
        return SetPhotoLocationInputSet()

    def _make_result_set(self, result, path):
        return SetPhotoLocationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SetPhotoLocationChoreographyExecution(session, exec_id, path)

class SetPhotoLocationInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SetPhotoLocation
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Flickr (AKA the OAuth Consumer Key).)
        """
        super(SetPhotoLocationInputSet, self)._set_input('APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((required, string) The API Secret provided by Flickr (AKA the OAuth Consumer Secret).)
        """
        super(SetPhotoLocationInputSet, self)._set_input('APISecret', value)
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(SetPhotoLocationInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(SetPhotoLocationInputSet, self)._set_input('AccessToken', value)
    def set_Accuracy(self, value):
        """
        Set the value of the Accuracy input for this Choreo. ((optional, integer) Recorded accuracy level of the location information. Current range is 1-16. Defaults to 16 if not specified.)
        """
        super(SetPhotoLocationInputSet, self)._set_input('Accuracy', value)
    def set_Context(self, value):
        """
        Set the value of the Context input for this Choreo. ((optional, string) A numeric value representing the photo's location beyond latitude and longitude. For example, you can indicate that a photo was taken "indoors" or "outdoors". Set to 1 for indoors or 2 for outdoors.)
        """
        super(SetPhotoLocationInputSet, self)._set_input('Context', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((required, decimal) The latitude whose valid range is -90 to 90. Anything more than 6 decimal places will be truncated.)
        """
        super(SetPhotoLocationInputSet, self)._set_input('Latitude', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((required, decimal) The longitude whose valid range is -180 to 180. Anything more than 6 decimal places will be truncated.)
        """
        super(SetPhotoLocationInputSet, self)._set_input('Longitude', value)
    def set_PhotoID(self, value):
        """
        Set the value of the PhotoID input for this Choreo. ((required, integer) The id of the photo to set location data for.)
        """
        super(SetPhotoLocationInputSet, self)._set_input('PhotoID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml and json. Defaults to json.)
        """
        super(SetPhotoLocationInputSet, self)._set_input('ResponseFormat', value)

class SetPhotoLocationResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SetPhotoLocation Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Flickr.)
        """
        return self._output.get('Response', None)

class SetPhotoLocationChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SetPhotoLocationResultSet(response, path)
