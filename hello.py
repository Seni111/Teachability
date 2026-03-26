def greet(name: str) -> str:
    """Return a personalized greeting message."""
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    """Return the sum of two numbers."""
    return a + b


if __name__ == "__main__":
    print(greet("World"))
    print(f"5 + 3 = {add(5, 3)}")