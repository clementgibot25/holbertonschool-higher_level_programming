#!/usr/bin/env python3

def generate_invitations(template, attendees):
    # check input
    if not isinstance(template, str):
        print("Template must be a string")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Attendees must be a list of dictionaries")
        return
    
    # Handle empty inputs
    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # process each attendee
    for index, attendee in enumerate(attendees, start=1):
        output = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key, "N/A")
            if value is None:
                value = "N/A"
            output = output.replace(f'{{{{ {key} }}}}', value)

        # Generate output file
        with open(f'output_{index}.txt', 'w') as file:
            file.write(output)
