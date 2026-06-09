import { Link, NavLink } from 'react-router-dom';
import { Play, Music2, Camera } from 'lucide-react';

export default function Header() {
  return (
    <header className="site-header">
      <Link className="brand" to="/">
        <div className="brand-seal">PE</div>
        <span>Punto de Encuentro</span>
      </Link>

      <nav>
        <NavLink to="/">Inicio</NavLink>
        <NavLink to="/episodios">Episodios</NavLink>
        <NavLink to="/invitados">Invitados</NavLink>
        <NavLink to="/sobre-nosotros">Sobre nosotros</NavLink>
        <NavLink to="/recursos">Recursos</NavLink>
        <NavLink to="/contacto">Contacto</NavLink>
      </nav>

      <div className="header-actions">
        <Music2 size={18} />
        <Camera size={18} />
        <Link className="gold-btn" to="/episodios">
          Escuchar ahora <Play size={15} />
        </Link>
      </div>
    </header>
  );
}
