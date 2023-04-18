import React from "react";
import './Layout.css'
import { Link, Outlet } from "react-router-dom";


const Layout = () => {
  return (
    <div className="layout">
        <nav className="navbar-layout">
            <ul>
                <li>
                    <Link to="/add">Agregar Personaje</Link>
                </li>
                <li>
                    <Link to="/delete">Eliminar Personaje</Link>
                </li>
                <li>
                    <Link to="/list">Listar Personajes</Link>
                </li>
            </ul>
        </nav>
        <hr />
        <Outlet />
    </div>
  );
};

export default Layout;