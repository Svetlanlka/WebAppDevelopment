class Urls {
  constructor() {
      this.url = 'http://localhost:8080/';
  }

  donuts() {
      return `donuts/`
  }

  donut(id) {
      return `donuts/${id}/`
  }
}

const urls = new Urls();

export default urls; 
