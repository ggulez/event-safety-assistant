import anthropic
import os
from datetime import datetime

client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)

print("=" * 60)
print("EVENT SAFETY ASSISTANT - Powered by Claude")
print("=" * 60)
print()
continue_analyzing = True

while continue_analyzing:
    # Get event details from user
    print("Describe your event:")
    event_description = input("> ")

    print("\nAnalyzing with Claude...\n")

    # Ask Claude to analyze it
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        messages=[
            {"role": "user", "content": f"""Analyze this event for safety and operational needs:

    {event_description}

    Provide:
    1. Overall risk level (LOW/MEDIUM/HIGH)
    2. Main safety concerns
    3. Staffing recommendations
    4. Key operational recommendations

    Be specific and practical."""}
        ]
    )

    # Get the analysis
    analysis = message.content[0].text

    # Print it
    print(analysis)
    print("\n" + "=" * 60)

    # Ask if they want to save
    save = input("\nSave this analysis to file? (y/n): ")

    if save.lower() == 'y':
        # Create filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"analysis_{timestamp}.txt"
        
        # Write to file
        with open(filename, 'w') as f:
            f.write("EVENT SAFETY ANALYSIS\n")
            f.write("=" * 60 + "\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Event: {event_description}\n")
            f.write("=" * 60 + "\n\n")
            f.write(analysis)
        
        print(f"✅ Analysis saved to: {filename}")
    else:
        print("Analysis not saved.")

    # Ask if they want to analyze another event
    response = input("\nAnalyze another event? (y/n)")
    
    if response.lower() != 'y':
        continue_analyzing = False

print("\n" + "=" * 60)
print("Thank you for using Event Safety Assistant!")
print("=" * 60)
