# -*- coding: utf-8 -*-

###############################################################################
#
# PlaceSearch
# Search for places based on latitude/longitude coordinates, keywords, and distance.
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

class PlaceSearch(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the PlaceSearch Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(PlaceSearch, self).__init__(temboo_session, '/Library/Google/Places/PlaceSearch')


    def new_input_set(self):
        return PlaceSearchInputSet()

    def _make_result_set(self, result, path):
        return PlaceSearchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PlaceSearchChoreographyExecution(session, exec_id, path)

class PlaceSearchInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the PlaceSearch
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Key(self, value):
        """
        Set the value of the Key input for this Choreo. ((required, string) Enter your Google API key.)
        """
        super(PlaceSearchInputSet, self)._set_input('Key', value)
    def set_Keyword(self, value):
        """
        Set the value of the Keyword input for this Choreo. ((optional, string) Enter a keyword (term, address, type, customer review, etc.) to be matched against all results retrieved for this Place.)
        """
        super(PlaceSearchInputSet, self)._set_input('Keyword', value)
    def set_Language(self, value):
        """
        Set the value of the Language input for this Choreo. ((optional, string) Set the language in which to return restults.  A list of supported languages is available here: https://spreadsheets.google.com/pub?key=p9pdwsai2hDMsLkXsoM05KQ&gid=1)
        """
        super(PlaceSearchInputSet, self)._set_input('Language', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((required, string) Specify a latitude point around which Places results will be retrieved.)
        """
        super(PlaceSearchInputSet, self)._set_input('Latitude', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((required, string) Specify a longitude point around which Places results will be retrieved.)
        """
        super(PlaceSearchInputSet, self)._set_input('Longitude', value)
    def set_MaxPrice(self, value):
        """
        Set the value of the MaxPrice input for this Choreo. ((optional, integer) Restricts results to only those places within the specified range. Valid values range between 0 (most affordable) to 4 (most expensive), inclusive. The exact amount will vary from region to region.)
        """
        super(PlaceSearchInputSet, self)._set_input('MaxPrice', value)
    def set_MinPrice(self, value):
        """
        Set the value of the MinPrice input for this Choreo. ((optional, integer) Restricts results to only those places within the specified range. Valid values range between 0 (most affordable) to 4 (most expensive), inclusive. The exact amount will vary from region to region.)
        """
        super(PlaceSearchInputSet, self)._set_input('MinPrice', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((optional, string) Enter a name to be matched when results are retrieved for this specified Place.)
        """
        super(PlaceSearchInputSet, self)._set_input('Name', value)
    def set_OpenNow(self, value):
        """
        Set the value of the OpenNow input for this Choreo. ((optional, boolean) Returns only those Places that are open for business at the time the query is sent. Places that do not specify opening hours in the Google Places database will not be returned.)
        """
        super(PlaceSearchInputSet, self)._set_input('OpenNow', value)
    def set_PageToken(self, value):
        """
        Set the value of the PageToken input for this Choreo. ((optional, string) The "NextPageToken" returned in the choreo output from a previous run. Used to page through large result sets. When the PageToken is specified, all other inputs are ignored.)
        """
        super(PlaceSearchInputSet, self)._set_input('PageToken', value)
    def set_Radius(self, value):
        """
        Set the value of the Radius input for this Choreo. ((required, integer) Specify the radius in meters for which Places results will be returned. Maximum radius is limited to 50,000 meters. If rankby=distance, then radius must not be specified.)
        """
        super(PlaceSearchInputSet, self)._set_input('Radius', value)
    def set_RankBy(self, value):
        """
        Set the value of the RankBy input for this Choreo. ((optional, string) Specify how results are listed. Values include: prominence (default); distance - sorts results by distance from specified location. Radius must not be used, and Keyword, Name, or Types are required).)
        """
        super(PlaceSearchInputSet, self)._set_input('RankBy', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(PlaceSearchInputSet, self)._set_input('ResponseFormat', value)
    def set_Sensor(self, value):
        """
        Set the value of the Sensor input for this Choreo. ((optional, boolean) Indicates whether or not the directions request is from a device with a location sensor. Value must be either 1 or 0. Defaults to 0 (false).)
        """
        super(PlaceSearchInputSet, self)._set_input('Sensor', value)
    def set_Types(self, value):
        """
        Set the value of the Types input for this Choreo. ((optional, string) Filter results by types, such as: bar, dentist.  Multiple types must be separated by the pipe ("|") symbol: bar|dentist|airport.)
        """
        super(PlaceSearchInputSet, self)._set_input('Types', value)

class PlaceSearchResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the PlaceSearch Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Google.)
        """
        return self._output.get('Response', None)

class PlaceSearchChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return PlaceSearchResultSet(response, path)
