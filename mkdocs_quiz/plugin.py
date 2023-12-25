from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import Files
from mkdocs.structure.pages import Page
from importlib import resources as impresources
import re
from . import css, js
import re
inp_file = (impresources.files(css) / 'quiz.css')
with inp_file.open("rt") as f:
    style = f.read()

style = '<style type="text/css">{}</style>'.format(style)

js_file = (impresources.files(js) / 'quiz.js')
with js_file.open("rt") as f:
    js = f.read()

js = '<script type="text/javascript" defer>{}</script>'.format(js)

# <?quiz?>
# question: Are you ready?
# answer-correct: Yes!
# answer: No!
# answer: Maybe!
# content:
# <h2>Provide some additional content</h2>
# <?/quiz?>

class MkDocsQuizPlugin(BasePlugin):
    def __init__(self):
        self.enabled = True
        self.dirty = False

    def on_startup(self, *, command, dirty: bool) -> None:
        """Configure the plugin on startup."""
        self.dirty = dirty

    def on_page_markdown(self, markdown, page, config, **kwargs):
        if "quiz" in page.meta and page.meta["quiz"] == "disable":
            return markdown
        # Regex from quiz_tag
        QUIZ_START_TAG = "<?quiz?>"
        QUIZ_END_TAG = "<?/quiz?>"
        REGEX = r'<\?quiz\?>(.*?)<\?/quiz\?>'
        matches = re.findall(REGEX, markdown, re.DOTALL)
        quiz_id = 0
        for match in matches:
            quiz_lines = match.splitlines()
            # Remove 0 and -1 if empty
            while quiz_lines[0] == "":
                quiz_lines = quiz_lines[1:]
            while quiz_lines[-1] == "":
                quiz_lines = quiz_lines[:-1]
            question = quiz_lines[0].split("question: ")[1]

            answers = quiz_lines[1: quiz_lines.index("content:")]
            # correct_answer = list(filter(lambda x: x.startswith(
            #     "quiz-answer-correct: "), answers))[0].split("quiz-answer-correct: ")[1]
            multiple_correct = list(
                filter(lambda x: x.startswith("answer-correct: "), answers))
            multiple_correct = list(
                map(lambda x: x.split("answer-correct: ")[1], multiple_correct))
            as_checkboxes = len(multiple_correct) > 1
                
            answers = list(
                map(lambda x: x.startswith("answer-correct: ") and x.split("answer-correct: ")[1] or x.startswith("answer: ") and x.split("answer: ")[1], answers))
            full_answers = []
            for i in range(len(answers)):
                is_correct = answers[i] in multiple_correct
                input_id = "quiz-{}-{}".format(quiz_id, i)
                input_type = as_checkboxes and "checkbox" or "radio"
                correct = is_correct and "correct" or ""
                full_answers.append('<div><input type="{}" name="answer" value="{}" id="{}" {}><label for="{}">{}</label></div>'.format(
                    input_type, i, input_id, correct, input_id, answers[i]))
            # Get the content of the quiz
            content = quiz_lines[quiz_lines.index("content:") + 1:]
            quiz = '<div class="quiz"><h3>{}</h3><form><fieldset>{}</fieldset><button type="submit" class="quiz-button">Submit</button></form><section class="content hidden">{}</section></div>'.format(
                question, "".join(full_answers), "\n".join(content))
            # old_quiz = "quiz-start" + match + "quiz-end"
            old_quiz = QUIZ_START_TAG + match + QUIZ_END_TAG
            markdown = markdown.replace(old_quiz, quiz)
            quiz_id += 1
        return markdown

    def on_page_content(self, html: str, *, page: Page, config: MkDocsConfig, files: Files) -> str | None:

        html = html + style + js
        return html
