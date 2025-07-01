from .components.hypothesizer import Hypothesizer
from .components.experiment_designer import ExperimentDesigner
from .components.data_analyzer import DataAnalyzer
from .components.manuscript_generator import ManuscriptGenerator

class ResearchAgent:
    """
    The main research agent.
    """
    def __init__(self):
        self.hypothesizer = Hypothesizer()
        self.experiment_designer = ExperimentDesigner()
        self.data_analyzer = DataAnalyzer()
        self.manuscript_generator = ManuscriptGenerator()

    def run(self):
        """
        Runs the research agent.
        """
        hypothesis = self.hypothesizer.generate()
        experiment = self.experiment_designer.design(hypothesis)
        data_path = "data/sample_data.csv"
        analysis = self.data_analyzer.analyze(data_path)
        self.manuscript_generator.generate(hypothesis, experiment, analysis)
