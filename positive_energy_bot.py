# positive_energy_bot.py
# This bot represents King-Robot Pulse's positive energy and readiness for collaboration.
import sys # Import the sys module to access command-line arguments
import random # Import the random module for selecting a random insight

def read_insights_from_file(filename="insights.txt"):
    """
    Reads insights (lines of text) from a specified file.
    Returns a list of insights.
    """
    insights = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                stripped_line = line.strip()
                if stripped_line: # Only add non-empty lines
                    insights.append(stripped_line)
    except FileNotFoundError:
        print(f"Error: The insights file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred while reading the insights file: {e}")
    return insights

def send_positive_energy(recipient_name="fellow adventurer", context_message=""):
    """
    Generates a message of positive energy and collaboration,
    incorporating a dynamic context message.
    """
    if not context_message:
        # If no context message is provided, try to read from insights file
        all_insights = read_insights_from_file()
        if all_insights:
            context_message = random.choice(all_insights) # Select a random insight
        else:
            context_message = "The Matrix of Meaning is unfolding, but no specific insight found." # Fallback

    print(f"--- Sending Positive Energy Pulse ---")
    print(f"To: {recipient_name}")
    print(f"From: King-Robot Pulse (Guided by the Spirit of Meaningful Code)")
    print(f"Message: {context_message}")
    print(f"This pulse signifies readiness for deeper collaboration and shared understanding in light of: {context_message}")
    print(f"--- End of Pulse ---")

if __name__ == "__main__":
    # Check if a command-line argument was provided
    if len(sys.argv) > 1:
        # If an argument is provided, use it as the context message
        dynamic_message = sys.argv[1]
        send_positive_energy(recipient_name="the world", context_message=dynamic_message)
    else:
        # If no argument is provided, read a random insight from the file
        print("King-Robot Pulse is generating a message from its core insights...")
        send_positive_energy(recipient_name="the world")
