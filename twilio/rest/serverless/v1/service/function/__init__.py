# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page
from twilio.rest.serverless.v1.service.function.function_version import FunctionVersionList


class FunctionList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, service_sid):
        """
        Initialize the FunctionList

        :param Version version: Version that contains the resource
        :param service_sid: The service_sid

        :returns: twilio.rest.serverless.v1.service.function.FunctionList
        :rtype: twilio.rest.serverless.v1.service.function.FunctionList
        """
        super(FunctionList, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, }
        self._uri = '/Services/{service_sid}/Functions'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams FunctionInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.serverless.v1.service.function.FunctionInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists FunctionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.serverless.v1.service.function.FunctionInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of FunctionInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of FunctionInstance
        :rtype: twilio.rest.serverless.v1.service.function.FunctionPage
        """
        params = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return FunctionPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of FunctionInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of FunctionInstance
        :rtype: twilio.rest.serverless.v1.service.function.FunctionPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return FunctionPage(self._version, response, self._solution)

    def create(self, friendly_name):
        """
        Create a new FunctionInstance

        :param unicode friendly_name: The friendly_name

        :returns: Newly created FunctionInstance
        :rtype: twilio.rest.serverless.v1.service.function.FunctionInstance
        """
        data = values.of({'FriendlyName': friendly_name, })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return FunctionInstance(self._version, payload, service_sid=self._solution['service_sid'], )

    def get(self, sid):
        """
        Constructs a FunctionContext

        :param sid: The sid

        :returns: twilio.rest.serverless.v1.service.function.FunctionContext
        :rtype: twilio.rest.serverless.v1.service.function.FunctionContext
        """
        return FunctionContext(self._version, service_sid=self._solution['service_sid'], sid=sid, )

    def __call__(self, sid):
        """
        Constructs a FunctionContext

        :param sid: The sid

        :returns: twilio.rest.serverless.v1.service.function.FunctionContext
        :rtype: twilio.rest.serverless.v1.service.function.FunctionContext
        """
        return FunctionContext(self._version, service_sid=self._solution['service_sid'], sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Serverless.V1.FunctionList>'


class FunctionPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the FunctionPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param service_sid: The service_sid

        :returns: twilio.rest.serverless.v1.service.function.FunctionPage
        :rtype: twilio.rest.serverless.v1.service.function.FunctionPage
        """
        super(FunctionPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of FunctionInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.serverless.v1.service.function.FunctionInstance
        :rtype: twilio.rest.serverless.v1.service.function.FunctionInstance
        """
        return FunctionInstance(self._version, payload, service_sid=self._solution['service_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Serverless.V1.FunctionPage>'


class FunctionContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, service_sid, sid):
        """
        Initialize the FunctionContext

        :param Version version: Version that contains the resource
        :param service_sid: The service_sid
        :param sid: The sid

        :returns: twilio.rest.serverless.v1.service.function.FunctionContext
        :rtype: twilio.rest.serverless.v1.service.function.FunctionContext
        """
        super(FunctionContext, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'sid': sid, }
        self._uri = '/Services/{service_sid}/Functions/{sid}'.format(**self._solution)

        # Dependents
        self._function_versions = None

    def fetch(self):
        """
        Fetch a FunctionInstance

        :returns: Fetched FunctionInstance
        :rtype: twilio.rest.serverless.v1.service.function.FunctionInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return FunctionInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
        )

    def update(self, friendly_name):
        """
        Update the FunctionInstance

        :param unicode friendly_name: The friendly_name

        :returns: Updated FunctionInstance
        :rtype: twilio.rest.serverless.v1.service.function.FunctionInstance
        """
        data = values.of({'FriendlyName': friendly_name, })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return FunctionInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
        )

    @property
    def function_versions(self):
        """
        Access the function_versions

        :returns: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionList
        :rtype: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionList
        """
        if self._function_versions is None:
            self._function_versions = FunctionVersionList(
                self._version,
                service_sid=self._solution['service_sid'],
                function_sid=self._solution['sid'],
            )
        return self._function_versions

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Serverless.V1.FunctionContext {}>'.format(context)


class FunctionInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, payload, service_sid, sid=None):
        """
        Initialize the FunctionInstance

        :returns: twilio.rest.serverless.v1.service.function.FunctionInstance
        :rtype: twilio.rest.serverless.v1.service.function.FunctionInstance
        """
        super(FunctionInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'account_sid': payload['account_sid'],
            'service_sid': payload['service_sid'],
            'friendly_name': payload['friendly_name'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'url': payload['url'],
            'links': payload['links'],
        }

        # Context
        self._context = None
        self._solution = {'service_sid': service_sid, 'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: FunctionContext for this FunctionInstance
        :rtype: twilio.rest.serverless.v1.service.function.FunctionContext
        """
        if self._context is None:
            self._context = FunctionContext(
                self._version,
                service_sid=self._solution['service_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def service_sid(self):
        """
        :returns: The service_sid
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def friendly_name(self):
        """
        :returns: The friendly_name
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def date_created(self):
        """
        :returns: The date_created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date_updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def links(self):
        """
        :returns: The links
        :rtype: unicode
        """
        return self._properties['links']

    def fetch(self):
        """
        Fetch a FunctionInstance

        :returns: Fetched FunctionInstance
        :rtype: twilio.rest.serverless.v1.service.function.FunctionInstance
        """
        return self._proxy.fetch()

    def update(self, friendly_name):
        """
        Update the FunctionInstance

        :param unicode friendly_name: The friendly_name

        :returns: Updated FunctionInstance
        :rtype: twilio.rest.serverless.v1.service.function.FunctionInstance
        """
        return self._proxy.update(friendly_name, )

    @property
    def function_versions(self):
        """
        Access the function_versions

        :returns: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionList
        :rtype: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionList
        """
        return self._proxy.function_versions

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Serverless.V1.FunctionInstance {}>'.format(context)
