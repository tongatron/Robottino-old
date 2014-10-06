# -*- coding: utf-8 -*-

###############################################################################
#
# Search
# Search the Freebase dataset.
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

class Search(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Search Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(Search, self).__init__(temboo_session, '/Library/Freebase/Search')


    def new_input_set(self):
        return SearchInputSet()

    def _make_result_set(self, result, path):
        return SearchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchChoreographyExecution(session, exec_id, path)

class SearchInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Search
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Freebase.)
        """
        super(SearchInputSet, self)._set_input('APIKey', value)
    def set_Domain(self, value):
        """
        Set the value of the Domain input for this Choreo. ((optional, string) Enter a comma separated list of domain IDs.)
        """
        super(SearchInputSet, self)._set_input('Domain', value)
    def set_EscapeHTMLResults(self, value):
        """
        Set the value of the EscapeHTMLResults input for this Choreo. ((optional, boolean) Specify whether html results are to be escaped or not.  Default is set to: true.)
        """
        super(SearchInputSet, self)._set_input('EscapeHTMLResults', value)
    def set_Exact(self, value):
        """
        Set the value of the Exact input for this Choreo. ((optional, boolean) If set to true, the search query will match only the name and keys exactly. No normalization of any kind will be performed at indexing and query time.Default is set to: false.)
        """
        super(SearchInputSet, self)._set_input('Exact', value)
    def set_Filter(self, value):
        """
        Set the value of the Filter input for this Choreo. ((optional, string) Specify an s-expression to filter search results. For more info, see: http://wiki.freebase.com/wiki/Search_Cookbook)
        """
        super(SearchInputSet, self)._set_input('Filter', value)
    def set_Indent(self, value):
        """
        Set the value of the Indent input for this Choreo. ((optional, boolean) Specify whether the JSON results should be indented, or not. Enter true, or false. Default: false.)
        """
        super(SearchInputSet, self)._set_input('Indent', value)
    def set_Language(self, value):
        """
        Set the value of the Language input for this Choreo. ((optional, string) Specify the language in which the searches will be performed.  Default is set to English: /lang/en)
        """
        super(SearchInputSet, self)._set_input('Language', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Specify the number of results to be retrieved.  Default: 20.)
        """
        super(SearchInputSet, self)._set_input('Limit', value)
    def set_MQLOutput(self, value):
        """
        Set the value of the MQLOutput input for this Choreo. ((optional, string) Enter an MQL query to extract entity information.)
        """
        super(SearchInputSet, self)._set_input('MQLOutput', value)
    def set_Prefixed(self, value):
        """
        Set the value of the Prefixed input for this Choreo. ((optional, boolean) Specify whether or not search queries are to match results by name prefix. Default value: false.)
        """
        super(SearchInputSet, self)._set_input('Prefixed', value)
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((required, string) Enter a search query.)
        """
        super(SearchInputSet, self)._set_input('Query', value)
    def set_Start(self, value):
        """
        Set the value of the Start input for this Choreo. ((optional, integer) Enter a value to page through results.  Default is set to 0.)
        """
        super(SearchInputSet, self)._set_input('Start', value)
    def set_Type(self, value):
        """
        Set the value of the Type input for this Choreo. ((optional, string) Enter a comma-seperated list of type IDs.)
        """
        super(SearchInputSet, self)._set_input('Type', value)

class SearchResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Search Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from the Freebase Search API in JSON format.)
        """
        return self._output.get('Response', None)

class SearchChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SearchResultSet(response, path)
