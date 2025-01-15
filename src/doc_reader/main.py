import sys
import warnings
from crew import DocReader

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the DocReader crew.
    """
    inputs = {
        'tool': 'React latest document'
    }
    DocReader().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()




