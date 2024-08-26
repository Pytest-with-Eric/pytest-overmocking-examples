from unittest.mock import Mock


class User:
    def get_first_name(self):
        # Imagine this fetches the first name from a database
        return "John"

    def get_last_name(self):
        # Imagine this fetches the last name from a database
        return "Doe"

    def get_full_name(self):
        first_name = self.get_first_name()
        last_name = self.get_last_name()
        return f"{first_name} {last_name}"


def test_get_full_name():
    user = User()

    # Mocking the internal methods of User
    user.get_first_name = Mock(return_value="Jane")
    user.get_last_name = Mock(return_value="Smith")

    full_name = user.get_full_name()

    # Asserting that the internal methods were called
    user.get_first_name.assert_called_once()
    user.get_last_name.assert_called_once()

    # Asserting the output
    assert full_name == "Jane Smith"
