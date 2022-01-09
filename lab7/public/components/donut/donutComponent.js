export default class DonutComponent {
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
            <p class="card-text">${props.info}</p>
          </div>
        </div>
        `
    )
}

  render(props) {
      const html = this.getHTML(props)
      this.root.insertAdjacentHTML('beforeend', html)
  }
}
