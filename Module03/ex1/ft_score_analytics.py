#!/usr/bin/env python3
import sys


def no_scores() -> None:
    print(
        "No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ..."
    )


def my_score_analytics() -> None:
    total_args: int = len(sys.argv)
    if total_args == 1:
        return no_scores()

    valid_scores: list[int] = []

    for arg in sys.argv[1:]:
        try:
            score: int = int(arg)
            valid_scores.append(score)
        except Exception as e:
            print(f"Invalid parameter: '{arg}'")

    total_players: int = len(valid_scores)
    if total_players == 0:
        return no_scores()

    total_score: int = sum(valid_scores)
    average_score: float = total_score / total_players
    high_score: int = max(valid_scores)
    low_score: int = min(valid_scores)
    score_range: int = high_score - low_score

    print(f"Scores processed: {valid_scores}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {score_range}")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    my_score_analytics()
