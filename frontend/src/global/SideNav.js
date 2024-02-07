import SidebarLogo from "../components/SidebarLogo";
import SidebarUserLogo from "../components/SidebarUserLogo";


const Item=({icon,title,link})=>{
  return(
    <li className="nav-item">
          <a href={link} className="nav-link">
            <i className={`nav-icon ${icon}`} />
            <p>
              {title}
            </p>
          </a>
    </li>
  )};



function SideNav() {
  return (
    <div>
<aside className="main-sidebar sidebar-dark-primary elevation-4">
  {/* Brand Logo */}
  <SidebarLogo/>
  {/* Sidebar */}
  <div className="sidebar">
    {/* Sidebar user panel (optional) */}
    <SidebarUserLogo/>
    {/* Sidebar Menu */}
    <nav className="mt-2">
      <ul className="nav nav-pills nav-sidebar flex-column" data-widget="treeview" role="menu" data-accordion="false">
        {/* Add icons to the links using the .nav-icon class
         with font-awesome or any other icon font library */}
        <Item icon="fas fa-book" title="Daily History" link="/daily-history"/>
      </ul>
    </nav>
    {/* /.sidebar-menu */}
  </div>
  {/* /.sidebar */}
</aside>

    </div>
  );
}

export default SideNav;
