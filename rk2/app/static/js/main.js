const plus = document.querySelector('.plus')
plus?.addEventListener('click', () => {
  const title = document.querySelector('.os-form-title')
  const submitBtn = document.querySelector('.os-btn-submit')
  const form = document.querySelector('.os-form')
  if (form.style.display == 'none') {
    form.style.display = 'flex'
    title.innerHTML = 'Добавление операционной системы компьютера:'
    submitBtn.innerHTML = 'Добавить'
  } else {
    form.style.display = 'none'
  }
})