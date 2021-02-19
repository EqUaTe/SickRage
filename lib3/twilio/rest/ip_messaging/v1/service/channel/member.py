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


class MemberList(ListResource):

    def __init__(self, version, service_sid, channel_sid):
        """
        Initialize the MemberList

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the Service that the resource is associated with
        :param channel_sid: The unique ID of the Channel for the member

        :returns: twilio.rest.chat.v1.service.channel.member.MemberList
        :rtype: twilio.rest.chat.v1.service.channel.member.MemberList
        """
        super(MemberList, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'channel_sid': channel_sid, }
        self._uri = '/Services/{service_sid}/Channels/{channel_sid}/Members'.format(**self._solution)

    def create(self, identity, role_sid=values.unset):
        """
        Create the MemberInstance

        :param unicode identity: The `identity` value that identifies the new resource's User
        :param unicode role_sid: The SID of the Role to assign to the member

        :returns: The created MemberInstance
        :rtype: twilio.rest.chat.v1.service.channel.member.MemberInstance
        """
        data = values.of({'Identity': identity, 'RoleSid': role_sid, })

        payload = self._version.create(method='POST', uri=self._uri, data=data, )

        return MemberInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            channel_sid=self._solution['channel_sid'],
        )

    def stream(self, identity=values.unset, limit=None, page_size=None):
        """
        Streams MemberInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param unicode identity: The `identity` value of the resources to read
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.chat.v1.service.channel.member.MemberInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(identity=identity, page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'])

    def list(self, identity=values.unset, limit=None, page_size=None):
        """
        Lists MemberInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param unicode identity: The `identity` value of the resources to read
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.chat.v1.service.channel.member.MemberInstance]
        """
        return list(self.stream(identity=identity, limit=limit, page_size=page_size, ))

    def page(self, identity=values.unset, page_token=values.unset,
             page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of MemberInstance records from the API.
        Request is executed immediately

        :param unicode identity: The `identity` value of the resources to read
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of MemberInstance
        :rtype: twilio.rest.chat.v1.service.channel.member.MemberPage
        """
        data = values.of({
            'Identity': serialize.map(identity, lambda e: e),
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return MemberPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of MemberInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of MemberInstance
        :rtype: twilio.rest.chat.v1.service.channel.member.MemberPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return MemberPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a MemberContext

        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.chat.v1.service.channel.member.MemberContext
        :rtype: twilio.rest.chat.v1.service.channel.member.MemberContext
        """
        return MemberContext(
            self._version,
            service_sid=self._solution['service_sid'],
            channel_sid=self._solution['channel_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a MemberContext

        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.chat.v1.service.channel.member.MemberContext
        :rtype: twilio.rest.chat.v1.service.channel.member.MemberContext
        """
        return MemberContext(
            self._version,
            service_sid=self._solution['service_sid'],
            channel_sid=self._solution['channel_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.IpMessaging.V1.MemberList>'


class MemberPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the MemberPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param service_sid: The SID of the Service that the resource is associated with
        :param channel_sid: The unique ID of the Channel for the member

        :returns: twilio.rest.chat.v1.service.channel.member.MemberPage
        :rtype: twilio.rest.chat.v1.service.channel.member.MemberPage
        """
        super(MemberPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of MemberInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.chat.v1.service.channel.member.MemberInstance
        :rtype: twilio.rest.chat.v1.service.channel.member.MemberInstance
        """
        return MemberInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            channel_sid=self._solution['channel_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.IpMessaging.V1.MemberPage>'


class MemberContext(InstanceContext):

    def __init__(self, version, service_sid, channel_sid, sid):
        """
        Initialize the MemberContext

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the Service to fetch the resource from
        :param channel_sid: The unique ID of the channel the member belongs to
        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.chat.v1.service.channel.member.MemberContext
        :rtype: twilio.rest.chat.v1.service.channel.member.MemberContext
        """
        super(MemberContext, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'channel_sid': channel_sid, 'sid': sid, }
        self._uri = '/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch the MemberInstance

        :returns: The fetched MemberInstance
        :rtype: twilio.rest.chat.v1.service.channel.member.MemberInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return MemberInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            channel_sid=self._solution['channel_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the MemberInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )

    def update(self, role_sid=values.unset,
               last_consumed_message_index=values.unset):
        """
        Update the MemberInstance

        :param unicode role_sid: The SID of the Role to assign to the member
        :param unicode last_consumed_message_index: The index of the last consumed Message for the Channel for the Member

        :returns: The updated MemberInstance
        :rtype: twilio.rest.chat.v1.service.channel.member.MemberInstance
        """
        data = values.of({'RoleSid': role_sid, 'LastConsumedMessageIndex': last_consumed_message_index, })

        payload = self._version.update(method='POST', uri=self._uri, data=data, )

        return MemberInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            channel_sid=self._solution['channel_sid'],
            sid=self._solution['sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.IpMessaging.V1.MemberContext {}>'.format(context)


class MemberInstance(InstanceResource):

    def __init__(self, version, payload, service_sid, channel_sid, sid=None):
        """
        Initialize the MemberInstance

        :returns: twilio.rest.chat.v1.service.channel.member.MemberInstance
        :rtype: twilio.rest.chat.v1.service.channel.member.MemberInstance
        """
        super(MemberInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'channel_sid': payload.get('channel_sid'),
            'service_sid': payload.get('service_sid'),
            'identity': payload.get('identity'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'role_sid': payload.get('role_sid'),
            'last_consumed_message_index': deserialize.integer(payload.get('last_consumed_message_index')),
            'last_consumption_timestamp': deserialize.iso8601_datetime(payload.get('last_consumption_timestamp')),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {
            'service_sid': service_sid,
            'channel_sid': channel_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: MemberContext for this MemberInstance
        :rtype: twilio.rest.chat.v1.service.channel.member.MemberContext
        """
        if self._context is None:
            self._context = MemberContext(
                self._version,
                service_sid=self._solution['service_sid'],
                channel_sid=self._solution['channel_sid'],
                sid=self._solution['sid'],
            )
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
    def channel_sid(self):
        """
        :returns: The unique ID of the Channel for the member
        :rtype: unicode
        """
        return self._properties['channel_sid']

    @property
    def service_sid(self):
        """
        :returns: The SID of the Service that the resource is associated with
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def identity(self):
        """
        :returns: The string that identifies the resource's User
        :rtype: unicode
        """
        return self._properties['identity']

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
    def role_sid(self):
        """
        :returns: The SID of the Role assigned to the member
        :rtype: unicode
        """
        return self._properties['role_sid']

    @property
    def last_consumed_message_index(self):
        """
        :returns: The index of the last Message that the Member has read within the Channel
        :rtype: unicode
        """
        return self._properties['last_consumed_message_index']

    @property
    def last_consumption_timestamp(self):
        """
        :returns: The ISO 8601 based timestamp string that represents the date-time of the last Message read event for the Member within the Channel
        :rtype: datetime
        """
        return self._properties['last_consumption_timestamp']

    @property
    def url(self):
        """
        :returns: The absolute URL of the Member resource
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch the MemberInstance

        :returns: The fetched MemberInstance
        :rtype: twilio.rest.chat.v1.service.channel.member.MemberInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the MemberInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def update(self, role_sid=values.unset,
               last_consumed_message_index=values.unset):
        """
        Update the MemberInstance

        :param unicode role_sid: The SID of the Role to assign to the member
        :param unicode last_consumed_message_index: The index of the last consumed Message for the Channel for the Member

        :returns: The updated MemberInstance
        :rtype: twilio.rest.chat.v1.service.channel.member.MemberInstance
        """
        return self._proxy.update(
            role_sid=role_sid,
            last_consumed_message_index=last_consumed_message_index,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.IpMessaging.V1.MemberInstance {}>'.format(context)
