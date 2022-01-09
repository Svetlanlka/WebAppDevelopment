export default class ButtonComponent {
  constructor(root) {
      this.root = root;
  }

  render(props, onClick) {
    const btnWrapper = document.createElement('div');
    btnWrapper.innerHTML = `<button type="button" class="btn btn-primary">${props.sign}</button>`;
    const btn = btnWrapper.firstChild;
    btn.addEventListener('click', onClick);
    this.root.insertAdjacentElement('beforeend', btn);
  }
}
