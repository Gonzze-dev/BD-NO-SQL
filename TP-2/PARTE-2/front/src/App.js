import { Route, Routes } from "react-router-dom";

import './App.css';

import FormRentChapter from "./formRentChapter/FormRentChapter";
import FormAlqChapter from "./formAlqChapter/FormAlqChapter";
import FormGetChapters from "./formGetChapters/FormGetChapters";
import Layout from './layout/Layout';

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path='/' element={<Layout/>}>
          <Route path="/rent" element={<FormRentChapter/>} />
          <Route path="/alq" element={<FormAlqChapter/>} />
          <Route path="/list" element={<FormGetChapters/>} />
        </Route>
      </Routes>
    </div>
  );
}

export default App;
