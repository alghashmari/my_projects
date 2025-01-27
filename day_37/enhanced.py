import requests
from datetime import datetime
from typing import Optional


class PixelaTracker:
    BASE_URL = "https://pixe.la/v1/users"

    def __init__(self, username: str, token: str):
        self.username = username
        self.token = token
        self.headers = {"X-USER-TOKEN": token}

    def create_user(self) -> dict:
        """Create a new Pixela user."""
        params = {
            "token": self.token,
            "username": self.username,
            "agreeTermsOfService": "yes",
            "notMinor": "yes",
        }
        response = requests.post(url=self.BASE_URL, json=params)
        return response.json()

    def create_graph(self, graph_id: str, name: str, unit: str,
                     type: str = "float", color: str = "sora") -> dict:
        """Create a new tracking graph."""
        graph_endpoint = f"{self.BASE_URL}/{self.username}/graphs"
        graph_config = {
            "id": graph_id,
            "name": name,
            "unit": unit,
            "type": type,
            "color": color
        }
        response = requests.post(
            url=graph_endpoint,
            json=graph_config,
            headers=self.headers
        )
        return response.json()

    def post_value(self, graph_id: str, quantity: float,
                   date: Optional[datetime] = None) -> dict:
        """Post a new value to the graph."""
        if date is None:
            date = datetime.now()

        post_endpoint = f"{self.BASE_URL}/{self.username}/graphs/{graph_id}"
        post_config = {
            "date": date.strftime("%Y%m%d"),
            "quantity": str(quantity),
        }
        response = requests.post(
            url=post_endpoint,
            json=post_config,
            headers=self.headers
        )
        return response.json()

    def update_value(self, graph_id: str, date: datetime,
                     quantity: float) -> dict:
        """Update an existing value on the graph."""
        update_endpoint = (f"{self.BASE_URL}/{self.username}/graphs/"
                           f"{graph_id}/{date.strftime('%Y%m%d')}")
        update_config = {
            "quantity": str(quantity)
        }
        response = requests.put(
            url=update_endpoint,
            json=update_config,
            headers=self.headers
        )
        return response.json()


def main():
    # Example usage
    USERNAME = "alghashmari"
    TOKEN = "fldsakfkldsajfkdjfls"
    GRAPH_ID = "graph1"

    tracker = PixelaTracker(USERNAME, TOKEN)

    # Create a new user (only needed once)
    # tracker.create_user()

    # Create a new graph (only needed once)
    # tracker.create_graph(GRAPH_ID, "Daily Study Hours", "Hour")

    # Post today's study hours
    hours = float(input("How many hours did you study today? "))
    result = tracker.post_value(GRAPH_ID, hours)
    print(result)


if __name__ == "__main__":
    main()