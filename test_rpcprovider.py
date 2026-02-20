# test_rpcprovider.py
"""
Tests for RpcProvider module.
"""

import unittest
from rpcprovider import RpcProvider

class TestRpcProvider(unittest.TestCase):
    """Test cases for RpcProvider class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RpcProvider()
        self.assertIsInstance(instance, RpcProvider)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RpcProvider()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
