#!/usr/bin/env python3
"""Test module for client.py"""
import unittest
from typing import Dict
from requests import HTTPError
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD
from client import GithubOrgClient
from unittest.mock import (
    MagicMock,
    Mock,
    patch,
    PropertyMock,
)


class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient"""

    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"})
    ])
    @patch("utils.get_json")
    def test_org(self, org: str, resp: Dict,
                 mocked_fxn: MagicMock) -> None:
        """test org method"""

        mocked_fxn.return_value = resp
        client = GithubOrgClient(org)
        client.org()
        mocked_fxn.called_with_once(client.ORG_URL.format(org=org))

    def test_public_repos_url(self) -> None:
        """Tests the _public_repos_url property."""
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as mocked_org:
            mocked_org.return_value = {
                'repos_url': "https://api.github.com/users/google/repos"
            }
            client = GithubOrgClient("google")
            self.assertEqual(
                client._public_repos_url,
                "https://api.github.com/users/google/repos"
            )

    @patch("utils.get_json")
    def test_public_repos(self, mocked_fxn: MagicMock) -> None:
        """Tests the public_repos property."""
        mocked_fxn.return_value = MagicMock(return_value=TEST_PAYLOAD)
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos, TEST_PAYLOAD)
