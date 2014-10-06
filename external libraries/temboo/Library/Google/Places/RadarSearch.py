# -*- coding: utf-8 -*-

###############################################################################
#
# RadarSearch
# Search up to 200 places at once.   RadarSearch helps identify specific areas of interest within a geographic area.
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

class RadarSearch(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RadarSearch Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(RadarSearch, self).__init__(temboo_session, '/Library/Google/Places/RadarSearch')


    def new_input_set(self):
        return RadarSearchInputSet()

    def _make_result_set(self, result, path):
        return RadarSearchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RadarSearchChoreographyExecution(session, exec_id, path)

class RadarSearchInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RadarSearch
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Key(self, value):
        """
        Set the value of the Key input for this Choreo. ((required, string) Enter your Google API key.)
        """
        super(RadarSearchInputSet, self)._set_input('Key', value)
    def set_Keyword(self, value):
        """
        Set the value of the Keyword input for this Choreo. ((conditional, string) Enter a keyword (term, address, type, customer review, etc.) to be matched against all results retrieved for this Place.  At least one of Keyword, Name or Types must be specified.)
        """
        super(RadarSearchInputSet, self)._set_input('Keyword', value)
    def set_Language(self, value):
        """
        Set the value of the Language input for this Choreo. ((optional, string) Set the language in which to return restults.  A list of supported languages is available here: https://spreadsheets.google.com/pub?key=p9pdwsai2hDMsLkXsoM05KQ&gid=1)
        """
        super(RadarSearchInputSet, self)._set_input('Language', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((required, string) Specify a latitude point around which Places results will be retrieved.)
        """
        super(RadarSearchInputSet, self)._set_input('Latitude', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((required, string) Specify a longitude point around which Places results will be retrieved.)
        """
        super(RadarSearchInputSet, self)._set_input('Longitude', value)
    def set_MaxPrice(self, value):
        """
        Set the value of the MaxPrice input for this Choreo. ((optional, integer) Restricts results to only those places within the specified range. Valid values range between 0 (most affordable) to 4 (most expensive), inclusive. The exact amount will vary from region to region.)
        """
        super(RadarSearchInputSet, self)._set_input('MaxPrice', value)
    def set_MinPrice(self, value):
        """
        Set the value of the MinPrice input for this Choreo. ((optional, integer) Restricts results to only those places within the specified range. Valid values range between 0 (most affordable) to 4 (most expensive), inclusive. The exact amount will vary from region to region.)
        """
        super(RadarSearchInputSet, self)._set_input('MinPrice', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((conditional, string) Enter a name to be matched when results are retrieved for this specified Place.  At least one of Keyword, Name or Types must be specified.)
        """
        super(RadarSearchInputSet, self)._set_input('Name', value)
    def set_OpenNow(self, value):
        """
        Set the value of the OpenNow input for this Choreo. ((optional, boolean) Returns only those Places that are open for business at the time the query is sent. Places that do not specify opening hours in the Google Places database will not be returned.)
        """
        super(RadarSearchInputSet, self)._set_input('OpenNow', value)
    def set_PageToken(self, value):
        """
        Set the value of the PageToken input for this Choreo. ((optional, string) The "NextPageToken" returned in the choreo output from a previous run. Used to page through large result sets. When the PageToken is specified, all other inputs are ignored.)
        """
        super(RadarSearchInputSet, self)._set_input('PageToken', value)
    def set_Radius(self, value):
        """
        Set the value of the Radius input for this Choreo. ((required, integer) Specify the radius in meters for which Places results will be returned. Maximum radius is limited to 50,000 meters.)
        """
        super(RadarSearchInputSet, self)._set_input('Radius', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(RadarSearchInputSet, self)._set_input('ResponseFormat', value)
    def set_Sensor(self, value):
        """
        Set the value of the Sensor input for this Choreo. ((optional, boolean) Indicates whether or not the directions request is from a device with a location sensor. Value must be either 1 or 0. Defaults to 0 (false).)
        """
        super(RadarSearchInputSet, self)._set_input('Sensor', value)
    def set_Types(self, value):
        """
        Set the value of the Types input for this Choreo. ((conditional, string) Filter results by types, such as: bar, dentist.  Multiple types must be separated by the pipe ("|") symbol: bar|dentist|airport.   At least one of Keyword, Name or Types must be specified.)
        """
        super(RadarSearchInputSet, self)._set_input('Types', value)

class RadarSearchResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RadarSearch Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Google.)
        """
        return self._output.get('Response', None)

class RadarSearchChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return RadarSearchResultSet(response, path)
