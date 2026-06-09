import { Link } from 'react-router-dom';
import { PlayCircle } from 'lucide-react';

export default function EpisodeCard({ episode }) {
  return <Link to={`/episodios/${episode.slug}`} className="episode-card">
    <img src={episode.thumbnail_url || '/placeholder.jpg'} alt={episode.title} />
    <div className="play"><PlayCircle size={34}/></div>
    <div className="episode-meta">
      <strong>{episode.title}</strong>
      <span>{episode.duration || 'Podcast'}</span>
    </div>
  </Link>;
}
