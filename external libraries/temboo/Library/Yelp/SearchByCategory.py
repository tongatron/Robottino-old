# -*- coding: utf-8 -*-

###############################################################################
#
# SearchByCategory
# Retrieve businesses in a specific location by business category.
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

class SearchByCategory(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchByCategory Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(SearchByCategory, self).__init__(temboo_session, '/Library/Yelp/SearchByCategory')


    def new_input_set(self):
        return SearchByCategoryInputSet()

    def _make_result_set(self, result, path):
        return SearchByCategoryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchByCategoryChoreographyExecution(session, exec_id, path)

class SearchByCategoryInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchByCategory
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Category(self, value):
        """
        Set the value of the Category input for this Choreo. ((required, string) The category to filter search results with. This can be a list of comma delimited categories. For example, "bars,french". See Choreo description for a list of categories.)
        """
        super(SearchByCategoryInputSet, self)._set_input('Category', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The Consumer Key provided by Yelp.)
        """
        super(SearchByCategoryInputSet, self)._set_input('ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The Consumer Secret provided by Yelp.)
        """
        super(SearchByCategoryInputSet, self)._set_input('ConsumerSecret', value)
    def set_Count(self, value):
        """
        Set the value of the Count input for this Choreo. ((optional, integer) The number of business results to return. The maxiumum is 20.)
        """
        super(SearchByCategoryInputSet, self)._set_input('Count', value)
    def set_CountryCode(self, value):
        """
        Set the value of the CountryCode input for this Choreo. ((optional, string) The ISO 3166-1 2-digit country code to use when parsing the location field. United States = US, Canada = CA, United Kingdom = GB.)
        """
        super(SearchByCategoryInputSet, self)._set_input('CountryCode', value)
    def set_Deals(self, value):
        """
        Set the value of the Deals input for this Choreo. ((optional, boolean) Set to "true" to exclusively search for businesses with deals.)
        """
        super(SearchByCategoryInputSet, self)._set_input('Deals', value)
    def set_LanguageCode(self, value):
        """
        Set the value of the LanguageCode input for this Choreo. ((optional, string) The ISO 639 language code. Default to "en". Reviews and snippets written in the specified language will be returned.)
        """
        super(SearchByCategoryInputSet, self)._set_input('LanguageCode', value)
    def set_Location(self, value):
        """
        Set the value of the Location input for this Choreo. ((required, string) An address, neighborhood, city, state, or ZIP code in which to search for the category.)
        """
        super(SearchByCategoryInputSet, self)._set_input('Location', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) Offsets the list of returned business results by this amount.)
        """
        super(SearchByCategoryInputSet, self)._set_input('Offset', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format of the response from Yelp, either XML or JSON (the default).)
        """
        super(SearchByCategoryInputSet, self)._set_input('ResponseFormat', value)
    def set_Sort(self, value):
        """
        Set the value of the Sort input for this Choreo. ((optional, integer) The sort mode: 0 = Best matched, 1 = Distance (default), 2 = Highest Rated.)
        """
        super(SearchByCategoryInputSet, self)._set_input('Sort', value)
    def set_TokenSecret(self, value):
        """
        Set the value of the TokenSecret input for this Choreo. ((required, string) The Token Secret provided by Yelp.)
        """
        super(SearchByCategoryInputSet, self)._set_input('TokenSecret', value)
    def set_Token(self, value):
        """
        Set the value of the Token input for this Choreo. ((required, string) The Token provided by Yelp.)
        """
        super(SearchByCategoryInputSet, self)._set_input('Token', value)

class SearchByCategoryResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchByCategory Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Yelp. Corresponds to the input value for ResponseFormat (defaults to JSON).)
        """
        return self._output.get('Response', None)

class SearchByCategoryChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SearchByCategoryResultSet(response, path)
