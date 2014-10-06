# -*- coding: utf-8 -*-

###############################################################################
#
# AddMemberMessageAAQToPartner
# Allows a buyer and seller in an order relationship to send messages to each other's My Messages Inboxes.
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

class AddMemberMessageAAQToPartner(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AddMemberMessageAAQToPartner Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(AddMemberMessageAAQToPartner, self).__init__(temboo_session, '/Library/eBay/Trading/AddMemberMessageAAQToPartner')


    def new_input_set(self):
        return AddMemberMessageAAQToPartnerInputSet()

    def _make_result_set(self, result, path):
        return AddMemberMessageAAQToPartnerResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddMemberMessageAAQToPartnerChoreographyExecution(session, exec_id, path)

class AddMemberMessageAAQToPartnerInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AddMemberMessageAAQToPartner
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Body(self, value):
        """
        Set the value of the Body input for this Choreo. ((required, string) The message body.)
        """
        super(AddMemberMessageAAQToPartnerInputSet, self)._set_input('Body', value)
    def set_EmailCopyToSender(self, value):
        """
        Set the value of the EmailCopyToSender input for this Choreo. ((optional, boolean) A flag used to indicate that a copy should be sent to the sender.)
        """
        super(AddMemberMessageAAQToPartnerInputSet, self)._set_input('EmailCopyToSender', value)
    def set_ItemID(self, value):
        """
        Set the value of the ItemID input for this Choreo. ((required, string) The unique ID of the item about which the question was asked.)
        """
        super(AddMemberMessageAAQToPartnerInputSet, self)._set_input('ItemID', value)
    def set_QuestionType(self, value):
        """
        Set the value of the QuestionType input for this Choreo. ((required, string) The type of question. Valid values are: General, Shipping, Payment, MultipleItemShipping, CustomizedSubject, or None.)
        """
        super(AddMemberMessageAAQToPartnerInputSet, self)._set_input('QuestionType', value)
    def set_RecipientID(self, value):
        """
        Set the value of the RecipientID input for this Choreo. ((required, string) The user ID of the message recipient.)
        """
        super(AddMemberMessageAAQToPartnerInputSet, self)._set_input('RecipientID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(AddMemberMessageAAQToPartnerInputSet, self)._set_input('ResponseFormat', value)
    def set_SandboxMode(self, value):
        """
        Set the value of the SandboxMode input for this Choreo. ((optional, boolean) Indicates that the request should be made to the sandbox endpoint instead of the production endpoint. Set to 1 to enable sandbox mode.)
        """
        super(AddMemberMessageAAQToPartnerInputSet, self)._set_input('SandboxMode', value)
    def set_SiteID(self, value):
        """
        Set the value of the SiteID input for this Choreo. ((optional, string) The eBay site ID that you want to access. Defaults to 0 indicating the US site.)
        """
        super(AddMemberMessageAAQToPartnerInputSet, self)._set_input('SiteID', value)
    def set_Subject(self, value):
        """
        Set the value of the Subject input for this Choreo. ((required, string) The message subject.)
        """
        super(AddMemberMessageAAQToPartnerInputSet, self)._set_input('Subject', value)
    def set_UserToken(self, value):
        """
        Set the value of the UserToken input for this Choreo. ((required, string) A valid eBay Auth Token.)
        """
        super(AddMemberMessageAAQToPartnerInputSet, self)._set_input('UserToken', value)

class AddMemberMessageAAQToPartnerResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AddMemberMessageAAQToPartner Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from eBay.)
        """
        return self._output.get('Response', None)

class AddMemberMessageAAQToPartnerChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return AddMemberMessageAAQToPartnerResultSet(response, path)
