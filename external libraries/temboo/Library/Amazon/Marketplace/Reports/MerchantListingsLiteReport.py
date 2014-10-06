# -*- coding: utf-8 -*-

###############################################################################
#
# MerchantListingsLiteReport
# Returns a tab-delimited flat file active listings report that contains only the SKU, ASIN, Price, and Quantity fields for items that have a quantity greater than zero.
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

class MerchantListingsLiteReport(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the MerchantListingsLiteReport Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(MerchantListingsLiteReport, self).__init__(temboo_session, '/Library/Amazon/Marketplace/Reports/MerchantListingsLiteReport')


    def new_input_set(self):
        return MerchantListingsLiteReportInputSet()

    def _make_result_set(self, result, path):
        return MerchantListingsLiteReportResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return MerchantListingsLiteReportChoreographyExecution(session, exec_id, path)

class MerchantListingsLiteReportInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the MerchantListingsLiteReport
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(MerchantListingsLiteReportInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSMarketplaceId(self, value):
        """
        Set the value of the AWSMarketplaceId input for this Choreo. ((required, string) The Marketplace ID provided by Amazon Web Services.)
        """
        super(MerchantListingsLiteReportInputSet, self)._set_input('AWSMarketplaceId', value)
    def set_AWSMerchantId(self, value):
        """
        Set the value of the AWSMerchantId input for this Choreo. ((required, string) The Merchant ID provided by Amazon Web Services.)
        """
        super(MerchantListingsLiteReportInputSet, self)._set_input('AWSMerchantId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(MerchantListingsLiteReportInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((conditional, string) The base URL for the MWS endpoint. Defaults to mws.amazonservices.co.uk.)
        """
        super(MerchantListingsLiteReportInputSet, self)._set_input('Endpoint', value)
    def set_TimeToWait(self, value):
        """
        Set the value of the TimeToWait input for this Choreo. ((optional, integer) By default, the Choreo will wait for 5 minutes to see if the report is ready for retrieval. Max is 120 minutes.)
        """
        super(MerchantListingsLiteReportInputSet, self)._set_input('TimeToWait', value)

class MerchantListingsLiteReportResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the MerchantListingsLiteReport Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Report(self):
        """
        Retrieve the value for the "Report" output from this Choreo execution. ((multiline) The report contents.)
        """
        return self._output.get('Report', None)
    def get_GeneratedReportId(self):
        """
        Retrieve the value for the "GeneratedReportId" output from this Choreo execution. ((integer) The GeneratedReportId parsed from the Amazon response.)
        """
        return self._output.get('GeneratedReportId', None)
    def get_ReportProcessingStatus(self):
        """
        Retrieve the value for the "ReportProcessingStatus" output from this Choreo execution. ((string) The status of the report request parsed from the Amazon response.)
        """
        return self._output.get('ReportProcessingStatus', None)
    def get_ReportRequestId(self):
        """
        Retrieve the value for the "ReportRequestId" output from this Choreo execution. ((integer) The ReportRequestId parsed from the Amazon response. This id is used in GetReportRequestList.)
        """
        return self._output.get('ReportRequestId', None)

class MerchantListingsLiteReportChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return MerchantListingsLiteReportResultSet(response, path)
