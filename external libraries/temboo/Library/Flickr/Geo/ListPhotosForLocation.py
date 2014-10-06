# -*- coding: utf-8 -*-

###############################################################################
#
# ListPhotosForLocation
# Return a list of the user's photos for a specified location.
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

class ListPhotosForLocation(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListPhotosForLocation Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListPhotosForLocation, self).__init__(temboo_session, '/Library/Flickr/Geo/ListPhotosForLocation')


    def new_input_set(self):
        return ListPhotosForLocationInputSet()

    def _make_result_set(self, result, path):
        return ListPhotosForLocationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListPhotosForLocationChoreographyExecution(session, exec_id, path)

class ListPhotosForLocationInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListPhotosForLocation
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Flickr (AKA the OAuth Consumer Key).)
        """
        super(ListPhotosForLocationInputSet, self)._set_input('APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((required, string) The API Secret provided by Flickr (AKA the OAuth Consumer Secret).)
        """
        super(ListPhotosForLocationInputSet, self)._set_input('APISecret', value)
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(ListPhotosForLocationInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(ListPhotosForLocationInputSet, self)._set_input('AccessToken', value)
    def set_Accuracy(self, value):
        """
        Set the value of the Accuracy input for this Choreo. ((optional, integer) Recorded accuracy level of the location information. Current range is 1-16. Defaults to 16 if not specified.)
        """
        super(ListPhotosForLocationInputSet, self)._set_input('Accuracy', value)
    def set_Extras(self, value):
        """
        Set the value of the Extras input for this Choreo. ((optional, string) A comma-delimited list of extra information to retrieve for each returned record. See Choreo documentation for accepted values.)
        """
        super(ListPhotosForLocationInputSet, self)._set_input('Extras', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((required, decimal) The latitude whose valid range is -90 to 90. Anything more than 6 decimal places will be truncated.)
        """
        super(ListPhotosForLocationInputSet, self)._set_input('Latitude', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((required, decimal) The longitude whose valid range is -180 to 180. Anything more than 6 decimal places will be truncated.)
        """
        super(ListPhotosForLocationInputSet, self)._set_input('Longitude', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) The page of results to return. Used for paging through many results. Defaults to 1.)
        """
        super(ListPhotosForLocationInputSet, self)._set_input('Page', value)
    def set_PerPage(self, value):
        """
        Set the value of the PerPage input for this Choreo. ((optional, integer) Number of photos to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is 500.)
        """
        super(ListPhotosForLocationInputSet, self)._set_input('PerPage', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml and json. Defaults to json.)
        """
        super(ListPhotosForLocationInputSet, self)._set_input('ResponseFormat', value)

class ListPhotosForLocationResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListPhotosForLocation Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Flickr.)
        """
        return self._output.get('Response', None)

class ListPhotosForLocationChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListPhotosForLocationResultSet(response, path)
