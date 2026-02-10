from pathlib import Path

from ..runner import BinaryRunner


def test_download_exercise(runner: BinaryRunner, exercises_dir: Path) -> None:
    """Test the download command output successfully performs the download for exercise."""
    res = runner.run(["download", "under-control"], cwd=exercises_dir)
    res.assert_success()

    exercise_folder = exercises_dir / "under-control"
    assert exercise_folder.is_dir()

    exercise_config = exercise_folder / ".gitmastery-exercise.json"
    assert exercise_config.is_file()

    exercise_readme = exercise_folder / "README.md"
    assert exercise_readme.is_file()


def test_download_hands_on(runner: BinaryRunner, exercises_dir: Path) -> None:
    """Test the download command output successfully performs the download for hands-on."""
    res = runner.run(["download", "hp-first-commit"], cwd=exercises_dir)
    res.assert_success()

    hands_on_folder = exercises_dir / "hp-first-commit"
    assert hands_on_folder.is_dir()
