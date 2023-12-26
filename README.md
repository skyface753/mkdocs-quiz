# MkDocs Quiz Plugin

## Installation

Install the package with pip:

```bash
pip install mkdocs_quiz
```

## Create your first quiz

Add the following to your `mkdocs.yml`:

```yaml
plugins:
  - mkdocs_quiz
```

### Single choice

Now you can create your first quiz directly in markdown:

```bash
<?quiz?>
question: Are you ready?
answer-correct: Yes!
answer: No!
answer: Maybe!
content:
<h2>Provide some additional content</h2>
<?/quiz?>
```

> **Info** The answers can get styled with HTML (like `<code>Yes!</code>`)

> **Warning** The quiz content needs to be valid **_HTML_**

### Multiple choice

You can also create a multiple choice quiz, by providing multiple answers as correct.

```bash
<?quiz?>
question: Are you ready?
answer-correct: Yes!
answer: No!
answer-correct: Maybe!
content:
<h2>Provide some additional content</h2>
<?/quiz?>
```

## [Demo](https://skyface753.github.io/mkdocs-quiz/)

## Screenshots

The single choice quiz will get generated as a radio button group, while the multiple choice quiz will get generated as a checkbox group.

### Single choice

<img src="assets/images/quiz.png" width="400rem">

### Multiple choice

<img src="assets/images/quiz-multi.png" width="400rem">

## Disable for a page

You can disable the quiz for a page by adding the following to the top (meta) of the page:

```markdown
---
quiz: disable
---
```
