import React from "react";
import './Layout.css'
import { Link, Outlet } from "react-router-dom";


const Layout = () => {
  return (
    <div className="layout">
        <nav className="navbar-layout">
            <ul>
                <li>
                    <Link to="/rent">Rentar capitulo</Link>
                </li>
                <li>
                    <Link to="/alq">Alquilar capitulo</Link>
                </li>
                <li>
                    <Link to="/list">Listar capitulos</Link>
                </li>
            </ul>
        </nav>
        <hr />
        <Outlet />
    </div>
  );
};

export default Layout;