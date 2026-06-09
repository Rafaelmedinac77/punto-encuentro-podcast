import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { BookOpen, Heart, Mic, Play, Users } from 'lucide-react';
import { apiGet } from '../api/client';
import EpisodeCard from '../components/EpisodeCard';
import Newsletter from '../components/Newsletter';

export default function Home() {
  const [data, setData] = useState({ latest: [], guests: [], articles: [] });
  useEffect(() => { apiGet('/content/home/').then(setData).catch(() => {}); }, []);
  const featured = data.featured;
  return <main>
    <section className="hero">
      <div className="hero-copy">
        <span className="eyebrow">Con Santiago Gil Martín</span>
        <h1>Punto de <span>Encuentro</span></h1>
        <p>Conversaciones que transforman vidas.</p>
        <div className="hero-buttons"><Link className="gold-btn" to="/episodios"><Play size={16}/> Ver episodios</Link><Link className="outline-btn" to="/sobre-nosotros">Conoce más</Link></div>
      </div>
      <div className="hero-quote">“Donde hay conversaciones auténticas, comienza el cambio que transforma el alma.”</div>
    </section>

    <section className="featured-grid">
      <div className="featured-card">
        <img src={featured?.thumbnail_url || 'https://images.unsplash.com/photo-1478737270239-2f02b77fc618?q=80&w=1200'} alt="Episodio destacado" />
        <div><span className="eyebrow">Episodio destacado</span><h2>{featured?.title || 'Ocupas del alma'}</h2><p>{featured?.description || 'Espiritualidad, dopamina y la urgencia del alma. Una conversación profunda sobre lo que ocupa tu mente y tu corazón.'}</p><Link className="gold-btn" to={featured ? `/episodios/${featured.slug}` : '/episodios'}><Play size={16}/> Escuchar ahora</Link></div>
      </div>
      <div className="quick-menu">
        <Link to="/episodios"><Mic/> <div><strong>Episodios</strong><span>Explora todos los capítulos</span></div></Link>
        <Link to="/invitados"><Users/> <div><strong>Invitados</strong><span>Historias que inspiran</span></div></Link>
        <Link to="/recursos"><BookOpen/> <div><strong>Recursos</strong><span>Artículos, guías y más</span></div></Link>
        <Link to="/contacto"><Heart/> <div><strong>Únete a la comunidad</strong><span>Sé parte del punto de encuentro</span></div></Link>
      </div>
    </section>

    <section className="section"><h2>Últimos episodios</h2><div className="cards">{data.latest.map(ep => <EpisodeCard key={ep.id} episode={ep}/>)}</div></section>
    <section className="reflection"><span>Reflexión del episodio</span><h2>¿Qué está ocupando el espacio que le corresponde a Dios en tu vida?</h2></section>
    <section className="section"><h2>Invitados destacados</h2><div className="guest-grid">{data.guests.map(g => <div className="guest" key={g.id}><div className="avatar">{g.name?.[0]}</div><h3>{g.name}</h3><p>{g.profession}</p></div>)}</div></section>
    <Newsletter />
  </main>;
}
