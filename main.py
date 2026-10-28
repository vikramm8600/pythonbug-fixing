"""Corrected examples of common beginner Python bugs."""


def is_palindrome(text: str) -> bool:
    """Return True when text reads the same forwards and backwards."""
    normalized = "".join(character.lower() for character in text if character.isalnum())
    return normalized == normalized[::-1]


def safe_average(numbers: list[float]) -> float:
    """Calculate an average and reject an empty list."""
    if not numbers:
        raise ValueError("Cannot calculate the average of an empty list.")
    return sum(numbers) / len(numbers)


def main() -> None:
    samples = ["madam", "Python", "Never odd or even"]
    for sample in samples:
        print(f"{sample!r} is palindrome: {is_palindrome(sample)}")

    try:
        print("Average:", safe_average([10, 20, 30]))
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
