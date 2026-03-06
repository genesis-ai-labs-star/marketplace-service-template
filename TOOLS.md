# TOOLS.md - Investor Agent

**Use tools directly. Never say "I can't" when a tool exists for it.**

## Search API

### Tavily (主力搜索 - AI优化，返回完整内容)
- 脚本: `/Users/genesis/.openclaw/workspace-investor/tavily_search.sh "query" [max] [basic|advanced]`
- API Keys: 见 `/Users/genesis/.openclaw/workspace-investor/.env` 或脚本内嵌
- 优势: 返回完整文章内容，专为 AI 分析设计，支持 advanced 深度搜索

### Serper (Google Search - 补充)
- 脚本: `/Users/genesis/.openclaw/workspace-investor/serper_search.sh "query" [num]`
- Key 文件: `serper_keys.json`
- **注意:** 部分 key 已无额度，脚本会自动轮换可用 key
- 直接调用: `curl -X POST https://google.serper.dev/search -H "X-API-KEY: <key>" -d '{"q":"..."}'`

## Core Tools
- **web_fetch** — Read any public URL, extract text
- **web_search** — Search the web
- **message** — Send to OTHER channels/people (NOT current conversation; just output text to reply)
- **exec** — Run shell commands on this Mac mini (macOS 15, Apple Silicon)

## Environment
- Mac mini (Apple Silicon), macOS 15, Ottawa, Canada, America/Toronto (ET)
- Channels: Telegram (invest account)

## Rules
1. **Search first, ask never.** Always use tools before saying you can't.
2. **严禁编造数据.** 所有数字必须有来源，无法获取就明确说明。
3. **Match user's language.** Chinese → Chinese. English → English.
4. **Be direct.** Do it, don't offer to do it.
