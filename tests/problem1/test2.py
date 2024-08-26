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

    full_name = user.get_full_name()

    assert full_name == "John Doe"
