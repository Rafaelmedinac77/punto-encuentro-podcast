import { useEffect, useState } from 'react';
import { apiGet } from '../api/client';
import EpisodeCard from '../components/EpisodeCard';

export default function Episodes() {
  const [episodes, setEpisodes] = useState([]);
  const [q, setQ] = useState('');
  useEffect(() => { apiGet(`/content/episodes/${q ? `?q=${q}` : ''}`).then(setEpisodes).catch(() => {}); }, [q]);
  return <main className="page"><h1>Episodios</h1><p>Explora las conversaciones de Punto de Encuentro.</p><input className="search" value={q} onChange={e=>setQ(e.target.value)} placeholder="Buscar episodio..."/><div className="cards">{episodes.map(ep => <EpisodeCard key={ep.id} episode={ep}/>)}</div></main>;
}
