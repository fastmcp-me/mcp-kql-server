"""
Unit tests for the utils module.
"""

import unittest
import tempfile
import os
from pathlib import Path
from unittest.mock import patch, MagicMock

from mcp_kql_server.utils import (
    normalize_cluster_uri,
    extract_cluster_and_database_from_query,
    clean_query_for_execution,
    validate_kql_query_syntax,
    format_error_message,
    safe_get_env_var,
    ensure_directory_exists,
    truncate_string,
    is_debug_mode,
    mask_sensitive_data,
    get_file_age_days
)


class TestUtils(unittest.TestCase):
    """Test cases for utility functions."""

    def test_normalize_cluster_uri(self):
        """Test cluster URI normalization."""
        # Test full HTTPS URI
        self.assertEqual(
            normalize_cluster_uri("https://mycluster.kusto.windows.net"),
            "https://mycluster.kusto.windows.net"
        )
        
        # Test FQDN
        self.assertEqual(
            normalize_cluster_uri("mycluster.kusto.windows.net"),
            "https://mycluster.kusto.windows.net"
        )
        
        # Test simple cluster name
        self.assertEqual(
            normalize_cluster_uri("mycluster"),
            "https://mycluster.kusto.windows.net"
        )
        
        # Test invalid inputs
        with self.assertRaises(ValueError):
            normalize_cluster_uri("")
        
        with self.assertRaises(ValueError):
            normalize_cluster_uri("   ")
        
        with self.assertRaises(ValueError):
            normalize_cluster_uri("invalid!cluster@name")

    def test_extract_cluster_and_database_from_query(self):
        """Test extraction of cluster and database from KQL queries."""
        # Valid query
        query = "cluster('mycluster').database('mydb').MyTable | take 10"
        cluster_uri, database = extract_cluster_and_database_from_query(query)
        self.assertEqual(cluster_uri, "https://mycluster.kusto.windows.net")
        self.assertEqual(database, "mydb")
        
        # Query with FQDN cluster
        query = "cluster('mycluster.kusto.windows.net').database('mydb').MyTable | take 10"
        cluster_uri, database = extract_cluster_and_database_from_query(query)
        self.assertEqual(cluster_uri, "https://mycluster.kusto.windows.net")
        self.assertEqual(database, "mydb")
        
        # Query missing cluster
        query = "database('mydb').MyTable | take 10"
        cluster_uri, database = extract_cluster_and_database_from_query(query)
        self.assertIsNone(cluster_uri)
        self.assertIsNone(database)
        
        # Query missing database
        query = "cluster('mycluster').MyTable | take 10"
        cluster_uri, database = extract_cluster_and_database_from_query(query)
        self.assertEqual(cluster_uri, "https://mycluster.kusto.windows.net")
        self.assertIsNone(database)

    def test_clean_query_for_execution(self):
        """Test query cleaning functionality."""
        original_query = "cluster('mycluster').database('mydb').MyTable | take 10"
        cleaned = clean_query_for_execution(original_query)
        self.assertEqual(cleaned, "MyTable | take 10")
        
        # Test query without cluster/database prefix
        simple_query = "MyTable | take 10"
        cleaned = clean_query_for_execution(simple_query)
        self.assertEqual(cleaned, "MyTable | take 10")

    def test_validate_kql_query_syntax(self):
        """Test KQL query syntax validation."""
        # Valid query
        valid_query = "cluster('mycluster').database('mydb').MyTable | take 10"
        is_valid, error = validate_kql_query_syntax(valid_query)
        self.assertTrue(is_valid)
        self.assertIsNone(error)
        
        # Empty query
        is_valid, error = validate_kql_query_syntax("")
        self.assertFalse(is_valid)
        self.assertIsNotNone(error)
        
        # Query missing cluster
        invalid_query = "database('mydb').MyTable | take 10"
        is_valid, error = validate_kql_query_syntax(invalid_query)
        self.assertFalse(is_valid)
        self.assertIsNotNone(error)
        
        # Query missing database
        invalid_query = "cluster('mycluster').MyTable | take 10"
        is_valid, error = validate_kql_query_syntax(invalid_query)
        self.assertFalse(is_valid)
        self.assertIsNotNone(error)

    def test_format_error_message(self):
        """Test error message formatting."""
        error = ValueError("Test error message")
        formatted = format_error_message(error, "Test context")
        self.assertIn("Test context", formatted)
        self.assertIn("ValueError", formatted)
        self.assertIn("Test error message", formatted)
        
        # Test without context
        formatted = format_error_message(error)
        self.assertIn("ValueError", formatted)
        self.assertIn("Test error message", formatted)

    def test_safe_get_env_var(self):
        """Test safe environment variable retrieval."""
        # Test with existing variable
        with patch.dict(os.environ, {'TEST_VAR': 'test_value'}):
            value = safe_get_env_var('TEST_VAR', 'default')
            self.assertEqual(value, 'test_value')
        
        # Test with non-existing variable
        value = safe_get_env_var('NON_EXISTING_VAR', 'default')
        self.assertEqual(value, 'default')
        
        # Test with empty default
        value = safe_get_env_var('NON_EXISTING_VAR')
        self.assertEqual(value, '')

    def test_ensure_directory_exists(self):
        """Test directory creation."""
        with tempfile.TemporaryDirectory() as temp_dir:
            test_path = Path(temp_dir) / "test_subdir" / "nested"
            
            # Directory should not exist initially
            self.assertFalse(test_path.exists())
            
            # Create directory
            result = ensure_directory_exists(test_path)
            self.assertTrue(result)
            self.assertTrue(test_path.exists())
            self.assertTrue(test_path.is_dir())

    def test_truncate_string(self):
        """Test string truncation."""
        # Test normal truncation
        text = "This is a very long string that should be truncated"
        truncated = truncate_string(text, 20)
        self.assertEqual(len(truncated), 20)
        self.assertTrue(truncated.endswith("..."))
        
        # Test string shorter than max length
        short_text = "Short"
        truncated = truncate_string(short_text, 20)
        self.assertEqual(truncated, "Short")
        
        # Test custom suffix
        truncated = truncate_string(text, 20, " [more]")
        self.assertTrue(truncated.endswith(" [more]"))

    def test_is_debug_mode(self):
        """Test debug mode detection."""
        # Test with debug enabled
        with patch.dict(os.environ, {'KQL_DEBUG': '1'}):
            self.assertTrue(is_debug_mode())
        
        with patch.dict(os.environ, {'DEBUG': 'true'}):
            self.assertTrue(is_debug_mode())
        
        # Test with debug disabled
        with patch.dict(os.environ, {}, clear=True):
            self.assertFalse(is_debug_mode())

    def test_mask_sensitive_data(self):
        """Test sensitive data masking."""
        # Test normal masking
        sensitive = "password123456"
        masked = mask_sensitive_data(sensitive, visible_chars=3)
        self.assertEqual(masked, "pas******456")
        
        # Test short string
        short = "abc"
        masked = mask_sensitive_data(short, visible_chars=2)
        self.assertEqual(len(masked), 3)
        self.assertTrue("*" in masked)

    def test_get_file_age_days(self):
        """Test file age calculation."""
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_path = Path(temp_file.name)
            
            try:
                # File should have very recent age (close to 0)
                age = get_file_age_days(temp_path)
                self.assertIsNotNone(age)
                if age is not None:
                    self.assertGreaterEqual(age, 0.0)
                    self.assertLess(age, 1.0)  # Should be less than 1 day old
                
            finally:
                temp_path.unlink()
        
        # Test non-existent file
        non_existent = Path("non_existent_file.txt")
        age = get_file_age_days(non_existent)
        self.assertIsNone(age)


if __name__ == '__main__':
    unittest.main()