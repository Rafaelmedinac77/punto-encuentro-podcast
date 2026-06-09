import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { apiGet } from '../api/client';
import EpisodeCard from '../components/EpisodeCard';

export default function EpisodeDetail() {
  const { slug } = useParams();
  const [data, setData] = useState(null);
  useEffect(() => { apiGet(`/content/episodes/${slug}/`).then(setData).catch(() => {}); }, [slug]);
  const ep = data?.episode;
  if (!ep) return <main className="page"><h1>Cargando episodio...</h1></main>;
  return <main className="page episode-detail"><h1>{ep.title}</h1><p>{ep.subtitle}</p><div className="video-wrap"><iframe src={ep.embed_url} title={ep.title} allowFullScreen /></div><article><h2>Descripción</h2><p>{ep.description}</p>{ep.reflection && <div className="reflection small"><span>Reflexión del episodio</span><h2>{ep.reflection}</h2></div>}</article><h2>Episodios relacionados</h2><div className="cards">{data.related.map(item => <EpisodeCard key={item.id} episode={item}/>)}</div></main>;
}
