import DonutCard from '../../components/donutCard/donutCard';

const DonutsPage =({donuts}) => {
  return (
      <div className='my-background'>
        {!donuts.length ? <h1>Пончики не найдены</h1>:
          <div className="d-flex justify-content-center flex-wrap mt-3">
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

export default DonutsPage;