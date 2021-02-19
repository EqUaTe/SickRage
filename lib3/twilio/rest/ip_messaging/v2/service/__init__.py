# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page
from twilio.rest.ip_messaging.v2.service.binding import BindingList
from twilio.rest.ip_messaging.v2.service.channel import ChannelList
from twilio.rest.ip_messaging.v2.service.role import RoleList
from twilio.rest.ip_messaging.v2.service.user import UserList


class ServiceList(ListResource):

    def __init__(self, version):
        """
        Initialize the ServiceList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.chat.v2.service.ServiceList
        :rtype: twilio.rest.chat.v2.service.ServiceList
        """
        super(ServiceList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/Services'.format(**self._solution)

    def create(self, friendly_name):
        """
        Create the ServiceInstance

        :param unicode friendly_name: A string to describe the resource

        :returns: The created ServiceInstance
        :rtype: twilio.rest.chat.v2.service.ServiceInstance
        """
        data = values.of({'FriendlyName': friendly_name, })

        payload = self._version.create(method='POST', uri=self._uri, data=data, )

        return ServiceInstance(self._version, payload, )

    def stream(self, limit=None, page_size=None):
        """
        Streams ServiceInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.chat.v2.service.ServiceInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists ServiceInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.chat.v2.service.ServiceInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of ServiceInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ServiceInstance
        :rtype: twilio.rest.chat.v2.service.ServicePage
        """
        data = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return ServicePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of ServiceInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ServiceInstance
        :rtype: twilio.rest.chat.v2.service.ServicePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return ServicePage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a ServiceContext

        :param sid: The SID of the Service resource to fetch

        :returns: twilio.rest.chat.v2.service.ServiceContext
        :rtype: twilio.rest.chat.v2.service.ServiceContext
        """
        return ServiceContext(self._version, sid=sid, )

    def __call__(self, sid):
        """
        Constructs a ServiceContext

        :param sid: The SID of the Service resource to fetch

        :returns: twilio.rest.chat.v2.service.ServiceContext
        :rtype: twilio.rest.chat.v2.service.ServiceContext
        """
        return ServiceContext(self._version, sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.IpMessaging.V2.ServiceList>'


class ServicePage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the ServicePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.chat.v2.service.ServicePage
        :rtype: twilio.rest.chat.v2.service.ServicePage
        """
        super(ServicePage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ServiceInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.chat.v2.service.ServiceInstance
        :rtype: twilio.rest.chat.v2.service.ServiceInstance
        """
        return ServiceInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.IpMessaging.V2.ServicePage>'


class ServiceContext(InstanceContext):

    def __init__(self, version, sid):
        """
        Initialize the ServiceContext

        :param Version version: Version that contains the resource
        :param sid: The SID of the Service resource to fetch

        :returns: twilio.rest.chat.v2.service.ServiceContext
        :rtype: twilio.rest.chat.v2.service.ServiceContext
        """
        super(ServiceContext, self).__init__(version)

        # Path Solution
        self._solution = {'sid': sid, }
        self._uri = '/Services/{sid}'.format(**self._solution)

        # Dependents
        self._channels = None
        self._roles = None
        self._users = None
        self._bindings = None

    def fetch(self):
        """
        Fetch the ServiceInstance

        :returns: The fetched ServiceInstance
        :rtype: twilio.rest.chat.v2.service.ServiceInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return ServiceInstance(self._version, payload, sid=self._solution['sid'], )

    def delete(self):
        """
        Deletes the ServiceInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )

    def update(self, friendly_name=values.unset,
               default_service_role_sid=values.unset,
               default_channel_role_sid=values.unset,
               default_channel_creator_role_sid=values.unset,
               read_status_enabled=values.unset, reachability_enabled=values.unset,
               typing_indicator_timeout=values.unset,
               consumption_report_interval=values.unset,
               notifications_new_message_enabled=values.unset,
               notifications_new_message_template=values.unset,
               notifications_new_message_sound=values.unset,
               notifications_new_message_badge_count_enabled=values.unset,
               notifications_added_to_channel_enabled=values.unset,
               notifications_added_to_channel_template=values.unset,
               notifications_added_to_channel_sound=values.unset,
               notifications_removed_from_channel_enabled=values.unset,
               notifications_removed_from_channel_template=values.unset,
               notifications_removed_from_channel_sound=values.unset,
               notifications_invited_to_channel_enabled=values.unset,
               notifications_invited_to_channel_template=values.unset,
               notifications_invited_to_channel_sound=values.unset,
               pre_webhook_url=values.unset, post_webhook_url=values.unset,
               webhook_method=values.unset, webhook_filters=values.unset,
               limits_channel_members=values.unset,
               limits_user_channels=values.unset,
               media_compatibility_message=values.unset,
               pre_webhook_retry_count=values.unset,
               post_webhook_retry_count=values.unset,
               notifications_log_enabled=values.unset):
        """
        Update the ServiceInstance

        :param unicode friendly_name: A string to describe the resource
        :param unicode default_service_role_sid: The service role assigned to users when they are added to the service
        :param unicode default_channel_role_sid: The channel role assigned to users when they are added to a channel
        :param unicode default_channel_creator_role_sid: The channel role assigned to a channel creator when they join a new channel
        :param bool read_status_enabled: Whether to enable the Message Consumption Horizon feature
        :param bool reachability_enabled: Whether to enable the Reachability Indicator feature for this Service instance
        :param unicode typing_indicator_timeout: How long in seconds to wait before assuming the user is no longer typing
        :param unicode consumption_report_interval: DEPRECATED
        :param bool notifications_new_message_enabled: Whether to send a notification when a new message is added to a channel
        :param unicode notifications_new_message_template: The template to use to create the notification text displayed when a new message is added to a channel
        :param unicode notifications_new_message_sound: The name of the sound to play when a new message is added to a channel
        :param bool notifications_new_message_badge_count_enabled: Whether the new message badge is enabled
        :param bool notifications_added_to_channel_enabled: Whether to send a notification when a member is added to a channel
        :param unicode notifications_added_to_channel_template: The template to use to create the notification text displayed when a member is added to a channel
        :param unicode notifications_added_to_channel_sound: The name of the sound to play when a member is added to a channel
        :param bool notifications_removed_from_channel_enabled: Whether to send a notification to a user when they are removed from a channel
        :param unicode notifications_removed_from_channel_template: The template to use to create the notification text displayed to a user when they are removed
        :param unicode notifications_removed_from_channel_sound: The name of the sound to play to a user when they are removed from a channel
        :param bool notifications_invited_to_channel_enabled: Whether to send a notification when a user is invited to a channel
        :param unicode notifications_invited_to_channel_template: The template to use to create the notification text displayed when a user is invited to a channel
        :param unicode notifications_invited_to_channel_sound: The name of the sound to play when a user is invited to a channel
        :param unicode pre_webhook_url: The webhook URL for pre-event webhooks
        :param unicode post_webhook_url: The URL for post-event webhooks
        :param unicode webhook_method: The HTTP method  to use for both PRE and POST webhooks
        :param unicode webhook_filters: The list of webhook events that are enabled for this Service instance
        :param unicode limits_channel_members: The maximum number of Members that can be added to Channels within this Service
        :param unicode limits_user_channels: The maximum number of Channels Users can be a Member of within this Service
        :param unicode media_compatibility_message: The message to send when a media message has no text
        :param unicode pre_webhook_retry_count: Count of times webhook will be retried in case of timeout or 429/503/504 HTTP responses
        :param unicode post_webhook_retry_count: The number of times calls to the `post_webhook_url` will be retried
        :param bool notifications_log_enabled: Whether to log notifications

        :returns: The updated ServiceInstance
        :rtype: twilio.rest.chat.v2.service.ServiceInstance
        """
        data = values.of({
            'FriendlyName': friendly_name,
            'DefaultServiceRoleSid': default_service_role_sid,
            'DefaultChannelRoleSid': default_channel_role_sid,
            'DefaultChannelCreatorRoleSid': default_channel_creator_role_sid,
            'ReadStatusEnabled': read_status_enabled,
            'ReachabilityEnabled': reachability_enabled,
            'TypingIndicatorTimeout': typing_indicator_timeout,
            'ConsumptionReportInterval': consumption_report_interval,
            'Notifications.NewMessage.Enabled': notifications_new_message_enabled,
            'Notifications.NewMessage.Template': notifications_new_message_template,
            'Notifications.NewMessage.Sound': notifications_new_message_sound,
            'Notifications.NewMessage.BadgeCountEnabled': notifications_new_message_badge_count_enabled,
            'Notifications.AddedToChannel.Enabled': notifications_added_to_channel_enabled,
            'Notifications.AddedToChannel.Template': notifications_added_to_channel_template,
            'Notifications.AddedToChannel.Sound': notifications_added_to_channel_sound,
            'Notifications.RemovedFromChannel.Enabled': notifications_removed_from_channel_enabled,
            'Notifications.RemovedFromChannel.Template': notifications_removed_from_channel_template,
            'Notifications.RemovedFromChannel.Sound': notifications_removed_from_channel_sound,
            'Notifications.InvitedToChannel.Enabled': notifications_invited_to_channel_enabled,
            'Notifications.InvitedToChannel.Template': notifications_invited_to_channel_template,
            'Notifications.InvitedToChannel.Sound': notifications_invited_to_channel_sound,
            'PreWebhookUrl': pre_webhook_url,
            'PostWebhookUrl': post_webhook_url,
            'WebhookMethod': webhook_method,
            'WebhookFilters': serialize.map(webhook_filters, lambda e: e),
            'Limits.ChannelMembers': limits_channel_members,
            'Limits.UserChannels': limits_user_channels,
            'Media.CompatibilityMessage': media_compatibility_message,
            'PreWebhookRetryCount': pre_webhook_retry_count,
            'PostWebhookRetryCount': post_webhook_retry_count,
            'Notifications.LogEnabled': notifications_log_enabled,
        })

        payload = self._version.update(method='POST', uri=self._uri, data=data, )

        return ServiceInstance(self._version, payload, sid=self._solution['sid'], )

    @property
    def channels(self):
        """
        Access the channels

        :returns: twilio.rest.chat.v2.service.channel.ChannelList
        :rtype: twilio.rest.chat.v2.service.channel.ChannelList
        """
        if self._channels is None:
            self._channels = ChannelList(self._version, service_sid=self._solution['sid'], )
        return self._channels

    @property
    def roles(self):
        """
        Access the roles

        :returns: twilio.rest.chat.v2.service.role.RoleList
        :rtype: twilio.rest.chat.v2.service.role.RoleList
        """
        if self._roles is None:
            self._roles = RoleList(self._version, service_sid=self._solution['sid'], )
        return self._roles

    @property
    def users(self):
        """
        Access the users

        :returns: twilio.rest.chat.v2.service.user.UserList
        :rtype: twilio.rest.chat.v2.service.user.UserList
        """
        if self._users is None:
            self._users = UserList(self._version, service_sid=self._solution['sid'], )
        return self._users

    @property
    def bindings(self):
        """
        Access the bindings

        :returns: twilio.rest.chat.v2.service.binding.BindingList
        :rtype: twilio.rest.chat.v2.service.binding.BindingList
        """
        if self._bindings is None:
            self._bindings = BindingList(self._version, service_sid=self._solution['sid'], )
        return self._bindings

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.IpMessaging.V2.ServiceContext {}>'.format(context)


class ServiceInstance(InstanceResource):

    def __init__(self, version, payload, sid=None):
        """
        Initialize the ServiceInstance

        :returns: twilio.rest.chat.v2.service.ServiceInstance
        :rtype: twilio.rest.chat.v2.service.ServiceInstance
        """
        super(ServiceInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'friendly_name': payload.get('friendly_name'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'default_service_role_sid': payload.get('default_service_role_sid'),
            'default_channel_role_sid': payload.get('default_channel_role_sid'),
            'default_channel_creator_role_sid': payload.get('default_channel_creator_role_sid'),
            'read_status_enabled': payload.get('read_status_enabled'),
            'reachability_enabled': payload.get('reachability_enabled'),
            'typing_indicator_timeout': deserialize.integer(payload.get('typing_indicator_timeout')),
            'consumption_report_interval': deserialize.integer(payload.get('consumption_report_interval')),
            'limits': payload.get('limits'),
            'pre_webhook_url': payload.get('pre_webhook_url'),
            'post_webhook_url': payload.get('post_webhook_url'),
            'webhook_method': payload.get('webhook_method'),
            'webhook_filters': payload.get('webhook_filters'),
            'pre_webhook_retry_count': deserialize.integer(payload.get('pre_webhook_retry_count')),
            'post_webhook_retry_count': deserialize.integer(payload.get('post_webhook_retry_count')),
            'notifications': payload.get('notifications'),
            'media': payload.get('media'),
            'url': payload.get('url'),
            'links': payload.get('links'),
        }

        # Context
        self._context = None
        self._solution = {'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: ServiceContext for this ServiceInstance
        :rtype: twilio.rest.chat.v2.service.ServiceContext
        """
        if self._context is None:
            self._context = ServiceContext(self._version, sid=self._solution['sid'], )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def date_created(self):
        """
        :returns: The RFC 2822 date and time in GMT when the resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The RFC 2822 date and time in GMT when the resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def default_service_role_sid(self):
        """
        :returns: The service role assigned to users when they are added to the service
        :rtype: unicode
        """
        return self._properties['default_service_role_sid']

    @property
    def default_channel_role_sid(self):
        """
        :returns: The channel role assigned to users when they are added to a channel
        :rtype: unicode
        """
        return self._properties['default_channel_role_sid']

    @property
    def default_channel_creator_role_sid(self):
        """
        :returns: The channel role assigned to a channel creator when they join a new channel
        :rtype: unicode
        """
        return self._properties['default_channel_creator_role_sid']

    @property
    def read_status_enabled(self):
        """
        :returns: Whether the Message Consumption Horizon feature is enabled
        :rtype: bool
        """
        return self._properties['read_status_enabled']

    @property
    def reachability_enabled(self):
        """
        :returns: Whether the Reachability Indicator feature is enabled for this Service instance
        :rtype: bool
        """
        return self._properties['reachability_enabled']

    @property
    def typing_indicator_timeout(self):
        """
        :returns: How long in seconds to wait before assuming the user is no longer typing
        :rtype: unicode
        """
        return self._properties['typing_indicator_timeout']

    @property
    def consumption_report_interval(self):
        """
        :returns: DEPRECATED
        :rtype: unicode
        """
        return self._properties['consumption_report_interval']

    @property
    def limits(self):
        """
        :returns: An object that describes the limits of the service instance
        :rtype: dict
        """
        return self._properties['limits']

    @property
    def pre_webhook_url(self):
        """
        :returns: The webhook URL for pre-event webhooks
        :rtype: unicode
        """
        return self._properties['pre_webhook_url']

    @property
    def post_webhook_url(self):
        """
        :returns: The URL for post-event webhooks
        :rtype: unicode
        """
        return self._properties['post_webhook_url']

    @property
    def webhook_method(self):
        """
        :returns: The HTTP method  to use for both PRE and POST webhooks
        :rtype: unicode
        """
        return self._properties['webhook_method']

    @property
    def webhook_filters(self):
        """
        :returns: The list of webhook events that are enabled for this Service instance
        :rtype: unicode
        """
        return self._properties['webhook_filters']

    @property
    def pre_webhook_retry_count(self):
        """
        :returns: Count of times webhook will be retried in case of timeout or 429/503/504 HTTP responses
        :rtype: unicode
        """
        return self._properties['pre_webhook_retry_count']

    @property
    def post_webhook_retry_count(self):
        """
        :returns: The number of times calls to the `post_webhook_url` will be retried
        :rtype: unicode
        """
        return self._properties['post_webhook_retry_count']

    @property
    def notifications(self):
        """
        :returns: The notification configuration for the Service instance
        :rtype: dict
        """
        return self._properties['notifications']

    @property
    def media(self):
        """
        :returns: The properties of the media that the service supports
        :rtype: dict
        """
        return self._properties['media']

    @property
    def url(self):
        """
        :returns: The absolute URL of the Service resource
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def links(self):
        """
        :returns: The absolute URLs of the Service's Channels, Roles, and Users
        :rtype: unicode
        """
        return self._properties['links']

    def fetch(self):
        """
        Fetch the ServiceInstance

        :returns: The fetched ServiceInstance
        :rtype: twilio.rest.chat.v2.service.ServiceInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the ServiceInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def update(self, friendly_name=values.unset,
               default_service_role_sid=values.unset,
               default_channel_role_sid=values.unset,
               default_channel_creator_role_sid=values.unset,
               read_status_enabled=values.unset, reachability_enabled=values.unset,
               typing_indicator_timeout=values.unset,
               consumption_report_interval=values.unset,
               notifications_new_message_enabled=values.unset,
               notifications_new_message_template=values.unset,
               notifications_new_message_sound=values.unset,
               notifications_new_message_badge_count_enabled=values.unset,
               notifications_added_to_channel_enabled=values.unset,
               notifications_added_to_channel_template=values.unset,
               notifications_added_to_channel_sound=values.unset,
               notifications_removed_from_channel_enabled=values.unset,
               notifications_removed_from_channel_template=values.unset,
               notifications_removed_from_channel_sound=values.unset,
               notifications_invited_to_channel_enabled=values.unset,
               notifications_invited_to_channel_template=values.unset,
               notifications_invited_to_channel_sound=values.unset,
               pre_webhook_url=values.unset, post_webhook_url=values.unset,
               webhook_method=values.unset, webhook_filters=values.unset,
               limits_channel_members=values.unset,
               limits_user_channels=values.unset,
               media_compatibility_message=values.unset,
               pre_webhook_retry_count=values.unset,
               post_webhook_retry_count=values.unset,
               notifications_log_enabled=values.unset):
        """
        Update the ServiceInstance

        :param unicode friendly_name: A string to describe the resource
        :param unicode default_service_role_sid: The service role assigned to users when they are added to the service
        :param unicode default_channel_role_sid: The channel role assigned to users when they are added to a channel
        :param unicode default_channel_creator_role_sid: The channel role assigned to a channel creator when they join a new channel
        :param bool read_status_enabled: Whether to enable the Message Consumption Horizon feature
        :param bool reachability_enabled: Whether to enable the Reachability Indicator feature for this Service instance
        :param unicode typing_indicator_timeout: How long in seconds to wait before assuming the user is no longer typing
        :param unicode consumption_report_interval: DEPRECATED
        :param bool notifications_new_message_enabled: Whether to send a notification when a new message is added to a channel
        :param unicode notifications_new_message_template: The template to use to create the notification text displayed when a new message is added to a channel
        :param unicode notifications_new_message_sound: The name of the sound to play when a new message is added to a channel
        :param bool notifications_new_message_badge_count_enabled: Whether the new message badge is enabled
        :param bool notifications_added_to_channel_enabled: Whether to send a notification when a member is added to a channel
        :param unicode notifications_added_to_channel_template: The template to use to create the notification text displayed when a member is added to a channel
        :param unicode notifications_added_to_channel_sound: The name of the sound to play when a member is added to a channel
        :param bool notifications_removed_from_channel_enabled: Whether to send a notification to a user when they are removed from a channel
        :param unicode notifications_removed_from_channel_template: The template to use to create the notification text displayed to a user when they are removed
        :param unicode notifications_removed_from_channel_sound: The name of the sound to play to a user when they are removed from a channel
        :param bool notifications_invited_to_channel_enabled: Whether to send a notification when a user is invited to a channel
        :param unicode notifications_invited_to_channel_template: The template to use to create the notification text displayed when a user is invited to a channel
        :param unicode notifications_invited_to_channel_sound: The name of the sound to play when a user is invited to a channel
        :param unicode pre_webhook_url: The webhook URL for pre-event webhooks
        :param unicode post_webhook_url: The URL for post-event webhooks
        :param unicode webhook_method: The HTTP method  to use for both PRE and POST webhooks
        :param unicode webhook_filters: The list of webhook events that are enabled for this Service instance
        :param unicode limits_channel_members: The maximum number of Members that can be added to Channels within this Service
        :param unicode limits_user_channels: The maximum number of Channels Users can be a Member of within this Service
        :param unicode media_compatibility_message: The message to send when a media message has no text
        :param unicode pre_webhook_retry_count: Count of times webhook will be retried in case of timeout or 429/503/504 HTTP responses
        :param unicode post_webhook_retry_count: The number of times calls to the `post_webhook_url` will be retried
        :param bool notifications_log_enabled: Whether to log notifications

        :returns: The updated ServiceInstance
        :rtype: twilio.rest.chat.v2.service.ServiceInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            default_service_role_sid=default_service_role_sid,
            default_channel_role_sid=default_channel_role_sid,
            default_channel_creator_role_sid=default_channel_creator_role_sid,
            read_status_enabled=read_status_enabled,
            reachability_enabled=reachability_enabled,
            typing_indicator_timeout=typing_indicator_timeout,
            consumption_report_interval=consumption_report_interval,
            notifications_new_message_enabled=notifications_new_message_enabled,
            notifications_new_message_template=notifications_new_message_template,
            notifications_new_message_sound=notifications_new_message_sound,
            notifications_new_message_badge_count_enabled=notifications_new_message_badge_count_enabled,
            notifications_added_to_channel_enabled=notifications_added_to_channel_enabled,
            notifications_added_to_channel_template=notifications_added_to_channel_template,
            notifications_added_to_channel_sound=notifications_added_to_channel_sound,
            notifications_removed_from_channel_enabled=notifications_removed_from_channel_enabled,
            notifications_removed_from_channel_template=notifications_removed_from_channel_template,
            notifications_removed_from_channel_sound=notifications_removed_from_channel_sound,
            notifications_invited_to_channel_enabled=notifications_invited_to_channel_enabled,
            notifications_invited_to_channel_template=notifications_invited_to_channel_template,
            notifications_invited_to_channel_sound=notifications_invited_to_channel_sound,
            pre_webhook_url=pre_webhook_url,
            post_webhook_url=post_webhook_url,
            webhook_method=webhook_method,
            webhook_filters=webhook_filters,
            limits_channel_members=limits_channel_members,
            limits_user_channels=limits_user_channels,
            media_compatibility_message=media_compatibility_message,
            pre_webhook_retry_count=pre_webhook_retry_count,
            post_webhook_retry_count=post_webhook_retry_count,
            notifications_log_enabled=notifications_log_enabled,
        )

    @property
    def channels(self):
        """
        Access the channels

        :returns: twilio.rest.chat.v2.service.channel.ChannelList
        :rtype: twilio.rest.chat.v2.service.channel.ChannelList
        """
        return self._proxy.channels

    @property
    def roles(self):
        """
        Access the roles

        :returns: twilio.rest.chat.v2.service.role.RoleList
        :rtype: twilio.rest.chat.v2.service.role.RoleList
        """
        return self._proxy.roles

    @property
    def users(self):
        """
        Access the users

        :returns: twilio.rest.chat.v2.service.user.UserList
        :rtype: twilio.rest.chat.v2.service.user.UserList
        """
        return self._proxy.users

    @property
    def bindings(self):
        """
        Access the bindings

        :returns: twilio.rest.chat.v2.service.binding.BindingList
        :rtype: twilio.rest.chat.v2.service.binding.BindingList
        """
        return self._proxy.bindings

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.IpMessaging.V2.ServiceInstance {}>'.format(context)
