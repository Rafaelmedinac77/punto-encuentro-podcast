import { useState } from 'react';
import { Send } from 'lucide-react';
import { apiPost } from '../api/client';

export default function Newsletter() {
  const [email, setEmail] = useState('');
  const [message, setMessage] = useState('');
  async function submit(e) {
    e.preventDefault();
    try { await apiPost('/content/subscribe/', { email }); setMessage('Suscripción registrada.'); setEmail(''); }
    catch { setMessage('No se pudo registrar el correo.'); }
  }
  return <section className="newsletter">
    <h3>Recibe contenido exclusivo</h3>
    <p>Reflexiones, novedades y recursos directos en tu correo.</p>
    <form onSubmit={submit}><input value={email} onChange={e=>setEmail(e.target.value)} placeholder="Tu correo electrónico" type="email" required/><button>Suscribirme <Send size={16}/></button></form>
    {message && <small>{message}</small>}
  </section>;
}
