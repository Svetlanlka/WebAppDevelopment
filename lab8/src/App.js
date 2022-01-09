import { BrowserRouter, Route, Switch } from "react-router-dom";
import {useEffect, useState} from 'react';

import MainPage from "./pages/main/mainPage";
import DonutPage from "./pages/donut/donutPage";
import DonutsPage from "./pages/donuts/donutsPage";
import Header from "./components/header/header";
import Footer from "./components/footer/footer";
import Loading from "./components/loading/loading";
import "./App.css"

import ajax from "./modules/ajax";
import urls from "./modules/urls";

function App() {
  const [loading, setLoading] = useState(false);
  const [donuts, setDonuts] = useState([]);

  const donutsLoading = () => {
    setLoading(true);
    ajax.get({url: urls.donuts()}).then(({response}) => {
      setDonuts(response)
      setLoading(false)
    });
  }

  useEffect(() => {
    donutsLoading();
  }, []);

  return (
      <BrowserRouter basename="/" >
        <Header/>
        <Switch>
          <Route exact path="/">
            {loading && <Loading/>}
            {!loading && <MainPage/>}
          </Route>
          <Route exact path="/donuts">
            {loading && <Loading/>}
            {!loading && <DonutsPage donuts={donuts}/>}
          </Route>
          <Route path="/donuts/:donutId">
            {loading && <Loading/>}
            {!loading && <DonutPage donuts={donuts}/>}
          </Route>
        </Switch>
        <Footer/>
      </BrowserRouter>
  );
}

export default App;
