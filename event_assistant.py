import anthropic
import os

client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)

print("=" * 60)
print("EVENT SAFETY ASSISTANT - Powered by Claude")
print("=" * 60)
print()

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

# Print the analysis
print(message.content[0].text)
print("\n" + "=" * 60)