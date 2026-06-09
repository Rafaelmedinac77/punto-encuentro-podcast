import React from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import App from './App';
import Home from './pages/Home';
import Episodes from './pages/Episodes';
import EpisodeDetail from './pages/EpisodeDetail';
import Guests from './pages/Guests';
import About from './pages/About';
import Resources from './pages/Resources';
import Contact from './pages/Contact';
import './styles.css';

createRoot(document.getElementById('root')).render(
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<App />}>
        <Route index element={<Home />} />
        <Route path="episodios" element={<Episodes />} />
        <Route path="episodios/:slug" element={<EpisodeDetail />} />
        <Route path="invitados" element={<Guests />} />
        <Route path="sobre-nosotros" element={<About />} />
        <Route path="recursos" element={<Resources />} />
        <Route path="contacto" element={<Contact />} />
      </Route>
    </Routes>
  </BrowserRouter>
);
