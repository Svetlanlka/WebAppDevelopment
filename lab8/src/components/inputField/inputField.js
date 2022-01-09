import {Button} from "react-bootstrap";
import React from "react";

const InputField = ({ value, setValue, onSubmit, loading, placeholder, buttonTitle = 'Поиск'}) => {
    return <div className="input-field mb-3 d-flex">
        <input className="form-control" value={value} placeholder={placeholder} onChange={(event => setValue(event.target.value))}/>
        <div className="input-group-append">
          <Button className="my-btn" disabled={loading} onClick={onSubmit}>{buttonTitle}</Button>
        </div>
    </div>
}

export default InputField