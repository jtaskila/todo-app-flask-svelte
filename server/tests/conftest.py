import pytest

import sys
sys.path.append('..')

from app import create_app

@pytest.fixture(scope='session')
def tester():
    flask_app = create_app()

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as tester:
        # Establish an application context
        with flask_app.app_context():
            yield tester  # this is where the testing happens!
