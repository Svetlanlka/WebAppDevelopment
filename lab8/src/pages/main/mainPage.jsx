import React, {useEffect, useState} from 'react';
import {Card, Col, Row, Button, Spinner} from "react-bootstrap";
import DonutCard from '../../components/donutCard/donutCard';
import InputField from '../../components/inputField/inputField';
// import getMusicByName from '../../modules';
import ajax from '../../modules/ajax';
import urls from '../../modules/urls';

function MainPage() {
  const [searchValue, setSearchValue] = useState('radiohead');

  const [filter, setFilter] = useState('');

  const [loading, setLoading] = useState(false)

  const [music, setMusic] = useState([])

  const handleSearch = () => {
    setLoading(true);
    setFilter('');
    ajax.get({url: urls.donuts()}).then(({response}) => {
      // const { results } = await getMusicByName();
      console.log("response:")
      console.log(response)
      // Добавляем в состояние только треки
      setMusic(response.filter(item => item.wrapperType === "track"));
      setLoading(false)
    });
  }

  const handleFilter = ()=> {
      setMusic(music => music.filter(item=>item.artistName && item.artistName.includes(filter)));
  }

  return (
      <div className={`container ${loading && 'containerLoading'}`}>
          {/* {loading && <div className="loadingBg"><Spinner animation="border"/></div>} */}
          <InputField value={searchValue} setValue={setSearchValue} placeholder="поиск" loading={loading} onSubmit={handleSearch} buttonTitle="Искать"/>
          <InputField value={filter} setValue={setFilter} placeholder="Автор" loading={loading} onSubmit={handleFilter} buttonTitle="Отфильтровать"/>
          {!music.length ? <h1>К сожалению, пока ничего не найдено :(</h1>:
              <Row xs={1} md={4} className="g-4">
              {music.map((item, index)=>{
                  return(
                      <Col key={index}>
                          <DonutCard {...item}/>
                      </Col>
                  )
              })}
          </Row>
          }
  </div>
  );
}

export default MainPage;