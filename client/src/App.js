import { useEffect, useState } from "react";
// Components
import SearchBar from "./components/Searchbar";
// utils
import axios from "axios"

function App() {
  const [loading, setLoading] = useState(false)
  const search = ({value}) => {
    setLoading(true)
    axios.get("http://127.0.0.1:5000/api/search_topic/" + value).then(({data})=>{
      setLoading(false)
      console.log(data)
    })
  }

  return (
    // <div className="container">
      <div className="text-center mt-5">
        <SearchBar
        search={search}
        loading={loading}
      /></div>
      

     
    // </div>
  );
}

export default App;
