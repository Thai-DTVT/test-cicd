// // import logo from './logo.svg';

 import React,{useEffect,useState} from "react";
 import ReactExport from "react-export-excel";

 const ExcelFile = ReactExport.ExcelFile;
 const ExcelSheet = ReactExport.ExcelFile.ExcelSheet;
 const ExcelColumn = ReactExport.ExcelFile.ExcelColumn;

 

const App = ()=> {
  const [data, setData] = useState([]);

  const getWelcomeMessage = async () => {
    const requestOptions ={
      method:"GET",
      headers: {
        "Content-Type":"application/json",
      },
    };
    const response = await fetch("/api", requestOptions);
    const jsonData = await response.json();
    // clc
    if (!response.ok) {
      console.log("something messed up");
    } else {
      setData(jsonData.slice(0, 10)); // Lấy 10 dòng dữ liệu đầu tiên
    }
  };

  useEffect(() => {
    getWelcomeMessage();
  }, []);

  return (
    <div>
      <h1>Information Table Bat Dong San</h1>
      <div>
          <ExcelFile element={<button>Download Data</button>}>
                <ExcelSheet data={data} name="BDS">
                    <ExcelColumn label="ID" value="id"/>
                    <ExcelColumn label="Tiêu đề" value="title"/>
                    <ExcelColumn label="Tiêu đề địa chỉ" value="title_address"/>
                    <ExcelColumn label="Địa chỉ" value="detail_address"/>
                    <ExcelColumn label="Giá" value="price"/>
                    <ExcelColumn label="Đơn giá" value="unit_price"/>
                    <ExcelColumn label="Phòng ngủ" value="bedroom"/>
                    <ExcelColumn label="Pháp lý" value="law"/>
                    <ExcelColumn label="Nội thất" value="indoor"/>
                    <ExcelColumn label="Mặt tiền" value="face_first"/>
                    <ExcelColumn label="Số tầng" value="floor"/>
                    <ExcelColumn label="Diện tích" value="area"/>
                    <ExcelColumn label="Hướng ban công" value="direction_balcony"/>
                </ExcelSheet>
          </ExcelFile>
        </div>
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
            {data.map(item => (
              <tr key={item.id}>
                <td>{item.id}</td>
                <td>{item.title}</td>
                <td>{item.title_address}</td>
                <td>{item.detail_address}</td>
                <td>{item.price}</td>
                <td>{item.unit_price}</td>
                <td>{item.bedroom}</td>
                <td>{item.toilet}</td>
                <td>{item.law}</td>
                <td>{item.indoor}</td>
                <td>{item.road}</td>
                <td>{item.face_first}</td>
                <td>{item.floor}</td>
                <td>{item.direction_balcony}</td>
                <td>{item.area}</td>
                <td>{item.type_new}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

    </div>
    
  );
};

//export excel
// class Download extends React.Component {
//   render() {
//       return (
//           <ExcelFile element={<button>Download Data</button>}>
//               <ExcelSheet data={data} name="Employees">
//                   <ExcelColumn label="Name" value="title"/>
//                   <ExcelColumn label="Wallet Money" value="toilet"/>
//                   <ExcelColumn label="Gender" value="area"/>
                  
//               </ExcelSheet>
              
//           </ExcelFile>
//       );
//   }
// }

 export default App;
