import requests
from typing import List


class Github:
    def __init__(self) -> None:
        self.url = "https://api.github.com/"

    def pulls(self, repo: str, state: str = "all") -> List[dict]:
        """Fetches a list of pull requests with status state made on the provided repo.

        Parameters
        ----------
        repo :  str
                string of format {owner}/{repository}
                    owner       -- username of owner of the repository
                    repository  -- name of the repository
        state : {\'all\', \'open\', \'closed\'}
                status of the pull request (open / closed / all)

        Returns
        -------
        data :  List[dict]
            list of pull requests where each record is a dict containing:
                \'username\' : str
                    username of the author
                \'labels\'   : List[str]
                    list of labels on the pull request

        Raises
        ------
        ValueError
            If the value of state is not \'all\', \'open\' or \'closed\'.
        RuntimeError
            If response status code from the request isn't 200.

        """

        VALID_STATES = {"all", "open", "closed"}

        state = state.lower()  # Making state case-insensitive
        if state not in VALID_STATES:
            # Raise error when invalid state
            raise ValueError(f"state: state must be one of {VALID_STATES}")

        url = f"{self.url}repos/{repo}/pulls?state={state}"
        response = requests.get(url)

        if response.ok:
            data = response.json()

            # Filtering out label, datetime and author username from data
            for index in range(len(data)):
                record = dict()
                record["username"] = data[index]["user"]["login"]
                record["labels"] = [label["name"]
                                    for label in data[index]["labels"]]

                data[index] = record

            return data
        else:
            raise RuntimeError(
                f"Error {response.status_code}: {response.json()['message']}")

    def user(self, username: str) -> dict:
        url = f"{self.url}users/{username}"

        user_info = {}
        response = requests.get(url)

        if response.ok:
            data = response.json()

            # Filtering out only required information
            user_info["username"] = data["login"]
            user_info["name"] = data["name"]
            user_info["avatar_url"] = data["avatar_url"]
            user_info["url"] = data["html_url"]
            return user_info
        else:
            raise RuntimeError(
                f"Error {response.status_code}: {response.json()['message']}")

    def repo(self, repo: str) -> dict:
        url = f"{self.url}repos/{repo}"

        repo_info = {}
        response = requests.get(url)

        if response.ok:
            data = response.json()

            # Filtering out only required information
            repo_info["username"] = data["login"]
            return repo_info
        else:
            raise RuntimeError(
                f"Error {response.status_code}: {response.json()['message']}")


if __name__ == "__main__":
    pass
