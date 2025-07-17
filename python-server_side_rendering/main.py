#!/usr/bin/env python3
"""
Main script to generate invitations from a template and attendee data.
"""
import os
from task_00_intro import generate_invitations

def main():
    try:
        # Check if template file exists
        template_path = 'template.txt'
        if not os.path.exists(template_path):
            print(f"Error: Template file '{template_path}' not found.")
            return

        # Read the template from a file
        with open(template_path, 'r', encoding='utf-8') as file:
            template_content = file.read()

        # List of attendees
        attendees = [
            {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
            {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
            {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
        ]

        # Call the function with the template and attendees list
        generate_invitations(template_content, attendees)
        print("Invitations generated successfully in the 'output' directory.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()