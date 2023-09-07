import contextlib
import subprocess
from pathlib import Path

from cookiecutter.main import cookiecutter
from pytest_bdd import given
from pytest_bdd import scenario
from pytest_bdd import then
from pytest_bdd import when

_PROJECT_NAME = "sample-test-project"
_EXPECTED_PACKAGE_NAME = "sample_test_project"
_DESC = "A project generated by the test"


@scenario("cookiecutter.feature", "the template creates a Python project")
def test_cookiecuttter() -> None:
    pass


@given("an empty directory")
def empty_dir(tmp_path: Path) -> None:  # pylint: disable=unused-argument
    pass


@when("I run cookiecutter")
def run_cookiecutter(tmp_path: Path) -> None:
    template = str(Path(".").absolute())
    with contextlib.chdir(tmp_path):
        cookiecutter(
            template=template,
            extra_context={
                "project_name": _PROJECT_NAME,
                "description": _DESC,
            },
            no_input=True,
        )


@then("placeholder variables should be correct")
def assert_placeholders_are_correct(tmp_path: Path) -> None:
    repo_path = tmp_path.joinpath(_PROJECT_NAME)
    repo_exists = repo_path.is_dir()
    assert repo_exists
    package_path = repo_path / "src" / _EXPECTED_PACKAGE_NAME
    package_exists = package_path.is_dir()
    assert package_exists
    readme_text = repo_path.joinpath("README.md").read_text()
    assert _DESC in readme_text


@then("the tests produced by the template should work")
def assert_tests_work(tmp_path: Path) -> None:
    repo_path = tmp_path.joinpath(_PROJECT_NAME)
    _git_init(repo_path)
    subprocess.run("make test", cwd=repo_path, shell=True, check=True)


@then("pre-commit can be run without error")
def assert_pre_commit_alters_no_files(tmp_path: Path) -> None:
    repo_path = tmp_path.joinpath(_PROJECT_NAME)
    subprocess.run("make setup-dev", cwd=repo_path, shell=True, check=True)
    _pre_commit("run --all-files", repo_path, check=True)


def _git_init(repo: Path) -> None:
    subprocess.run("git init", cwd=repo, check=True, shell=True)


def _pre_commit(args: str, repo: Path, *, check: bool) -> None:
    subprocess.run(
        f"""\
make setup-dev \\
&& . .venv-dev/bin/activate \\
&& git add . \\
&& pre-commit {args}""",
        cwd=repo,
        check=check,
        shell=True,
    )
