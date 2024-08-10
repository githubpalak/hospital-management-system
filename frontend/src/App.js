import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './components/Home';
import Patients from './components/Patients';
import Doctors from './components/Doctors';
import Appointments from '.components/Appointments';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />}/>
        <Route path="/patients" element={<Patients />}/>
        <Route path="/doctors" element={<Doctors />}/>
        <Route path="/appointments" element={<Appointments />}/>
      </Routes>
    </Router>
  );
}

export default App;