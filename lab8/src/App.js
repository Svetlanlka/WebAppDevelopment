import { BrowserRouter, Route, Link, Switch } from "react-router-dom";
import StartPage from "./pages/start/startPage";

function App() {

  return (
      <BrowserRouter basename="/" >
        <div>
          <ul>
            <li>
              <Link to="/">Старт</Link>
            </li>
            <li>
              <Link to="/new">Хочу на страницу с чем-то новеньким</Link>
            </li>
          </ul>
          <hr />
          <Switch>
            <Route exact path="/">
              <StartPage/>
            </Route>
            <Route path="/new">
              <h1>Это наша страница с чем-то новеньким</h1>
            </Route>
          </Switch>
        </div>
      </BrowserRouter>
  );
}

export default App;
