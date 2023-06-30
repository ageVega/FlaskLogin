# Pruebas relacionadas con la gestión de usuarios.
from unittest.mock import patch
from src.connection import get_user_by_id

def test_get_user_by_id():
    with patch("src.connection.get_user_by_id") as mock_get_user:
        mock_get_user.return_value = None
        user = get_user_by_id(0)
        assert user is None
