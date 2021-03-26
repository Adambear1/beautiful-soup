import React from "react";

function Searchbar({search, loading}) {
  const value =  React.useRef()
  return (
    <div class="input-group">
      <div class="form-outline">
        <input type="search" id="form1" class="form-control" ref={value}/>
        <label class="form-label" for="form1">
          Search
        </label>
      </div>
      <button type="button" class="btn btn-primary" onClick={()=>search(value.current)}>
        {!loading ? <i class="fas fa-search"></i> : <div class="spinner-border text-light" role="status">
  <span class="visually-hidden">Loading...</span>
</div>}
      </button>
    </div>
  );
}

export default Searchbar;
