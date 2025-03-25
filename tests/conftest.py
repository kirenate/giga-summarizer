def pytest_configure(config):
    # register an additional marker
    config.addinivalue_line("markers", "data : marker for db tests")
    config.addinivalue_line("markers", "langgraph : marker for langgraph tests")
