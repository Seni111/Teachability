from hello import greet, add


class TestGreet:
    def test_greet_world(self):
        assert greet("World") == "Hello, World!"

    def test_greet_with_name(self):
        assert greet("Alice") == "Hello, Alice!"

    def test_greet_empty_string(self):
        assert greet("") == "Hello, !"

    def test_greet_special_characters(self):
        assert greet("John@123") == "Hello, John@123!"


class TestAdd:
    def test_add_positive_numbers(self):
        assert add(5, 3) == 8

    def test_add_negative_numbers(self):
        assert add(-5, -3) == -8

    def test_add_mixed_signs(self):
        assert add(5, -3) == 2

    def test_add_zeros(self):
        assert add(0, 0) == 0

    def test_add_with_zero(self):
        assert add(5, 0) == 5
