import { useEffect, useState } from 'react';
import { apiGet } from '../api/client';

export default function Resources() {
  const [articles, setArticles] = useState([]);
  useEffect(() => { apiGet('/content/articles/').then(setArticles).catch(() => {}); }, []);
  return <main className="page"><h1>Recursos</h1><div className="article-grid">{articles.map(a => <article className="article" key={a.id}><h2>{a.title}</h2><p>{a.excerpt}</p></article>)}</div></main>;
}
