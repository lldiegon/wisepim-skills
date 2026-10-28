# WisePIM skills

Public, reusable workflows for connected WisePIM catalogs in Claude, ChatGPT and Codex. These are instructions, not a hosted service or proof of a directory listing.

| Skill | Purpose |
| --- | --- |
| `catalog-quality-audit` | Inspect stored quality and missing content with explicit sample coverage. |
| `prepare-product-translations` | Prepare a native translation action with exact locales, selection and human review. |
| `channel-readiness-review` | Compare available catalog evidence against explicit channel requirements without claiming publication or certification. |

## Use and distribution

Each directory under `skills/` is a standalone skill with a `SKILL.md` entrypoint. These skills require the authenticated WisePIM MCP tools named in their instructions. Installing instructions alone does not connect an account. No API keys belong in this repository.

The [Claude package](https://github.com/lldiegon/wisepim-claude-plugin) and [ChatGPT package](https://github.com/lldiegon/wisepim-chatgpt-plugin) vendor a reviewed revision of this repository during their builds. Their release locks record the source Git revision and file hashes. Change the canonical instructions here, then rebuild the packages; do not maintain independent copies.

The hosted gateway belongs to the private WisePIM frontend repository; OAuth, permission checks, previews and task execution remain authoritative in the WisePIM backend. `https://wisepim.com/mcp` is the intended gateway URL. Deployment and directory approval must be verified separately.

## Validation

```sh
python3 scripts/validate.py
```

Run the synthetic scenarios in `evals/scenarios.json` with the built plugin on each host. The fixtures contain fictional identifiers and no customer content. Record observed tool calls and answers; static validation does not establish model behavior.

## Contributing

Keep skills concise, use only tools that actually exist, preserve project identity and manual content, and distinguish stored evidence, proposals, queued tasks and saved outcomes. Add a behavioral scenario for meaningful workflow changes. See [SECURITY.md](SECURITY.md) for reporting a security issue.

MIT licensed. The license covers this repository's instructions and tooling, not WisePIM service access or customer data.
