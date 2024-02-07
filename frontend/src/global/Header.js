import { useNavigate } from 'react-router-dom';
function Header() {
  const navigate = useNavigate();

  return (
<div>
  {/* Navbar */}
  <nav className="main-header navbar navbar-expand navbar-white navbar-light">
    {/* Left navbar links */}
    <ul className="navbar-nav">
      <li className="nav-item">
        <a className="nav-link" data-widget="pushmenu" href="#" role="button"><i className="fas fa-bars" /></a>
      </li>
    </ul>
    {/* Right navbar links */}
    <ul className="navbar-nav ml-auto">
      {/* Notifications Dropdown Menu */}
      <li className="nav-item dropdown">
        <a className="nav-link" data-toggle="dropdown" href="#">
          <i className="far fa-user" />
        </a>
        <div className="dropdown-menu dropdown-menu-lg dropdown-menu-right">
          <div className="dropdown-divider" />
          <div className="dropdown-divider" />
          <button className="dropdown-item dropdown-footer">
            Logout
        </button>
        </div>
      </li>
    </ul>
  </nav>
  {/* /.navbar */}
</div>

  );
}

export default Header;
