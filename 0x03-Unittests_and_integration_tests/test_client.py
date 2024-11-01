#!/usr/bin/env python3
"""Test module for client.py"""
import unittest
from typing import Dict
from parameterized import parameterized
from fixtures import TEST_PAYLOAD
from client import GithubOrgClient
from unittest.mock import (
    MagicMock,
    patch,
    PropertyMock,
)


class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        mock_response = {"key": "value"}
        mock_get_json.return_value = mock_response
        client = GithubOrgClient(org_name)
        result = client.org
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, mock_response)

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
