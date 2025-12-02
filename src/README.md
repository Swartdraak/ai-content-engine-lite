# Source Code - Lite Version

This directory contains the limited source code for AI Content Engine Lite.

## Contents

```
src/
├── ai_content_engine_lite.py   # Main CLI application
└── modes/                      # Content generation modules
    ├── __init__.py
    ├── blog.py                 # Blog post generator
    └── tweet_thread.py         # Tweet thread generator
```

## Quick Usage

```bash
# Generate a blog post
python ai_content_engine_lite.py --mode blog --topic "your topic"

# Generate a tweet thread
python ai_content_engine_lite.py --mode tweet_thread --topic "your topic"

# Interactive mode
python ai_content_engine_lite.py --interactive

# Save to file
python ai_content_engine_lite.py --mode blog --topic "topic" --output article.md
```

## Limitations

This Lite version includes only 2 of the 5 available modes:

| Mode | Available |
|------|:---------:|
| Blog | ✅ |
| Tweet Thread | ✅ |
| YouTube Script | ❌ |
| Social Caption | ❌ |
| SEO Snippet | ❌ |

## Upgrade to Full

The Full Commercial version includes:

- All 5 content modes
- Extended templates
- AI provider integration
- Configuration system
- Complete documentation
- Test suite
- Commercial use rights

See `../UPGRADE_TO_FULL.md` for details.

---

*AI Content Engine Lite - Evaluation Version*
