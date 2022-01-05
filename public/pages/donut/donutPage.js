import DonutComponent from '../../components/donut/donutComponent.js';
import ButtonComponent from '../../components/button/button.js';
import MainPage from '../main/mainPage.js';
import urls from '../../module/urls.js';
import ajax from '../../module/ajax.js';

export default class DonutPage {
  constructor(root, id) {
    this.root = root;
    this.id = id;
  }

  getData() {
    return ajax.get({url: urls.donut(this.id)});
  }

  get page() {
    return document.getElementById('donut-page');
  }

  getHTML() {
    return (
      `
        <div id="donut-page"></div>
      `
    );
  }

  render() {
      this.root.innerHTML = '';
      const html = this.getHTML();
      this.root.insertAdjacentHTML('beforeend', html);

      // const data = await this.getData()
      // const donut = new DonutComponent(this.page)
      // donut.render(data)

      // const backBtn = new ButtonComponent(this.page);
      // backBtn.render({sign: 'Назад'}, (e) => {
      //     const mainPage = new MainPage(this.root);
      //     mainPage.render();
      // });

      const donut = new DonutComponent(this.page);
      this.getData().then(({data}) => {
        console.log("data:", data)
        donut.render(data);

        const backBtn = new ButtonComponent(this.page);
        backBtn.render({sign: 'Назад'}, (e) => {
          const mainPage = new MainPage(this.root);
          mainPage.render();
        });
      });
  }
}