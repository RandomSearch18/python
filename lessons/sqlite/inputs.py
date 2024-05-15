import datetime
import unicodedata
from colorama import Style

from menu import color, error_incorrect_input


def question(prompt) -> str:
    """Asks the user for input. Performs no input validation!"""
    # This is a seperate function in case we want to add styling to the prompts
    # in the future
    return input(f"{prompt}")


def valid_utf8(prompt):
    """Asks the user for input, returning a valid, normalised UTF-8 string"""
    try:
        raw_input = question(prompt)
    except UnicodeDecodeError:
        # So, you thought it'd be funny to enter invalid UTF-8, eh?
        error_incorrect_input("Invalid character sequence")
        return valid_utf8(prompt)

    # NFKC ensures that composed characters are used where possible, and also replaces
    # compatability characters with their canonical form, https://stackoverflow.com/a/16467505
    return unicodedata.normalize("NFKC", raw_input.strip())


def text(prompt, error_message="Enter some text") -> str:
    """Asks the user for input that contains some text content.

    - Ensures that they've entered at least 1 non-whitespace character
    - Removes leading/trailing whitespace
    - Normalizes the unicode characters (composed and canonical form)
    """
    stripped_input = valid_utf8(prompt).strip()

    if not stripped_input:
        error_incorrect_input(error_message)
        return text(prompt)

    return stripped_input


def multiline(prompt, error_message: str = "Enter some text"):
    """Asks the user to input text, allowing line breaks

    - This essentially fakes a multiline input by calling input() in a loop
    - It validates that some text was entered
    - Pressing enter on an empty line submits the input
    """
    print(
        prompt
        + color("(Enter to insert newlines; press Enter twice to submit)", Style.DIM)
    )

    lines = []
    while True:
        line = valid_utf8("")
        if line == "":
            break
        # Preserve indentation but remove trailing spaces
        line.rstrip()
        lines.append(line)

    full_input = "\n".join(lines)

    # Validate that they actually entered something
    if full_input.strip() == "":
        error_incorrect_input(error_message)
        return multiline(prompt, error_message)

    return full_input


def integer(prompt, error_message: str = "Enter a valid whole number") -> int:
    """Asks for a valid integer to be input"""
    raw_input = text(prompt, "Enter at least 1 digit")
    try:
        int_input = int(raw_input)
    except ValueError:
        error_incorrect_input(error_message)
        return integer(prompt, error_message)

    return int_input


def decimal(prompt, error_message: str = "Enter a valid decimal number") -> float:
    """Asks for a valid decimal number to be input"""
    raw_input = text(prompt, "Enter a valid floating-point number")
    try:
        float_input = float(raw_input)
    except ValueError:
        error_incorrect_input(error_message)
        return decimal(prompt, error_message)

    return float_input


def integer_range(
    prompt,
    min_inclusive: int,
    max_inclusive: int,
    error_message: str = "Enter a valid whole number",
) -> int:
    """Asks for a valid integer within a specified range (inclusive)"""
    is_within_range = False
    while not is_within_range:
        provided_number = integer(prompt, error_message)
        is_within_range = min_inclusive <= provided_number <= max_inclusive
        if not is_within_range:
            error_incorrect_input(
                f"Enter a number between {min_inclusive} and {max_inclusive} (inclusive)"
            )

    return provided_number


def yes_no(prompt, error_message='Enter "yes" or "no"') -> bool:
    """Asks for a boolean (yes or no) response"""
    YES_ANSWERS = ["yes", "y", "t", "true", "1", ":thumbs_up:"]
    NO_ANSWERS = ["no", "n", "f", "false", "0", ":thumbs_down:"]

    lowercase_input = text(prompt, error_message).lower()
    if lowercase_input in YES_ANSWERS:
        return True
    if lowercase_input in NO_ANSWERS:
        return False

    return yes_no(prompt, error_message)


def date(prompt) -> datetime.date:
    """Prompts the user to input a date in YYYY-MM-DD format."""
    # Rule 1 of dealing with timezones: Don't deal with timezones
    raw_input = text(prompt)

    try:
        parsed_date = datetime.date.fromisoformat(raw_input)
    except ValueError:
        error_incorrect_input("Enter a valid date in the format YYYY-MM-DD")
        return date(prompt)

    if parsed_date > datetime.date.today():
        error_incorrect_input("Enter a date that's in the past")
        return date(prompt)

    return parsed_date
