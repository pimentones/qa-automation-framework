Doubts

section 1.7

<!-- Learninngs -->

1. use .venv to set the correct python version we want to use in the project
   1.1 remeber to activate with every terminal session or set it in vscode settings

2. environment variables priority
   2.1 Highest: Aeal environment variable: set in your shell, on the command line, or by CI
   2.2 .env file
   2.3 Lowest: Default written in from_env()

3. Use .env for local environment settings and real environment variables (sheel, command line or CI) for one-off overrides

4. USE A HOOK WHEN...
   A rule must apply to every test and forgetting it would be a silent bug. In step 1.7, if each file had to declare its own suite marker, sooner or later someone would forget and their tests would drop out of -m api runs. The hook makes forgetting impossible.

You need something only pytest knows, like whether the test failed. A fixture can't easily tell whether the test it served passed. In step 3.5, pytest_runtest_makereport sees the outcome, so it can take a screenshot exactly when a test fails.

You want to change which tests run, or in what order. For example, skip every UI test when no browser or Grid is reachable, or deselect tests marked destructive when ENV=prod. That's pytest_collection_modifyitems again.

You want new command-line options or extra output. pytest_addoption could add --env staging. pytest_report_header could print the API and UI base URLs at the top of every run. That header is useful when you're reading a CI log and need to know which environment it ran against.

You're connecting pytest to another system. For example, posting results to a test-management tool, Slack or a dashboard from pytest_runtest_logreport or pytest_sessionfinish.

4.1. do all the hooks run once, after pytest has found all the tests and before it runs any of them?

No. Each hook fires at its own point in the run, and they fire very different numbers of times: once per run, once per file, once per test, three times per test, or only when some event happens.

5. what is the function of **init**.py files?
   An **init**.py file tells Python that a folder is a package: a group of modules you can import with dots

6. what is the difference between a module and a package?
   A module is one .py file. A package is a folder of modules, marked with an **init**.py, and it can contain other packages.

7. what is the difference between a class and an object?
   A class is a blueprint: it says what data its objects hold and what they can do. An object (also called an instance) is one concrete thing built from that blueprint, with its own values.

Instance attributes vs class attributes is where this matters in an interview. In Wednesday's page objects:

class HomePage(BasePage):
SEARCH_BOX = dt("search-query") # class attribute: one copy, shared by every HomePage

    def __init__(self, driver):
        self.driver = driver            # instance attribute: each HomePage has its own

Two HomePage objects share the same SEARCH_BOX locator, which is fine because locators never change. Each one drives its own browser. self is how a method knows which object it was called on. The classic trap is a mutable class attribute, such as a list: it's shared by every instance, so one object changing it changes it for all of them.

8. clean up inputs at the boundary
   the idea is to clean up inputs where they occur and where the config reads the envinroment, in this case in the config file, so that any erros like typos don't impact the framework later on when running.

9.
