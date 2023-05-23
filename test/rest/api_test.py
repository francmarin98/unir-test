import http.client
import os
import unittest
from urllib.request import urlopen

import pytest

import urllib.error

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

# ADD

    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error in API request to {url}"
        )

        url = f"{BASE_URL}/calc/add/-2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error in API request to {url}"
        )

        url = f"{BASE_URL}/calc/add/-2/-2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error in API request to {url}"
        )


    def test_api_add_wrong(self):
        url = f"{BASE_URL}/calc/add/a/2"
        with self.assertRaises(urllib.error.HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            context.exception.code, http.client.BAD_REQUEST, f"Error in API request to {url}"
        )

        url = f"{BASE_URL}/calc/add/a/a"
        with self.assertRaises(urllib.error.HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            context.exception.code, http.client.BAD_REQUEST, f"Error in API request to {url}"
        )

        url = f"{BASE_URL}/calc/add/a/2"
        with self.assertRaises(urllib.error.HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            context.exception.code, http.client.BAD_REQUEST, f"Error in API request to {url}"
        )

 
# SUBSTRACT

    def test_api_substract(self):
        url = f"{BASE_URL}/calc/substract/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error in API request to {url}"
        )

    def test_api_substract_wrong(self):
        url = f"{BASE_URL}/calc/substract/a/2"
        with self.assertRaises(urllib.error.HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            context.exception.code, http.client.BAD_REQUEST, f"Error in API request to {url}"
        )

        url = f"{BASE_URL}/calc/substract/a/a"
        with self.assertRaises(urllib.error.HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            context.exception.code, http.client.BAD_REQUEST, f"Error in API request to {url}"
        )

        url = f"{BASE_URL}/calc/substract/a/2"
        with self.assertRaises(urllib.error.HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            context.exception.code, http.client.BAD_REQUEST, f"Error in API request to {url}"
        )

# MULTIPLY

    def test_api_multiply(self):
        url = f"{BASE_URL}/calc/multiply/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error in API request to {url}"
        )

    def test_api_multiply_wrong(self):
        url = f"{BASE_URL}/calc/multiply/a/2"
        with self.assertRaises(urllib.error.HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            context.exception.code, http.client.BAD_REQUEST, f"Error in API request to {url}"
        )

        url = f"{BASE_URL}/calc/multiply/a/a"
        with self.assertRaises(urllib.error.HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            context.exception.code, http.client.BAD_REQUEST, f"Error in API request to {url}"
        )

        url = f"{BASE_URL}/calc/multiply/a/2"
        with self.assertRaises(urllib.error.HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            context.exception.code, http.client.BAD_REQUEST, f"Error in API request to {url}"
        )

# POWER

    def test_api_power(self):
        url = f"{BASE_URL}/calc/power/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error in API request to {url}"
        )

    def test_api_power_wrong(self):
        url = f"{BASE_URL}/calc/power/a/2"
        with self.assertRaises(urllib.error.HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            context.exception.code, http.client.BAD_REQUEST, f"Error in API request to {url}"
        )

        url = f"{BASE_URL}/calc/power/a/a"
        with self.assertRaises(urllib.error.HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            context.exception.code, http.client.BAD_REQUEST, f"Error in API request to {url}"
        )

        url = f"{BASE_URL}/calc/power/a/2"
        with self.assertRaises(urllib.error.HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            context.exception.code, http.client.BAD_REQUEST, f"Error in API request to {url}"
        )

# DIVIDE

    def test_api_divide(self):
        url = f"{BASE_URL}/calc/divide/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error in API request to {url}"
        )

    def test_api_divide_wrong(self):
        url = f"{BASE_URL}/calc/divide/a/2"
        with self.assertRaises(urllib.error.HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            context.exception.code, http.client.BAD_REQUEST, f"Error in API request to {url}"
        )

        url = f"{BASE_URL}/calc/divide/a/a"
        with self.assertRaises(urllib.error.HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            context.exception.code, http.client.BAD_REQUEST, f"Error in API request to {url}"
        )

        url = f"{BASE_URL}/calc/divide/a/2"
        with self.assertRaises(urllib.error.HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            context.exception.code, http.client.BAD_REQUEST, f"Error in API request to {url}"
        )

        url = f"{BASE_URL}/calc/divide/2/0"
        with self.assertRaises(urllib.error.HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            context.exception.code, http.client.BAD_REQUEST, f"Error in API request to {url}"
        )

# Unit tests for the sqrt endpoint

    def test_api_sqrt(self):
        url = f"{BASE_URL}/calc/sqrt/5"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error in API request to {url}"
        )

    def test_api_sqrt_wrong(self):
        url = f"{BASE_URL}/calc/sqrt/a"
        with self.assertRaises(urllib.error.HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            context.exception.code, http.client.BAD_REQUEST, f"Error in API request to {url}"
        )

        url = f"{BASE_URL}/calc/sqrt/-2"
        with self.assertRaises(urllib.error.HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            context.exception.code, http.client.BAD_REQUEST, f"Error in API request to {url}"
        )

        url = f"{BASE_URL}/calc/sqrt/0"
        with self.assertRaises(urllib.error.HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            context.exception.code, http.client.BAD_REQUEST, f"Error in API request to {url}"
        )


# Unit tests for the log endpoint

    def test_api_log(self):
        url = f"{BASE_URL}/calc/sqrt/100"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error in API request to {url}"
        )

    def test_api_log_wrong(self):
        url = f"{BASE_URL}/calc/log/a"
        with self.assertRaises(urllib.error.HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            context.exception.code, http.client.BAD_REQUEST, f"Error in API request to {url}"
        )

        url = f"{BASE_URL}/calc/log/-2"
        with self.assertRaises(urllib.error.HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            context.exception.code, http.client.BAD_REQUEST, f"Error in API request to {url}"
        )

        url = f"{BASE_URL}/calc/log/0"
        with self.assertRaises(urllib.error.HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            context.exception.code, http.client.BAD_REQUEST, f"Error in API request to {url}"
        )