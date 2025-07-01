import unittest
from src.agent import ResearchAgent

class TestAgent(unittest.TestCase):
    """
    Tests for the ResearchAgent class.
    """
    def test_run(self):
        """
        Tests the run method of the ResearchAgent class.
        """
        agent = ResearchAgent()
        agent.run()

if __name__ == "__main__":
    unittest.main()