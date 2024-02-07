function SidebarUserLogo() {
    return (
      <div className="user-panel mt-3 pb-3 mb-3 d-flex">
      <div className="image">
        <img src="/dist/img/user.png" className="img-circle elevation-2" alt="User Image" />
      </div>
      <div className="info">
        <a href="#" className="d-block">Hi Admin!</a>
      </div>
    </div>
  
    );
  }   
  
  export default SidebarUserLogo;