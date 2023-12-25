from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import Files
from mkdocs.structure.pages import Page
from importlib import resources as impresources
from . import css, js

inp_file = (impresources.files(css) / 'quiz.css')
with inp_file.open("rt") as f:
    style = f.read()

style = '<style type="text/css">{}</style>'.format(style)

js_file = (impresources.files(js) / 'quiz.js')
with js_file.open("rt") as f:
    js = f.read()

js = '<script type="text/javascript" defer>{}</script>'.format(js)


class MkDocsQuizPlugin(BasePlugin):
    def __init__(self):
        self.enabled = True
        self.dirty = False

    def on_startup(self, *, command, dirty: bool) -> None:
        """Configure the plugin on startup."""
        self.dirty = dirty

    def on_page_markdown(self, markdown, page, config, **kwargs):
        if "quiz" in page.meta:
            if page.meta["quiz"] == "disable":
                return markdown
        REGEX = r'quiz-start(.*?)quiz-end'
        import re
        matches = re.findall(REGEX, markdown, re.DOTALL)
        quiz_id = 0
        for match in matches:
            quiz_lines = match.splitlines()
            # Remove 0 and -1 if empty
            if quiz_lines[0] == "":
                quiz_lines = quiz_lines[1:]
            if quiz_lines[-1] == "":
                quiz_lines = quiz_lines[:-1]
            question = quiz_lines[0].split("quiz-question: ")[1]

            answers = quiz_lines[1: quiz_lines.index("quiz-content:")]
            # correct_answer = list(filter(lambda x: x.startswith(
            #     "quiz-answer-correct: "), answers))[0].split("quiz-answer-correct: ")[1]
            multiple_correct = list(
                filter(lambda x: x.startswith("quiz-answer-correct: "), answers))
            multiple_correct = list(
                map(lambda x: x.split("quiz-answer-correct: ")[1], multiple_correct))
            as_checkboxes = len(multiple_correct) > 1
                
            answers = list(
                map(lambda x: x.startswith("quiz-answer-correct: ") and x.split("quiz-answer-correct: ")[1] or x.startswith("quiz-answer: ") and x.split("quiz-answer: ")[1], answers))
            full_answers = []
            for i in range(len(answers)):
                is_correct = answers[i] in multiple_correct
                input_id = "quiz-{}-{}".format(quiz_id, i)
                input_type = as_checkboxes and "checkbox" or "radio"
                correct = is_correct and "correct" or ""
                full_answers.append('<div><input type="{}" name="answer" value="{}" id="{}" {}><label for="{}">{}</label></div>'.format(
                    input_type, i, input_id, correct, input_id, answers[i]))
            # Get the content of the quiz
            content = quiz_lines[quiz_lines.index("quiz-content:") + 1:]
            quiz = '<div class="quiz"><h3>{}</h3><form><fieldset>{}</fieldset><button type="submit" class="quiz-button">Show Answer</button></form><section class="content hidden">{}</section></div>'.format(
                question, "".join(full_answers), "\n".join(content))
            old_quiz = "quiz-start" + match + "quiz-end"
            markdown = markdown.replace(old_quiz, quiz)
            quiz_id += 1
        return markdown

    def on_page_content(self, html: str, *, page: Page, config: MkDocsConfig, files: Files) -> str | None:

        html = html + style + js
        return html
