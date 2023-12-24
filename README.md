# MkDocs Quiz Plugin

## Create your first quiz

```bash
quiz-start
quiz-question: Are you ready?
quiz-answer-correct: <code>Yes!</code>
quiz-answer: No!
quiz-answer: Maybe!
quiz-content:
<h2>Provide some additional content</h2>
quiz-end
```

> **Info** The answers can styled with HTML (like `<code>Yes!</code>`)

> **Warning** The quiz content needs to be valid **_HTML_**

## Disable for a page

```markdown
---
quiz: disable
---
```
