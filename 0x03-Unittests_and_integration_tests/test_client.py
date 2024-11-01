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

    @parameterized.expand([
        ("google", "https://api.github.com/orgs/google/repos"),
        ("abc", "https://api.github.com/orgs/abc/repos"),
    ])
    def test_public_repos_url(self, org_name, expected_url):
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
    def test_public_repos(self, mock_json):
        """TestGithubOrgClient.test_public_repos
        return the correct value
        """

        payloads = [{"name": "google"}, {"name": "Twitter"}]
        mock_json.return_value = payloads

        with patch('client.GithubOrgClient._public_repos_url') as mock_public:
            mock_public.return_value = "hey there!"
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()

            expected = [p["name"] for p in payloads]
            self.assertEqual(result, expected)
            mock_json.called_with_once()
            mock_public.called_with_once()
