#!/usr/bin/env python3
"""
AI Content Engine Lite - Basic Content Generator

A simplified version with blog and tweet thread modes only.
Uses template-based generation - no API required.

Usage:
    python ai_content_engine_lite.py --mode <mode> --topic "<topic>"
    python ai_content_engine_lite.py --interactive

Modes: blog, tweet_thread
"""

import argparse
import sys

# Import mode modules
from modes import blog, tweet_thread

# Available modes (limited in Lite version)
MODES = {
    "blog": blog,
    "tweet_thread": tweet_thread,
}


def generate_content(mode: str, topic: str) -> str:
    """Generate content using the specified mode."""
    if mode not in MODES:
        raise ValueError(f"Unknown mode: {mode}. Available modes: {list(MODES.keys())}")
    
    module = MODES[mode]
    return module.generate(topic)


def interactive_mode():
    """Run the engine in interactive mode."""
    print("\n" + "=" * 60)
    print("    AI Content Engine Lite")
    print("=" * 60)
    print("\nAvailable modes:")
    for i, mode in enumerate(MODES.keys(), 1):
        print(f"  {i}. {mode.replace('_', ' ').title()}")
    
    print("\nNote: This is the Lite version. Upgrade to Full Commercial")
    print("for YouTube scripts, social captions, SEO snippets, and more!")
    print("\nEnter 'quit' or 'q' to exit.\n")
    
    while True:
        print("-" * 40)
        mode_input = input("Select mode (1 for Blog, 2 for Tweet Thread): ").strip().lower()
        
        if mode_input in ('quit', 'q'):
            print("\nThank you for using AI Content Engine Lite!")
            print("Upgrade to Full Commercial for all 5 modes!")
            break
        
        # Handle numeric input
        if mode_input == '1':
            mode = 'blog'
        elif mode_input == '2':
            mode = 'tweet_thread'
        elif mode_input in MODES:
            mode = mode_input
        else:
            print("Invalid selection. Please enter 1 or 2.")
            continue
        
        # Get topic
        topic = input(f"\nEnter topic for {mode.replace('_', ' ')}: ").strip()
        if not topic:
            print("Topic cannot be empty. Please try again.")
            continue
        
        # Generate content
        print("\n" + "=" * 60)
        print(f"Generating {mode.replace('_', ' ')} content...")
        print("=" * 60 + "\n")
        
        try:
            content = generate_content(mode, topic)
            print(content)
        except Exception as e:
            print(f"Error generating content: {e}")
        
        print("\n")


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="AI Content Engine Lite - Basic Content Generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python ai_content_engine_lite.py --mode blog --topic "Healthy eating tips"
  python ai_content_engine_lite.py --mode tweet_thread --topic "Startup lessons"
  python ai_content_engine_lite.py --interactive
  
Note: This is the Lite version with 2 modes. Upgrade to Full Commercial
for all 5 modes (Blog, YouTube, Twitter, Social, SEO) plus:
  - AI provider integration
  - Extended documentation
  - Template customization guide
  - Priority support
        """
    )
    
    parser.add_argument(
        "--mode", "-m",
        choices=list(MODES.keys()),
        help="Content generation mode (blog or tweet_thread)"
    )
    
    parser.add_argument(
        "--topic", "-t",
        type=str,
        help="Topic or brief for content generation"
    )
    
    parser.add_argument(
        "--interactive", "-i",
        action="store_true",
        help="Run in interactive mode"
    )
    
    parser.add_argument(
        "--output", "-o",
        type=str,
        help="Output file path (optional)"
    )
    
    args = parser.parse_args()
    
    # Interactive mode
    if args.interactive:
        interactive_mode()
        return
    
    # Command-line mode
    if not args.mode or not args.topic:
        parser.print_help()
        print("\n" + "=" * 60)
        print("LITE VERSION - 2 modes available: blog, tweet_thread")
        print("Upgrade to Full Commercial for all 5 modes!")
        print("=" * 60)
        sys.exit(1)
    
    try:
        content = generate_content(args.mode, args.topic)
        
        if args.output:
            with open(args.output, 'w') as f:
                f.write(content)
            print(f"Content saved to: {args.output}")
        else:
            print(content)
            
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
