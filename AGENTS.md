# AGENTS

load:
- .specs/INDEX.md
- .specs/CONTEXT.md

workflow:
- load-spec
- load-dependencies
- load-contracts
- load-rules
- load-checklists
- load-skills

rules:
- respect-dependencies
- do-not-implement-draft-work-items
- validate-checklists
- keep-specs-synchronized
- keep-docs-synchronized
- update-changelog
- specs-are-source-of-truth
- no-agent-self-attribution

precedence:
contracts > rules > spec > code > docs

agent:
- The agent is a tool. It has no authorship, no choice, and no merit.
- Never add agent self-attribution to commits, PR titles/descriptions, code comments, or docs.
- No co-author trailers, no "Generated with ..." lines, no agent name anywhere in history or artifacts.
- All commits and PRs are authored solely by the human owner.