#!/usr/bin/env python3
"""Test module for client.py"""
import unittest
from typing import Dict
from parameterized import parameterized
from fixtures import TEST_PAYLOAD
from client import GithubOrgClient
from unittest.mock import (
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
    def test_org(self, org_name, mock_get_json) -> None:
        mock_response = {"key": "value"}
        mock_get_json.return_value = mock_response
        client = GithubOrgClient(org_name)
        result = client.org
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, mock_response)

    @parameterized.expand([
        ("google", "https://api.github.com/orgs/google/repos"),
        ("abc", "https://api.github.com/orgs/abc/repos"),
    ])
    def test_public_repos_url(self, org_name, expected_url) -> None:
        """Test public repos property value"""
        # Arrange
        mock_payload = {
            "repos_url": expected_url
        }
        # Act
        with patch.object(GithubOrgClient, 'org', return_value=mock_payload):
            client = GithubOrgClient(org_name)
            result = client._public_repos_url
        # Assert
        self.assertEqual(result, expected_url)

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json) -> None:
        """Test GithubOrgClient.public_repos returns the correct value."""
        # Arrange
        org_payload = {
            "repos_url": "https://api.github.com/orgs/test/repos"
        }
        repos_payload = [
            {"name": "google"},
            {"name": "Twitter"}
        ]

        # Set up the mock for get_json
        mock_get_json.side_effect = [org_payload, repos_payload]

        # Create an instance of GithubOrgClient
        test_class = GithubOrgClient('test')

        # Use patch as a context manager to mock _public_repos_url
        with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock) as mock_public:
            mock_public.return_value = org_payload["repos_url"]

            # Act
            result = test_class.public_repos()

            # Assert
            expected = [x["name"] for x in repos_payload]
            self.assertEqual(result, expected)

            # Check that get_json was called twice (once for org and once for repos)
            self.assertEqual(mock_get_json.call_count, 2)

            # Check that _public_repos_url was called once
            self.assertEqual(mock_public.call_count, 1)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        # Act
        result = GithubOrgClient.has_license(repo, license_key)
        # Assert
        self.assertEqual(result, expected)
