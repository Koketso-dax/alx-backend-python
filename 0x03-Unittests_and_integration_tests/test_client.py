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

    @parameterized.expand([
        ([{"name": "google"}, {"name": "Twitter"}], "https://api.github.com/orgs/test/repos", ["google", "Twitter"]),
        ([{"name": "google"}], "https://api.github.com/orgs/test/repos", ["google"]),
        ([], "https://api.github.com/orgs/test/repos", []),
    ])
    @patch('client.get_json')
    def test_public_repos(self, payloads, mock_repos_url,
                          expected, mock_get_json):
        """Test GithubOrgClient.public_repos returns the correct value."""
        # Arrange
        mock_get_json.return_value = payloads
        # Act
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public:
            mock_public.return_value = mock_repos_url
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()
        # Assert
        self.assertEqual(result, expected)
        mock_get_json.assert_called_once_with(mock_repos_url)
        mock_public.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        # Act
        result = GithubOrgClient.has_license(repo, license_key)
        # Assert
        self.assertEqual(result, expected)
