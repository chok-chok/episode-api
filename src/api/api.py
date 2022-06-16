"""Class with CRUD logic for API, it takes DB-access module as dependency"""

def read_episode():
    # Take the id of episode
    # Check if the episode exists
    # Return None if it doesn't, otherwise return Episode
    return "dummy_data"


def read_episodes():
    """Read list of episode from database"""
    # Retrieve list of episodes with default pagination
    # If there is argument coming in for pagination use take to chop the list
    # (Optionally) consider to apply default sorting
    return "dummy_data"


def create_episode():
    # Take payload to create a new episode
    # (Consider to validate the payload)
    # Raise exception when the payload is invalid 
    # Pass the payload to db-access 
    # Return the URL to new data
    return "dummy_data"


def delete_episode():
    # Take id to delete the episode
    # Check if episode exists
    # Return None if it doesn't
    # Pass the ID to DB-access
    # Return success message to caller
    return "dummy_data"
