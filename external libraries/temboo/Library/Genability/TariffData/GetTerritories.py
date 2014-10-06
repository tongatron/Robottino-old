# -*- coding: utf-8 -*-

###############################################################################
#
# GetTerritories
# Returns a list of Territory objects based a specified search criteria.
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

class GetTerritories(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetTerritories Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetTerritories, self).__init__(temboo_session, '/Library/Genability/TariffData/GetTerritories')


    def new_input_set(self):
        return GetTerritoriesInputSet()

    def _make_result_set(self, result, path):
        return GetTerritoriesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTerritoriesChoreographyExecution(session, exec_id, path)

class GetTerritoriesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetTerritories
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AppID(self, value):
        """
        Set the value of the AppID input for this Choreo. ((conditional, string) The App ID provided by Genability.)
        """
        super(GetTerritoriesInputSet, self)._set_input('AppID', value)
    def set_AppKey(self, value):
        """
        Set the value of the AppKey input for this Choreo. ((required, string) The App Key provided by Genability.)
        """
        super(GetTerritoriesInputSet, self)._set_input('AppKey', value)
    def set_ContainsItemType(self, value):
        """
        Set the value of the ContainsItemType input for this Choreo. ((optional, string) Filters the result set to include a particular type of territory. Valid values are: CITY, ZIPCODE, STATE, COUNTY.)
        """
        super(GetTerritoriesInputSet, self)._set_input('ContainsItemType', value)
    def set_ContainsItemValue(self, value):
        """
        Set the value of the ContainsItemValue input for this Choreo. ((optional, string) Used in combination with the ContainsItemType value. Filters the Types by this value.)
        """
        super(GetTerritoriesInputSet, self)._set_input('ContainsItemValue', value)
    def set_EndsWith(self, value):
        """
        Set the value of the EndsWith input for this Choreo. ((optional, string) When true, the search will only return results that end with the specified search string. Otherwise, any match of the search string will be returned as a result.)
        """
        super(GetTerritoriesInputSet, self)._set_input('EndsWith', value)
    def set_IsRegex(self, value):
        """
        Set the value of the IsRegex input for this Choreo. ((optional, boolean) When true, the provided search string will be regarded as a regular expression and the search will return results matching the regular expression.)
        """
        super(GetTerritoriesInputSet, self)._set_input('IsRegex', value)
    def set_LSEID(self, value):
        """
        Set the value of the LSEID input for this Choreo. ((optional, integer) Filters the result set to only include territories within this LSE ID.)
        """
        super(GetTerritoriesInputSet, self)._set_input('LSEID', value)
    def set_MasterTariffID(self, value):
        """
        Set the value of the MasterTariffID input for this Choreo. ((optional, integer) For tariffs with prices varying by geographic location, this will return the list of those territories covered by this tariff.)
        """
        super(GetTerritoriesInputSet, self)._set_input('MasterTariffID', value)
    def set_PageCount(self, value):
        """
        Set the value of the PageCount input for this Choreo. ((optional, integer) The number of results to return. Defaults to 25.)
        """
        super(GetTerritoriesInputSet, self)._set_input('PageCount', value)
    def set_PageStart(self, value):
        """
        Set the value of the PageStart input for this Choreo. ((optional, integer) The page number to begin the result set from. Defaults to 1.)
        """
        super(GetTerritoriesInputSet, self)._set_input('PageStart', value)
    def set_PopulateItems(self, value):
        """
        Set the value of the PopulateItems input for this Choreo. ((optional, boolean) If set to "true", returns a list of territory items for each territory in the result set.)
        """
        super(GetTerritoriesInputSet, self)._set_input('PopulateItems', value)
    def set_PopulateLSES(self, value):
        """
        Set the value of the PopulateLSES input for this Choreo. ((optional, string) If set to "true", the response includes a list of TerritoryLses which are all the LSEs providing service in this territory.)
        """
        super(GetTerritoriesInputSet, self)._set_input('PopulateLSES', value)
    def set_SearchOn(self, value):
        """
        Set the value of the SearchOn input for this Choreo. ((optional, string) Comma separated list of fields to query on. When searchOn is specified, the text provided in the search string field will be searched within these fields.)
        """
        super(GetTerritoriesInputSet, self)._set_input('SearchOn', value)
    def set_Search(self, value):
        """
        Set the value of the Search input for this Choreo. ((optional, string) The string of text to search on. This can also be a regular expression, in which case you should set the 'isRegex' flag to true.)
        """
        super(GetTerritoriesInputSet, self)._set_input('Search', value)
    def set_SortOn(self, value):
        """
        Set the value of the SortOn input for this Choreo. ((optional, string) Comma separated list of fields to sort on.)
        """
        super(GetTerritoriesInputSet, self)._set_input('SortOn', value)
    def set_SortOrder(self, value):
        """
        Set the value of the SortOrder input for this Choreo. ((optional, string) Comma separated list of ordering. Possible values are 'ASC' and 'DESC'. Default is 'ASC'. This list corresponds to the field list used in the SortOn input.)
        """
        super(GetTerritoriesInputSet, self)._set_input('SortOrder', value)
    def set_StartsWith(self, value):
        """
        Set the value of the StartsWith input for this Choreo. ((optional, boolean) When true, the search will only return results that begin with the specified search string. Otherwise, any match of the search string will be returned as a result.)
        """
        super(GetTerritoriesInputSet, self)._set_input('StartsWith', value)
    def set_UsageTypes(self, value):
        """
        Set the value of the UsageTypes input for this Choreo. ((optional, string) Filters the result set to only include territories of the specified usageType. valid values are: SERVICE, TARIFF.)
        """
        super(GetTerritoriesInputSet, self)._set_input('UsageTypes', value)

class GetTerritoriesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetTerritories Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Genability.)
        """
        return self._output.get('Response', None)

class GetTerritoriesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetTerritoriesResultSet(response, path)
