# -*- coding: utf-8 -*-

###############################################################################
#
# SearchByNeighborhood
# Retrieve businesses by neighborhood.
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

class SearchByNeighborhood(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchByNeighborhood Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(SearchByNeighborhood, self).__init__(temboo_session, '/Library/Yelp/SearchByNeighborhood')


    def new_input_set(self):
        return SearchByNeighborhoodInputSet()

    def _make_result_set(self, result, path):
        return SearchByNeighborhoodResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchByNeighborhoodChoreographyExecution(session, exec_id, path)

class SearchByNeighborhoodInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchByNeighborhood
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_BusinessType(self, value):
        """
        Set the value of the BusinessType input for this Choreo. ((optional, string) A term to narrow the search, such as "wine" or "restaurants". Leave blank to search for all business types.)
        """
        super(SearchByNeighborhoodInputSet, self)._set_input('BusinessType', value)
    def set_Category(self, value):
        """
        Set the value of the Category input for this Choreo. ((optional, string) The category to filter search results with. This can be a list of comma delimited categories. For example, "bars,french". See Choreo description for a list of categories.)
        """
        super(SearchByNeighborhoodInputSet, self)._set_input('Category', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The Consumer Key provided by Yelp.)
        """
        super(SearchByNeighborhoodInputSet, self)._set_input('ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The Consumer Secret provided by Yelp.)
        """
        super(SearchByNeighborhoodInputSet, self)._set_input('ConsumerSecret', value)
    def set_Count(self, value):
        """
        Set the value of the Count input for this Choreo. ((optional, integer) The number of business results to return. The maxiumum is 20.)
        """
        super(SearchByNeighborhoodInputSet, self)._set_input('Count', value)
    def set_CountryCode(self, value):
        """
        Set the value of the CountryCode input for this Choreo. ((optional, string) The ISO 3166-1 2-digit country code to use when parsing the location field. United States = US, Canada = CA, United Kingdom = GB.)
        """
        super(SearchByNeighborhoodInputSet, self)._set_input('CountryCode', value)
    def set_Deals(self, value):
        """
        Set the value of the Deals input for this Choreo. ((optional, boolean) Set to "true" to exclusively search for businesses with deals.)
        """
        super(SearchByNeighborhoodInputSet, self)._set_input('Deals', value)
    def set_LanguageCode(self, value):
        """
        Set the value of the LanguageCode input for this Choreo. ((optional, string) The ISO 639 language code. Default to "en". Reviews and snippets written in the specified language will be returned.)
        """
        super(SearchByNeighborhoodInputSet, self)._set_input('LanguageCode', value)
    def set_Neighborhood(self, value):
        """
        Set the value of the Neighborhood input for this Choreo. ((required, string) The neighborhood in which to search for businesses. See the Yelp API documentation for a list of supported neighborhoods.)
        """
        super(SearchByNeighborhoodInputSet, self)._set_input('Neighborhood', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) Offsets the list of returned business results by this amount.)
        """
        super(SearchByNeighborhoodInputSet, self)._set_input('Offset', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format of the response from Yelp, either XML or JSON (the default).)
        """
        super(SearchByNeighborhoodInputSet, self)._set_input('ResponseFormat', value)
    def set_Sort(self, value):
        """
        Set the value of the Sort input for this Choreo. ((optional, integer) The sort mode: 0 = Best matched, 1 = Distance (default), 2 = Highest Rated.)
        """
        super(SearchByNeighborhoodInputSet, self)._set_input('Sort', value)
    def set_TokenSecret(self, value):
        """
        Set the value of the TokenSecret input for this Choreo. ((required, string) The Token Secret provided by Yelp.)
        """
        super(SearchByNeighborhoodInputSet, self)._set_input('TokenSecret', value)
    def set_Token(self, value):
        """
        Set the value of the Token input for this Choreo. ((required, string) The Token provided by Yelp.)
        """
        super(SearchByNeighborhoodInputSet, self)._set_input('Token', value)

class SearchByNeighborhoodResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchByNeighborhood Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Yelp. Corresponds to the input value for ResponseFormat (defaults to JSON).)
        """
        return self._output.get('Response', None)

class SearchByNeighborhoodChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SearchByNeighborhoodResultSet(response, path)
