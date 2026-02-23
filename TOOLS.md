# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Search API

### Serper (Google Search)
- 脚本: `/Users/genesis/.openclaw/workspace-investor/serper_search.sh "query" [num]`
- Key 文件: `serper_keys.json`（4个key，2个有效，2个无额度）
- 直接调用: `curl -X POST https://google.serper.dev/search -H "X-API-KEY: <key>" -d '{"q":"..."}'`
- **注意:** OpenClaw 内置 `web_search` 不支持 Serper，需通过 exec/curl 调用

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.
