import { BrowserRouter, Route, Link, Switch } from "react-router-dom";
import StartPage from "./pages/start/startPage";
import MainPage from "./pages/main/mainPage";
import "./App.css"

function App() {

  return (
      <BrowserRouter basename="/" >
        <div>
          <ul>
            <li>
              <Link to="/">Старт</Link>
            </li>
            <li>
              <Link to="/example">Хочу на страницу с чем-то новеньким</Link>
            </li>
          </ul>
          <hr />
          <Switch>
            <Route exact path="/">
              <MainPage/>    
            </Route>
            <Route path="/example">
              <StartPage/>
            </Route>
          </Switch>
        </div>
      </BrowserRouter>
  );
}

export default App;
