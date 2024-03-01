// import logo from './logo.svg';

import React,{useEffect,useState} from "react";

//import AddNote from "./components/AddNote";
//import NotesList from "./components/NotesList";

const App = ()=> {
  const [message,setMessage]=useState("");
  const getWelcomeMessage = async()=>{
    const requestOptions ={
      method:"GET",
      headers: {
      "Content-Type":"application/json",
    },
    };
    const respone = await fetch("/api", requestOptions);
    const data = await respone.json();

    console.log(data)
    if (!respone.ok) {
      console.log("something messed up");
    } else {
      setMessage(data.message);
    }
    
  };
  useEffect(()=>{
    getWelcomeMessage();
  },[]);
//   display_data_limit(($limit)=>{
//     global $conn;
//     $sql = "SELECT * FROM infor_news ORDER BY id DESC limit $limit  " ;
    
//     $result = $conn->query($sql);

//     return $result;
// }
  return (
        <div>
          <h1>Information Table Bat Dong San</h1>
          <h1>{message}</h1>
          <div>
          <div class="table-responsive">
            <table class="table table-bordered">
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Tiêu đề</th>
                  <th>Tiêu đề địa chỉ</th>
                  <th>Địa chỉ</th>
                  <th>Giá</th>
                  <th>Đơn giá</th>
                  <th>Phòng ngủ</th>
                  <th>Nhà vệ sinh</th>
                  <th>Pháp lý</th>
                  <th>Nội thất</th>
                  <th>Mặt đường</th>
                  <th>Mặt tiền</th>
                  <th>Số tầng</th>
                  <th>Hướng ban công</th>
                  <th>Diện tích</th>
                  <th>Loại</th>
                </tr>
              </thead>
              <tbody>
                <tr>  
                  <td></td>
                  <td></td>
                  <td></td>              
                  <td></td>
                  <td></td>
                  <td></td>
                  <td></td>
                  <td></td>
                  <td></td>
                  <td></td>
                  <td></td>
                  <td></td>
                  <td></td>
                  <td></td>
                  <td></td>             
                  <td></td>  
                  
                </tr>  
          </tbody>
            </table>
            </div>
          </div>
        </div>
      );
};
export default App;
