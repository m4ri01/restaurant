import React,{useEffect,useState} from 'react';
import axios from 'axios';
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
import { useNavigate } from 'react-router-dom';
import FormatCurrency from '../../tools/FormatCurrency';

function getDate() {
    const today = new Date();
    return today;
  }


  function Table() {
    const [dataOrder, setDataOrder] = useState([]);
    const [dataFoodTransactions, setDataFoodTransactions] = useState([]);
    const [expandedRows, setExpandedRows] = useState(new Set());
    const [isLoading, setIsLoading] = useState(true);
    const [error, setError] = useState(null);
    const [date, setDate] = useState(getDate());
    const navigate = useNavigate();
    useEffect(() => {
      let isMounted = true; 
      const fetchData = async () => {
          setIsLoading(true);
          setError(null);
          // console.log(date);
          const formattedDate = `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()}`;
          console.log(formattedDate);
          try {
         
          const resultOrder = await axios.get(`${process.env.REACT_APP_ENDPOINT_URL}/order_and_payments/${formattedDate}`, {});
          const resultFoodTransactions = await axios.get(`${process.env.REACT_APP_ENDPOINT_URL}/food_transactions/${formattedDate}`, {});
          if (isMounted) {
            setDataOrder(resultOrder.data);
            setDataFoodTransactions(resultFoodTransactions.data);
          }
        } catch (error) {
          if (isMounted) {

              setError(error.message);
              setDataOrder([]); // reset data
              setDataFoodTransactions([]); // reset data
          }
          console.error(error);
        } finally {
          if (isMounted) {
              setIsLoading(false);
          }
        }
      };
      fetchData();
      return () => {
          isMounted = false; // cleanup function to prevent memory leak
      };
    }, []);

    const handleCalendarClose = () => {
        const fetchData = async () => {
            setIsLoading(true);
            setError(null);
            
            const formattedDate = `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()}`;
            console.log(formattedDate);
            
          try { 
            const resultOrder = await axios.get(`${process.env.REACT_APP_ENDPOINT_URL}/order_and_payments/${formattedDate}`, {});
            const resultFoodTransactions = await axios.get(`${process.env.REACT_APP_ENDPOINT_URL}/food_transactions/${formattedDate}`, {});
            if (resultOrder.data.length > 0 && resultFoodTransactions.data.length > 0) {
                setDataOrder(resultOrder.data);
                setDataFoodTransactions(resultFoodTransactions.data);
            }else{
                setDataOrder([]); // reset data
                setDataFoodTransactions([]); // reset data
            }
          } catch (error) {
            if (error) {
                setError(error.message);
                setDataOrder([]); // reset data
                setDataFoodTransactions([]); // reset data
            }
            console.error(error);
          } finally {
            setIsLoading(false);
          }
        }
        fetchData();
        console.log('Calendar closed');

    }
    const toggleRowExpansion = (orderId) => {
        const newExpandedRows = new Set(expandedRows);
        if (newExpandedRows.has(orderId)) {
          newExpandedRows.delete(orderId);
        } else {
          newExpandedRows.add(orderId);
        }
        setExpandedRows(newExpandedRows);
      };

      const ExpandableTable = () => {
        if (isLoading) return <div>Loading...</div>;
        if (error) return <div>Error: {error}</div>;
    
        return (
            <table id="example2" className="table table-bordered table-striped">
            <thead>
              <tr>
                <th>No.</th>
                <th>User Name</th>
                <th>Total Price</th>
                
                <th>Payment Status</th>
                <th>Order Status</th>
                <th>Date and Time</th>
                <th>Details</th>

                {/* Add more headers as needed */}
              </tr>
            </thead>
            <tbody>
              {dataOrder.map((order,index) => (
                <React.Fragment key={order.id}>
                  <tr onClick={() => toggleRowExpansion(order.id)}>
                    <td>{index+1}</td>
                    <td>{order.user_name}</td>
                    <td>{FormatCurrency(order.total_price)}</td>
                    
                    <td style={{ backgroundColor: order.payment_status === 1 ? 'green' : 'red', color: 'white', textAlign: 'center' }}>
                    {order.payment_status === 1 ? 'Paid' : 'Not Paid'}
                    </td>

                    <td style={{ backgroundColor: order.order_status === 1 ? 'green' : 'yellow', color: order.order_status === 1 ? 'white' : 'black', textAlign: 'center' }}>
                    {order.order_status === 1 ? 'Serving' : 'Cooking'}
                    </td>
                    <td>{order.created_at}</td>

                    <td>
                      <button className="btn btn-info" onClick={() => toggleRowExpansion(order.id)}>Details</button>
                    </td>
                    
                    {/* Render other order details as needed */}
                  </tr>
                  {expandedRows.has(order.id) && dataFoodTransactions.filter(ft => ft.order_id === order.id).map((transaction,index_details) => (
                    <tr key={transaction.id} className="child-row">
                      <td colspan={2}>item {index_details+1}</td>
                      <td colSpan={5}>
                        {transaction.food_name} - {transaction.total_item} items - {FormatCurrency(transaction.total_price)}
                      </td>
                      {/* Render other transaction details as needed */}
                    </tr>
                  ))}
                </React.Fragment>
              ))}
            </tbody>
          </table>
        );
      };

      return (
        <div className="card-body">
        <div className='row'>
            <div className='col-md-4'>
            <DatePicker showIcon selected={new Date(date)} onChange={date=>setDate(date)}  onCalendarClose={handleCalendarClose}
            style={{ marginBottom: '10px' }} />
            </div>
            <div className='col-md-4'>
            
            </div>
            <div className='col-md-4'></div>
        </div>
        <ExpandableTable />
        </div>
      );
}

export default Table;
