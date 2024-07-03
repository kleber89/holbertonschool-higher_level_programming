import requests


def fetch_and_print_posts():
    """
    Fetches posts from JSONPlaceholder and prints the titles of the posts.
    """
    # Send a GET request to fetch posts
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    # Print the status code of the response
    print(f"Status Code: {response.status_code}")

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the fetched data into a JSON object
        posts = response.json()

        # Iterate through the parsed JSON data and print out the titles of all the posts
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """
    Fetches posts from JSONPlaceholder and saves them into a CSV file.
    """
    # Send a GET request to fetch posts
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the fetched data into a JSON object
        posts = response.json()

        # Structure the data into a list of dictionaries
        structured_data = []
        for post in posts:
            structured_data.append(
                {"id": post["id"], "title": post["title"], "body": post["body"]}
            )

        # Write the structured data into a CSV file
        import csv

        with open("posts.csv", mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(structured_data)
        print("Data has been written to posts.csv")


if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
