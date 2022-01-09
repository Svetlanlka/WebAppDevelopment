import React from "react";
import { Link } from "react-router-dom";

const Header = () => {
    return <header className="header-mg-bottom">
    <nav className="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
      <div className="container-fluid">
        <a className="navbar-brand" href="/">Donuts World</a>
        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarCollapse">
          <ul className="navbar-nav me-auto mb-2 mb-md-0">
            <div className="d-flex">
              <li className = "nav-item me-2">
                <Link to="/">
                  <div className="btn my-btn">
                    Главная страница
                   </div>
                </Link>
              </li>
              <li className = "nav-item me-2">
                <Link to="/donuts">
                  <div className="btn my-btn">
                    Все пончики
                  </div>
                </Link>
              </li>
              <li className = "nav-item me-2">
                <Link to="/donuts/1">
                  <div className="btn my-btn">
                    1 пончик
                  </div>
                </Link>
              </li>
            </div>
          </ul>
          <div className="d-flex">
            <div className = "d-flex">
              <div className = "container-sm">
                <div className="row">
                  <a className="btn btn-sm btn-outline-secondary" href="/">Log out</a>
                </div>
                <div className="row">
                  <a className="btn btn-sm btn-outline-secondary" href="/">Settings</a>
                </div>
              </div>
            </div>
            <div className="d-flex container align-items-center text-secondary">
              <img src="/static/img/avatar.jpg" className="my-avatar rounded" alt="avatar"/>
              <div className="m-2">Светлана</div>
            </div>
          </div>
        </div>
      </div>
    </nav>
  </header>
}

export default Header