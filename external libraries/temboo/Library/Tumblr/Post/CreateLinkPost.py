# -*- coding: utf-8 -*-

###############################################################################
#
# CreateLinkPost
# Creates a new link post for a specified Tumblr blog.
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

class CreateLinkPost(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateLinkPost Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CreateLinkPost, self).__init__(temboo_session, '/Library/Tumblr/Post/CreateLinkPost')


    def new_input_set(self):
        return CreateLinkPostInputSet()

    def _make_result_set(self, result, path):
        return CreateLinkPostResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateLinkPostChoreographyExecution(session, exec_id, path)

class CreateLinkPostInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateLinkPost
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_URL(self, value):
        """
        Set the value of the URL input for this Choreo. ((required, string) The link you want to post.)
        """
        super(CreateLinkPostInputSet, self)._set_input('URL', value)
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Tumblr (AKA the OAuth Consumer Key).)
        """
        super(CreateLinkPostInputSet, self)._set_input('APIKey', value)
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        super(CreateLinkPostInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        super(CreateLinkPostInputSet, self)._set_input('AccessToken', value)
    def set_BaseHostname(self, value):
        """
        Set the value of the BaseHostname input for this Choreo. ((required, string) The standard or custom blog hostname (i.e. temboo.tumblr.com).)
        """
        super(CreateLinkPostInputSet, self)._set_input('BaseHostname', value)
    def set_Date(self, value):
        """
        Set the value of the Date input for this Choreo. ((optional, date) The GMT date and time of the post. Can be an epoch timestamp in milliseconds or formatted like: Dec 8th, 2011 4:03pm. Defaults to NOW().)
        """
        super(CreateLinkPostInputSet, self)._set_input('Date', value)
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((optional, string) A user-supplied description. HTML is allowed.)
        """
        super(CreateLinkPostInputSet, self)._set_input('Description', value)
    def set_Markdown(self, value):
        """
        Set the value of the Markdown input for this Choreo. ((optional, boolean) Indicates whether the post uses markdown syntax. Defaults to false. Set to 1 to indicate true.)
        """
        super(CreateLinkPostInputSet, self)._set_input('Markdown', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        super(CreateLinkPostInputSet, self)._set_input('ResponseFormat', value)
    def set_SecretKey(self, value):
        """
        Set the value of the SecretKey input for this Choreo. ((required, string) The Secret Key provided by Tumblr (AKA the OAuth Consumer Secret).)
        """
        super(CreateLinkPostInputSet, self)._set_input('SecretKey', value)
    def set_Slug(self, value):
        """
        Set the value of the Slug input for this Choreo. ((optional, string) Adds a short text summary to the end of the post URL.)
        """
        super(CreateLinkPostInputSet, self)._set_input('Slug', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((optional, string) The state of the post. Specify one of the following:  published, draft, queue. Defaults to published.)
        """
        super(CreateLinkPostInputSet, self)._set_input('State', value)
    def set_Tags(self, value):
        """
        Set the value of the Tags input for this Choreo. ((optional, string) Comma-separated tags for this post.)
        """
        super(CreateLinkPostInputSet, self)._set_input('Tags', value)
    def set_Title(self, value):
        """
        Set the value of the Title input for this Choreo. ((optional, string) The title of the page the link points to. HTML entities should be escaped.)
        """
        super(CreateLinkPostInputSet, self)._set_input('Title', value)
    def set_Tweet(self, value):
        """
        Set the value of the Tweet input for this Choreo. ((optional, string) Manages the autotweet (if enabled) for this post. Set to "off" for no tweet. Enter text to override the default tweet.)
        """
        super(CreateLinkPostInputSet, self)._set_input('Tweet', value)

class CreateLinkPostResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateLinkPost Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Tumblr. Default is JSON, can be set to XML by entering 'xml' in ResponseFormat.)
        """
        return self._output.get('Response', None)

class CreateLinkPostChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CreateLinkPostResultSet(response, path)
