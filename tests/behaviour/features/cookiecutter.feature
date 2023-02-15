Feature: cookiecutter
  A working template should be created by cookiecutter

  Scenario: the template creates a Python project
    Given an empty directory
    When I run cookiecutter
    Then placeholder variables should be correct
    And the tests produced by the template should work
    And pre-commit can be run without error
