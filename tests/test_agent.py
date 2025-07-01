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
        # We need to mock the hypothesizer to avoid errors since it now expects a topic
        # For a simple test, we can just ensure the run method executes without errors.
        # In a more robust test, we would mock the components to control their behavior.
        agent.run()

if __name__ == "__main__":
    unittest.main()