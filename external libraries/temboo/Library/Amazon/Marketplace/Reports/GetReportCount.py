# -*- coding: utf-8 -*-

###############################################################################
#
# GetReportCount
# Retrieves the number of your available Amazon Marketplace reports, ready for download, that were generated in the last 90 days.
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

class GetReportCount(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetReportCount Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetReportCount, self).__init__(temboo_session, '/Library/Amazon/Marketplace/Reports/GetReportCount')


    def new_input_set(self):
        return GetReportCountInputSet()

    def _make_result_set(self, result, path):
        return GetReportCountResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetReportCountChoreographyExecution(session, exec_id, path)

class GetReportCountInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetReportCount
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(GetReportCountInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSMarketplaceId(self, value):
        """
        Set the value of the AWSMarketplaceId input for this Choreo. ((required, string) The Marketplace ID provided by Amazon Web Services.)
        """
        super(GetReportCountInputSet, self)._set_input('AWSMarketplaceId', value)
    def set_AWSMerchantId(self, value):
        """
        Set the value of the AWSMerchantId input for this Choreo. ((required, string) The Merchant ID provided by Amazon Web Services.)
        """
        super(GetReportCountInputSet, self)._set_input('AWSMerchantId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(GetReportCountInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_Acknowledged(self, value):
        """
        Set the value of the Acknowledged input for this Choreo. ((optional, boolean) A Boolean value that indicates if an order report has been acknowledged by a prior call to UpdateReportAcknowledgements. Set to "true" to list order reports that have been acknowledged.)
        """
        super(GetReportCountInputSet, self)._set_input('Acknowledged', value)
    def set_AvailableFromDate(self, value):
        """
        Set the value of the AvailableFromDate input for this Choreo. ((optional, date) The earliest date you are looking for, in ISO8601 date format (i.e. 2012-01-01).)
        """
        super(GetReportCountInputSet, self)._set_input('AvailableFromDate', value)
    def set_AvailableToDate(self, value):
        """
        Set the value of the AvailableToDate input for this Choreo. ((optional, date) The most recent date you are looking for, in ISO8601 date format (i.e. 2012-01-01).)
        """
        super(GetReportCountInputSet, self)._set_input('AvailableToDate', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((conditional, string) The base URL for the MWS endpoint. Defaults to mws.amazonservices.co.uk.)
        """
        super(GetReportCountInputSet, self)._set_input('Endpoint', value)
    def set_ReportType(self, value):
        """
        Set the value of the ReportType input for this Choreo. ((optional, string) A ReportType enumeration value (i.e. _GET_FLAT_FILE_OPEN_LISTINGS_DATA_).)
        """
        super(GetReportCountInputSet, self)._set_input('ReportType', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(GetReportCountInputSet, self)._set_input('ResponseFormat', value)

class GetReportCountResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetReportCount Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (Stores the response from Amazon.)
        """
        return self._output.get('Response', None)
    def get_Count(self):
        """
        Retrieve the value for the "Count" output from this Choreo execution. ((integer) A non-negative integer. parsed from the Amazon response, that represents the total number of reports available to download.)
        """
        return self._output.get('Count', None)

class GetReportCountChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetReportCountResultSet(response, path)
