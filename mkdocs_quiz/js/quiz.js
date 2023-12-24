document.querySelectorAll('.quiz').forEach((quiz) => {
  console.log(quiz);
  let form = quiz.querySelector('form');
  let fieldset = form.querySelector('fieldset');
  form.addEventListener('submit', (event) => {
    event.preventDefault();
    console.log('Submitted');
    let answer = form.querySelector('input[name="answer"]:checked');
    console.log(answer);
    if (answer) {
      let correct = answer.hasAttribute('correct');
      let section = quiz.querySelector('section');
      // section.classList.remove('hidden');
      if (correct) {
        section.classList.remove('hidden');
        resetFieldset(fieldset);
        answer.parentElement.classList.add('correct');
      } else {
        section.classList.add('hidden');
        resetFieldset(fieldset);
        answer.parentElement.classList.add('wrong');
      }
    }
  });
});

function resetFieldset(fieldset) {
  const fieldsetChildren = fieldset.children;
  for (let i = 0; i < fieldsetChildren.length; i++) {
    fieldsetChildren[i].classList.remove('wrong');
    fieldsetChildren[i].classList.remove('correct');
  }
}
