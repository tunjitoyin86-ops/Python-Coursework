class User:
    """
    Represents a generic user with a name and email.
    """
    def __init__(self, name: str, email: str):
        """
        Initialize a User with a name and email.

        Args:
            name (str): The name of the user.
            email (str): The email address of the user.
        """
        self.name = name
        self.email = email

    def __str__(self) -> str:
        """
        String representation of the User.

        Returns:
            str: User details.
        """
        return f"User(name={self.name}, email={self.email})"

class Owner(User):
    """
    Represents an owner, which is a specialized type of User.
    """
    def __str__(self) -> str:
        """
        String representation of the Owner.

        Returns:
            str: Owner details.
        """
        return f"Owner(name={self.name}, email={self.email})"