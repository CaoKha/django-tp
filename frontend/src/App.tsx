import React from 'react';
import logo from './logo.svg';
import './App.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import { Navigation } from './components/navigations';

function App() {
  return <BrowserRouter>
    <Navigation></Navigation>
      <Routes>
      <Route path='/' element={<Home/>}/>
      <Route path='/login' element={<Login/>}/>
      <Route path='/' element={<Logout/>}/>
    </Routes>

  </BrowserRouter>;
}

export default App;
