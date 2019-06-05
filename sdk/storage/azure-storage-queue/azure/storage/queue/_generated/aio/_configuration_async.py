# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from azure.core.configuration import Configuration, ConnectionConfiguration
from azure.core.pipeline import policies

from ..version import VERSION


class AzureQueueStorageConfiguration(Configuration):
    """Configuration for AzureQueueStorage
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param url: The URL of the service account, queue or message that is the
     targe of the desired operation.
    :type url: str
    :ivar version: Specifies the version of the operation to use for this
     request.
    :type version: str
    """

    def __init__(self, url, **kwargs):

        if url is None:
            raise ValueError("Parameter 'url' must not be None.")

        super(AzureQueueStorageConfiguration, self).__init__(**kwargs)
        self._configure(**kwargs)

        self.user_agent_policy.add_user_agent('azurequeuestorage/{}'.format(VERSION))
        self.generate_client_request_id = True
        self.accept_language = None

        self.url = url
        self.version = "2018-03-28"

    def _configure(self, **kwargs):
        self.connection = ConnectionConfiguration(**kwargs)
        self.user_agent_policy = policies.UserAgentPolicy(**kwargs)
        self.headers_policy = policies.HeadersPolicy(**kwargs)
        self.proxy_policy = policies.ProxyPolicy(**kwargs)
        self.logging_policy = policies.NetworkTraceLoggingPolicy(**kwargs)
        self.retry_policy = policies.AsyncRetryPolicy(**kwargs)
        self.redirect_policy = policies.AsyncRedirectPolicy(**kwargs)
