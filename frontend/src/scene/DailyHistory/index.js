import Footer from "../../global/Footer";
import Header from "../../global/Header";
import SideNav from "../../global/SideNav";
import PageHeader from "../../components/PageHeader";
import Table from "./Table";


function  DailyHistory() {
  return (
    <div>
      <Header />
      <SideNav />
        <div className="content-wrapper">
        <PageHeader title="Daily History" />
        <section className="content">
            <div className="container-fluid">
            <div className="row">
                <div className="col-12">
                <div className="card">
                    <div className="card">
                    <Table/>
                    </div>
                    {/* /.card */}
                </div>
                {/* /.col */}
                </div>
            </div>{/* /.container-fluid */}
            </div></section>
        {/* /.content */}
        </div>

      <Footer />
    </div>
  );
}


export {DailyHistory};

// export default Role;