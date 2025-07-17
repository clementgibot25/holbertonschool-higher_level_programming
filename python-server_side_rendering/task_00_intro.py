#!/usr/bin/env python3
import os

def generate_invitations(template, attendees):
    """
    Generate invitation files from a template and attendee data.
    
    Args:
        template (str): The template string with {placeholders}
        attendees (list): List of dictionaries containing attendee data
    """
    # Check input types
    if not isinstance(template, str):
        raise TypeError("Error: Template must be a string")
        
    if not isinstance(attendees, list):
        raise TypeError("Error: Attendees must be a list")
        
    if not all(isinstance(a, dict) for a in attendees):
        raise TypeError("Error: All attendees must be dictionaries")
    
    # Handle empty inputs
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Create output directory if it doesn't exist
    os.makedirs('output', exist_ok=True)
    
    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        output = template
        
        # Replace placeholders with attendee data
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key, "N/A")
            if value is None:
                value = "N/A"
            # Using {key} format as per requirements
            output = output.replace(f'{{{key}}}', value)

        # Generate output file
        output_path = os.path.join('output', f'output_{index}.txt')
        try:
            # Check if file already exists
            if os.path.exists(output_path):
                print(f"Warning: {output_path} already exists, overwriting...")
                
            with open(output_path, 'w', encoding='utf-8') as file:
                file.write(output)
                
        except IOError as e:
            print(f"Error writing to file {output_path}: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
