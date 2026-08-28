# airia-scan-demo

Demo repository for the **Airia Code Scanner**.

Deliberately contains a spread of AI frameworks, direct LLM provider calls, an MCP
server, and synthetic credentials so a scan produces findings across every category.

> **All credentials in this repository are fake placeholders.** They are not valid,
> have never been valid, and exist only so secret-detection rules have something to
> match. Do not replace them with real values.

| Path | What it plants |
|---|---|
| `agents/` | CrewAI, LangGraph, LangChain agent definitions |
| `tools/` | Direct Bedrock + OpenAI provider calls |
| `mcp/` | An MCP server definition |
| `config/` | Config-file credentials |
| `requirements.txt` | AI dependencies |
