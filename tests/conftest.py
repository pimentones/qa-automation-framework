import pytest

SUITES = ["unit", "api", "e2e"]

# adds a marker per folder, so a suite can be combined with other markers in one -m expression: pytest -m "smoke and not e2e" runs the quick checks from every folder except the browser tests
@pytest.hookimpl(tryfirst=True)
def pytest_collection_modifyitems(items):
    #tests/api/* gets @pytest.mark.api, tests/e2e/* gets e2e, tests/unit/* gets unit
    for item  in items:
        suite = item.path.parent.name
        if suite in SUITES:
            item.add_marker(getattr(pytest.mark, suite))