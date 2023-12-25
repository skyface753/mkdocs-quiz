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

## Multiple choice

You can also create a multiple choice quiz, by providing multiple answers as correct.

```bash
quiz-start
quiz-question: Are you ready?
quiz-answer-correct: Yes!
quiz-answer-correct: Maybe!
quiz-answer: No!
quiz-content:
<h4>Great!</h4>
quiz-end
```

## Screenshots

### Quiz (single choice)

<img src="assets/images/quiz.png" width="400rem">

### Quiz (multiple choice)

<img src="assets/images/quiz-multi.png" width="400rem">

## Disable for a page

```markdown
---
quiz: disable
---
```
