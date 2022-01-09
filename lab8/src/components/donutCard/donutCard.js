import {Card} from "react-bootstrap";
import { Link } from "react-router-dom";
import React, {useState, useEffect} from 'react';

const DonutCard = ({donutLoad, isDonutPage=false}) => {
  const [donut, setDonut] = useState({
    pk: 1,
    name: "Donut name",
    cost: 0,
    info: 'About donut',
    picture: '/static/img/donut-default.jpg'
  });

  useEffect(() => {
    if (donutLoad) {
      setDonut(donutLoad);
    }
  }, [donutLoad]);

  return <Card className="card-donut">
    <Card.Img src = {donut.picture} className="card-img donut-img" alt={donut.name} height={100} width={100}/>
    <Card.Body>
      <div className="textStyle">
        <Card.Title className="card-title">{donut.name}</Card.Title>
      </div>
      <div className="textStyle">
        <Card.Text>{donut.cost} руб.</Card.Text>
      </div>
      {isDonutPage &&
      <div className="textStyle">
        <Card.Text>{donut.info}</Card.Text>
      </div>
      }
      {!isDonutPage &&
      <Link to={`/donuts/${donut.pk}`} >
        <div className="btn my-btn mt-1">Подробнее</div>
      </Link>
      }
    </Card.Body>
  </Card>
}

export default DonutCard;