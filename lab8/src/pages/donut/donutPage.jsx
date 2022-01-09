import {useParams} from "react-router-dom";
import { Link } from "react-router-dom";
import DonutCard from '../../components/donutCard/donutCard';

const DonutPage = ({donuts}) => {
  const {donutId} = useParams();
  const donut = donuts.find((d) => d.pk + '' === donutId)

  return (
    <div className='my-background'>
      <div className="d-flex justify-content-center mt-3 flex-column align-items-center">
        <DonutCard donutLoad={donut} isDonutPage={true}/>
        <Link to="/">
          <div className="btn my-btn" href='/'>Перейти на главную страницу</div>
        </Link>
      </div>
    </div>
  );
}

export default DonutPage;