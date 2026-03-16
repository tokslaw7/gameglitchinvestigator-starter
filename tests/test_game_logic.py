from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from logic_utils import check_guess


def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"


def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"


def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


def test_hint_direction_matches_outcome_regression():
    high_outcome, high_message = check_guess(75, 50)
    low_outcome, low_message = check_guess(25, 50)

    assert high_outcome == "Too High"
    assert high_message == "📉 Go LOWER!"
    assert low_outcome == "Too Low"
    assert low_message == "📈 Go HIGHER!"
