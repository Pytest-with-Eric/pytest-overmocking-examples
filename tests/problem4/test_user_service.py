from unittest.mock import Mock


class UserService:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def get_user_by_id(self, user_id):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        return cursor.fetchone()


def test_get_user_by_id():
    mock_db_connection = Mock()
    mock_cursor = mock_db_connection.cursor.return_value
    mock_cursor.fetchone.return_value = {"id": 1, "name": "John Doe"}

    service = UserService(mock_db_connection)
    user = service.get_user_by_id(1)

    assert user == {"id": 1, "name": "John Doe"}
    mock_db_connection.cursor.assert_called_once()
    mock_cursor.execute.assert_called_once_with(
        "SELECT * FROM users WHERE id = ?", (1,)
    )
