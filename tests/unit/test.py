# Copyright 2016: Mirantis Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import mock
import testtools

import time
import os
import sys

from spamostack import main
import fakes
import tests

TEST_CONFIG_PATH = os.path.join(os.path.dirname(tests.__file__), '..',
                                'etc', 'conf.json')

FAKE_CREDS = {"OS_USERNAME": "admin",
              "OS_PASSWORD": "admin",
              "OS_PROJECT_NAME": "fake",
              "OS_PROJECT_DOMAIN_ID": "fake",
              "OS_USER_DOMAIN_ID": "fake",
              "OS_AUTH_URL": "http://fake/v3",
              "OS_COMPUTE_API_VERSION": "2",
              "OS_IDENTITY_API_VERSION": "3",
              "OS_IMAGE_API_VERSION": "2",
              "OS_NETWORK_API_VERSION": "2",
              "OS_VOLUME_API_VERSION": "2"}


class RunTestCase(testtools.TestCase):

    def setUp(self):
        super(RunTestCase, self).setUp()

        for k, v in FAKE_CREDS.iteritems():
            os.environ[k] = v

        self.addCleanup(mock.patch.stopall)

    @mock.patch('spamostack.client_factory.Swift', autospec=True,
                return_value=fakes.FakeClient())
    @mock.patch('spamostack.client_factory.Keystone', autospec=True,
                return_value=fakes.FakeKeystone())
    @mock.patch('spamostack.client_factory.Glance', autospec=True,
                return_value=fakes.FakeClient())
    @mock.patch('spamostack.client_factory.Nova', autospec=True,
                return_value=fakes.FakeClient())
    @mock.patch('spamostack.client_factory.Neutron', autospec=True,
                return_value=fakes.FakeClient())
    @mock.patch('spamostack.client_factory.Cinder', autospec=True,
                return_value=fakes.FakeClient())
    @mock.patch('keystoneclient.client.Client', autospec=True,
                return_value=fakes.FakeKeystone())
    @mock.patch('sys.exit', return_value=None)
    def test_main(self, mock_sys, mock_kc, mock_ccc, mock_cnc,
                     mock_cnovac, mock_cgc, mock_ckc, mock_csc):
        sys.argv = ['spamostack/main.py', '--conf={}'.format(TEST_CONFIG_PATH)]
        main.main()

    @mock.patch('spamostack.client_factory.Swift', autospec=True,
                return_value=fakes.FakeClient())
    @mock.patch('spamostack.client_factory.Keystone', autospec=True,
                return_value=fakes.FakeKeystone())
    @mock.patch('spamostack.client_factory.Glance', autospec=True,
                return_value=fakes.FakeClient())
    @mock.patch('spamostack.client_factory.Nova', autospec=True,
                return_value=fakes.FakeClient())
    @mock.patch('spamostack.client_factory.Neutron', autospec=True,
                return_value=fakes.FakeClient())
    @mock.patch('spamostack.client_factory.Cinder', autospec=True,
                return_value=fakes.FakeClient())
    @mock.patch('keystoneclient.client.Client', autospec=True,
                return_value=fakes.FakeKeystone())
    @mock.patch('sys.exit', return_value=None)
    def test_verbose(self, mock_sys, mock_kc, mock_ccc, mock_cnc,
                   mock_cnovac, mock_cgc, mock_ckc, mock_csc):
        sys.argv = ['spamostack/main.py', '--conf={}'.format(TEST_CONFIG_PATH),
                    '--verbose']
        main.main()

class CleanTestCase(testtools.TestCase):

    def setUp(self):
        super(CleanTestCase, self).setUp()

        for k, v in FAKE_CREDS.iteritems():
            os.environ[k] = v

        self.addCleanup(mock.patch.stopall)

    @mock.patch('spamostack.client_factory.Swift', autospec=True,
                return_value=fakes.FakeClient())
    @mock.patch('spamostack.client_factory.Keystone', autospec=True,
                return_value=fakes.FakeKeystone())
    @mock.patch('spamostack.client_factory.Glance', autospec=True,
                return_value=fakes.FakeClient())
    @mock.patch('spamostack.client_factory.Nova', autospec=True,
                return_value=fakes.FakeClient())
    @mock.patch('spamostack.client_factory.Neutron', autospec=True,
                return_value=fakes.FakeClient())
    @mock.patch('spamostack.client_factory.Cinder', autospec=True,
                return_value=fakes.FakeClient())
    @mock.patch('keystoneclient.client.Client', autospec=True,
                return_value=fakes.FakeKeystone())
    @mock.patch('sys.exit', return_value=None)
    def test_clean(self, mock_sys, mock_kc, mock_ccc, mock_cnc,
                     mock_cnovac, mock_cgc, mock_ckc, mock_csc):
        sys.argv = ['spamostack/main.py', '--clean all']
        main.main()
