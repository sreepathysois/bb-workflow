from behave import *
from features.common.ApiClient import ApiClient
from hamcrest import assert_that, equal_to, is_not

HOST = 'http://localhost/'


class Process(object):

    def __init__(self, endpoint_name):
        self._endpoint_name = endpoint_name
        self._url = f'{HOST}{endpoint_name}'

    def count_of_records(self):
        if self._endpoint_name is not None:
            return 1


@given('we have token from login')
def step_impl(context):
    pass


@when('we request list from {endpoint_name} endpoint')
def step_impl(context, endpoint_name):
    context.obj = Process(endpoint_name)
    assert True is not False


@then('we receive list of processes having {predefined_number} of processes')
def step_impl(context, predefined_number):
    obj = ApiClient('processes', protocol='https', port='', prefix='', suffix='')
    data = obj.all_records
    count = context.obj.count_of_records()
    assert count == 2
    assert context.failed is False