export default class DonutCardComponent {
  constructor(root) {
      this.root = root;
  }

  getHTML(props) {
    return (
      `
      <div class="card card-donut">
        <img src="${props.picture || 'static/img/donut-default.jpg'}" alt="${props.name}" class="card-img donut-img">
        <div class="card-body">
          <h2 class="card-title">${props.name}</h2>
          <h3 class="card-text">${props.cost} руб.</h3>
          <button class="btn btn-primary" id="click-card-${props.id}" data-id="${props.id}">Подробнее о пончике</button>
        </div>
      </div>
      `
    )
  }

  addListeners(props, listener) {
    document
        .getElementById(`click-card-${props.id}`)
        .addEventListener("click", listener);
  }

  render(props, listener) {
    const html = this.getHTML(props)
    this.root.insertAdjacentHTML('beforeend', html)
    this.addListeners(props, listener);
  }
}
