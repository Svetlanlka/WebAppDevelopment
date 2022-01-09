import React, {useEffect, useState} from 'react';
import {Card, Col, Row, Button, Spinner} from "react-bootstrap";
import DonutCard from '../../components/donutCard/donutCard';
import InputField from '../../components/inputField/inputField';
import Loading from '../../components/loading/loading';

import ajax from '../../modules/ajax';
import urls from '../../modules/urls';

function MainPage() {
  const [searchValue, setSearchValue] = useState('Шоколадка');
  const [loading, setLoading] = useState(false);
  const [donuts, setDonuts] = useState([]);

  const handleSearch = () => {
    setLoading(true);
    ajax.get({url: urls.donuts()}).then(({response}) => {
      console.log("response:")
      console.log(response)
      setDonuts(response.filter(item => item.name && item.name.toLowerCase().includes(searchValue.toLowerCase())));
      setLoading(false)
    });
  }

  return (
    <div className='my-background d-flex justify-content-center flex-column align-items-center'>
      <h1 className='welcome-title'>Welcome to Donuts World!</h1>
      <InputField value={searchValue} setValue={setSearchValue} placeholder="поиск" loading={loading} onSubmit={handleSearch} buttonTitle="Искать"/>
      {loading && <Loading/>}
      {!loading && !donuts.length ? <h1 className='welcome-error'>Пончики не найдены</h1>:
        <div className="d-flex justify-content-center flex-wrap">
          {donuts?.map((item, index)=>{
              return(
                  <div key={index}>
                      <DonutCard donutLoad={item}/>
                  </div>
              )
          })}
        </div>
      }
    </div>
  );
}

export default MainPage;