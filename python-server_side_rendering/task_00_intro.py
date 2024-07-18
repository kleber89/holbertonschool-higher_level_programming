import os


def generate_invitations(template, attendees):
    # Check if the template is a string
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    # Check if the attendees is a list of dictionaries
    if not isinstance(attendees, list) or not all(
        isinstance(attendee, dict) for attendee in attendees
    ):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Check if the template is empty
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # Check if the attendees list is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for i, attendee in enumerate(attendees, start=1):
        # Replace placeholders with actual values or 'N/A' if missing
        personalized_template = template.format(
            name=attendee.get("name", "N/A"),
            event_title=attendee.get("event_title", "N/A"),
            event_date=attendee.get("event_date", "N/A"),
            event_location=attendee.get("event_location", "N/A"),
        )

        # Generate the output filename
        output_filename = f"output_{i}.txt"

        # Write the personalized template to the output file
        try:
            with open(output_filename, "w") as output_file:
                output_file.write(personalized_template)
        except Exception as e:
            print(f"Error writing to file {output_filename}: {e}")
            return

    print(f"{len(attendees)} invitation(s) generated successfully.")


# Main file content for testing
if __name__ == "__main__":
    # Read the template from a file
    try:
        with open("template.txt", "r") as file:
            template_content = file.read()
    except FileNotFoundError:
        print("Error: template.txt file not found.")
        template_content = ""

    # List of attendees
    attendees = [
        {
            "name": "Alice",
            "event_title": "Python Conference",
            "event_date": "2023-07-15",
            "event_location": "New York",
        },
        {
            "name": "Bob",
            "event_title": "Data Science Workshop",
            "event_date": "2023-08-20",
            "event_location": "San Francisco",
        },
        {
            "name": "Charlie",
            "event_title": "AI Summit",
            "event_date": None,
            "event_location": "Boston",
        },
    ]

    # Call the function with the template and attendees list
    generate_invitations(template_content, attendees)
