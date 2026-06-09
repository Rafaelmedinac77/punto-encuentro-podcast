import { useEffect, useState } from 'react';
import { apiGet } from '../api/client';

export default function Guests() {
  const [guests, setGuests] = useState([]);
  useEffect(() => { apiGet('/content/guests/').then(setGuests).catch(() => {}); }, []);
  return <main className="page"><h1>Invitados</h1><div className="guest-grid">{guests.map(g => <div className="guest" key={g.id}>{g.photo_url ? <img src={g.photo_url} alt={g.name}/> : <div className="avatar">{g.name?.[0]}</div>}<h3>{g.name}</h3><p>{g.profession}</p><small>{g.bio}</small></div>)}</div></main>;
}
