# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteTags
# Deletes a specific set of tags from a specific set of resources.
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

class DeleteTags(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteTags Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(DeleteTags, self).__init__(temboo_session, '/Library/Amazon/EC2/DeleteTags')


    def new_input_set(self):
        return DeleteTagsInputSet()

    def _make_result_set(self, result, path):
        return DeleteTagsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteTagsChoreographyExecution(session, exec_id, path)

class DeleteTagsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteTags
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(DeleteTagsInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(DeleteTagsInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_ResourceId(self, value):
        """
        Set the value of the ResourceId input for this Choreo. ((required, string) The ID of a resource to tag. This can be a comma-separated list of up to 10  Resource IDs.)
        """
        super(DeleteTagsInputSet, self)._set_input('ResourceId', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(DeleteTagsInputSet, self)._set_input('ResponseFormat', value)
    def set_TagKey(self, value):
        """
        Set the value of the TagKey input for this Choreo. ((required, string) The key for a tag.)
        """
        super(DeleteTagsInputSet, self)._set_input('TagKey', value)
    def set_TagValue(self, value):
        """
        Set the value of the TagValue input for this Choreo. ((optional, string) Indicates a tag should be deleted only if the value matches.To delete a tag regardless of its value, leave this blank. To delete a tag with an empty string value (""), pass the string value "null".)
        """
        super(DeleteTagsInputSet, self)._set_input('TagValue', value)
    def set_UserRegion(self, value):
        """
        Set the value of the UserRegion input for this Choreo. ((optional, string) The AWS region that corresponds to the EC2 endpoint you wish to access. The default region is "us-east-1". See description below for valid values.)
        """
        super(DeleteTagsInputSet, self)._set_input('UserRegion', value)

class DeleteTagsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteTags Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class DeleteTagsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return DeleteTagsResultSet(response, path)
