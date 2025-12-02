"""
Tweet Thread Generator Module - Lite Version

Generates engaging Twitter/X threads using template-based logic.
No external API required - uses built-in templates and rules.

Note: This is the Lite version. Full Commercial includes
more templates and customization options.
"""

import random
from typing import Optional


# Thread components (subset of Full version)
HOOK_TWEETS = [
    "🧵 I spent 5 years studying {topic}, and here's what nobody tells you:\n\n(A thread that might change your perspective)",
    "Most people get {topic} completely wrong.\n\nHere are the insights that transformed my understanding:\n\n🧵👇",
    "Want to master {topic}?\n\nI'm about to share the framework that changed everything for me.\n\nBookmark this thread. 🔖",
]

POINT_TEMPLATES = [
    {
        "intro": "1/ The foundation:",
        "content": "Understanding {topic} starts with the basics. Most people skip this step and struggle later.\n\n✅ Master the fundamentals first\n✅ Don't rush to advanced concepts\n✅ Build on solid ground"
    },
    {
        "intro": "The biggest mistake I see:",
        "content": "People approach {topic} without a clear goal.\n\nBefore you start, ask yourself:\n• What do I want to achieve?\n• How will I measure success?\n• What's my timeline?"
    },
    {
        "intro": "Here's the game-changer:",
        "content": "Consistency beats intensity with {topic}.\n\n📊 Daily small actions > Monthly big pushes\n📈 Progress compounds over time\n🎯 Show up even when you don't feel like it"
    },
    {
        "intro": "The secret most experts won't share:",
        "content": "Success with {topic} comes from:\n\n1. Learning from failures\n2. Adapting quickly\n3. Staying curious\n\nIt's not about being perfect. It's about improving."
    },
]

CTA_TWEETS = [
    "That's the thread!\n\n♻️ Retweet the first tweet to help others discover this\n\n👤 Follow for more on {topic}",
    "If you made it here, you're serious about {topic}.\n\n💾 Save this thread for later\n🔔 Follow for more insights!",
]


def generate(topic: str, config: Optional[dict] = None) -> str:
    """
    Generate a Twitter/X thread about the given topic.
    
    Args:
        topic: The main topic for the thread
        config: Optional configuration (not used in Lite version)
    
    Returns:
        A formatted tweet thread as a string
    """
    parts = []
    
    # Header
    parts.append(f"🐦 TWITTER/X THREAD: {topic.upper()}\n")
    parts.append("=" * 50 + "\n\n")
    
    # Hook tweet
    parts.append("TWEET 1/\n")
    parts.append("-" * 30 + "\n")
    hook = random.choice(HOOK_TWEETS).format(topic=topic.title())
    parts.append(f"{hook}\n")
    parts.append(f"[{len(hook)} characters]\n\n")
    
    # Middle tweets (3 in Lite version)
    selected_points = random.sample(POINT_TEMPLATES, 3)
    for i, point in enumerate(selected_points, 2):
        parts.append(f"TWEET {i}/\n")
        parts.append("-" * 30 + "\n")
        
        content = f"{point['intro']}\n\n{point['content'].format(topic=topic)}"
        parts.append(f"{content}\n")
        parts.append(f"[{len(content)} characters]\n\n")
    
    # CTA tweet
    parts.append("TWEET 5/\n")
    parts.append("-" * 30 + "\n")
    cta = random.choice(CTA_TWEETS).format(topic=topic)
    parts.append(f"{cta}\n")
    parts.append(f"[{len(cta)} characters]\n\n")
    
    # Summary
    parts.append("=" * 50 + "\n")
    parts.append("📊 THREAD STATS:\n")
    parts.append("- Total tweets: 5\n")
    parts.append(f"- Topic: {topic}\n")
    
    # Lite version notice
    parts.append("\n---\n")
    parts.append("Generated with AI Content Engine Lite.\n")
    parts.append("Upgrade to Full Commercial for more modes and longer threads!\n")
    
    return "".join(parts)


if __name__ == "__main__":
    sample_topic = "productivity"
    print(generate(sample_topic))
