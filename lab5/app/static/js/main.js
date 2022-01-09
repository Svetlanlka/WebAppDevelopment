const plus = document.querySelector('.plus')
plus?.addEventListener('click', () => {
  const title = document.querySelector('.donut-form-title')
  const submitBtn = document.querySelector('.donut-btn-submit')
  const form = document.querySelector('.donut-form')
  if (form.style.display == 'none') {
    form.style.display = 'flex'
    title.innerHTML = 'Добавление пончика:'
    submitBtn.innerHTML = 'Добавить'
  } else {
    form.style.display = 'none'
  }
})