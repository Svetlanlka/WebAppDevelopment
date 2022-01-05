import ButtonComponent from '../../components/button/button.js';
import DonutCardComponent from '../../components/donutCard/donutCard.js';
import DonutPage from '../donut/donutPage.js'
import urls from '../../module/urls.js';
import ajax from '../../module/ajax.js';

export default class MainPage {
  constructor(root) {
      this.root = root;
  }

  getData() {
    return ajax.get({url: urls.donuts()});
  }

  // getData() {
  //   return [{
  //       id: 1,
  //       picture: "uploads/donut-1.jpg",
  //       name: "Пончик Зведное небо",
  //       cost: 180,
  //       info: "Вам нравиться наблюдать за красотой ночного неба? За звездами, раскиданными \
  //       по нему. Тогда вам обязательно стоит попробовать наше изделие."
  //   },
  //   {
  //     id: 2,
  //     picture: "uploads/donut-2.jpg",
  //     name: `Пончик "Космическая радость"`,
  //     cost: 130,
  //     info: "Этот пончик космически красив и обязательно порадует вас своим вкусом. "
  //   },
  //   {
  //     id: 3,
  //     picture: "uploads/donut-3.jpg",
  //     name: `Пончик "Галактика"`,
  //     cost: 145,
  //     info: "Вкус этого пончика превосходен. Говорят, что его создатели обладали \
  //     знаниями, присланными издалека, с конца нашей галактики."
  //   },
  // ]
  // }

  get page() {
    return document.getElementById('main-page')
  }

  getHTML() {
    return (
        `
            <div id="main-page" class="d-flex flex-wrap"><div/>
        `
    )
  }

  clickCard(e) {
    const cardId = e.target.dataset.id

    const donutPage = new DonutPage(this.root, cardId)
    donutPage.render()
  }

  render() {
    this.root.innerHTML = ''
    const html = this.getHTML()
    this.root.insertAdjacentHTML('beforeend', html)

    // const data = this.getData()
    // data.forEach((item) => {
    //   const donutCard = new DonutCardComponent(this.page)
    //   donutCard.render(item, this.clickCard.bind(this))
    // })

    this.getData().then((data) => {
      console.log("data:")
      console.log(data)
      data.forEach(item => {
        const donutCard = new DonutCardComponent(this.page)
        donutCard.render(item, this.clickCard.bind(this));
      });
    });
  }
}
