import os

def generate_invitations(template, attendees, output_dir='.'):
    """
    Generate invitation files from a template and attendee data.
    
    Args:
        template (str): The template string containing placeholders in {{ key }} format
        attendees (list): List of dictionaries containing attendee data
        output_dir (str): Directory to save output files (default: current directory)
    """
    # Check input types
    if not isinstance(template, str):
        raise ValueError("Template must be a string")
        
    if not isinstance(attendees, list) or not all(isinstance(i, dict) for i in attendees):
        raise ValueError("Attendees must be a list of dictionaries")
    
    # Handle empty inputs
    if not template.strip():
        raise ValueError("Template is empty, no output files generated.")
        
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Ensure output directory exists
    try:
        os.makedirs(output_dir, exist_ok=True)
    except OSError as e:
        raise OSError(f"Failed to create output directory: {e}")

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        try:
            output = template
            for key in ["name", "event_title", "event_date", "event_location"]:
                value = str(attendee.get(key, "N/A") or "N/A")
                output = output.replace(f'{{{{ {key} }}}}', value)
            
            # Generate output filename
            output_file = os.path.join(output_dir, f'output_{index}.txt')
            
            # Check if file already exists
            if os.path.exists(output_file):
                print(f"Warning: {output_file} already exists, it will be overwritten")
            
            # Write to file with error handling
            try:
                with open(output_file, 'w', encoding='utf-8') as file:
                    file.write(output)
                print(f"Successfully created: {output_file}")
            except IOError as e:
                print(f"Error writing to {output_file}: {e}")
                
        except Exception as e:
            print(f"Error processing attendee {index}: {e}")

# Test function (you can run this to manually test the function)
if __name__ == "__main__":
    template_content = """
    Hello {{ name }},

    You are invited to the {{ event_title }} on {{ event_date }} at {{ event_location }}.

    We look forward to your presence.

    Best regards,
    Event Team
    """

    attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]

    generate_invitations(template_content, attendees)