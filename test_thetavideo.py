# test_thetavideo.py
"""
Tests for ThetaVideo module.
"""

import unittest
from thetavideo import ThetaVideo

class TestThetaVideo(unittest.TestCase):
    """Test cases for ThetaVideo class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ThetaVideo()
        self.assertIsInstance(instance, ThetaVideo)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ThetaVideo()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
