import React, {useState, useEffect} from 'react';
import axios from 'axios';

import './Form.css';

const REACT_APP_API_URL = process.env.REACT_APP_API_URL;
const REACT_APP_API_BASE = process.env.REACT_APP_API_BASE;
const API_URL = `${REACT_APP_API_URL}${REACT_APP_API_BASE}`;

function MyForm() {
    const [number1, setNumber1] = useState('');
    const [number2, setNumber2] = useState('');
    const [dropdownOptions, setDropdownOptions] = useState([]);
    const [selectedOption, setSelectedOption] = useState('');
    const [result, setResult] = useState('');

    useEffect(() => {
        // Replace with your API endpoint
        axios.get(`${API_URL}/operations`).then(response => {
            const options = response.data.result.map(operator => ({
                value: operator,
                label: operator  // Assuming you want the label to be the same as the value
            }));
            setDropdownOptions(options);

            if (options.length > 0) {
                setSelectedOption(options[0].value);
            }
        });
    }, []);

    // Handle form submission
    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            const response = await axios.post(`${API_URL}/calculate`, {
                "operands": [
                    number1,
                    number2,
                ],
                "operator": selectedOption
            });
            let result1 = Number(response.data.result);
            if (result1) {
                setResult(result1.toFixed(2)); // Assuming the API returns an object with a 'result' field
            }
        } catch (error) {
            console.error('Error submitting form', error);
        }
    };

    return (
        <form onSubmit={handleSubmit} className="myForm">
            <input
                type="text"
                value={number1}
                onChange={(e) => setNumber1(e.target.value)}
                placeholder="Input A"
            />
            <select
                value={selectedOption}
                onChange={(e) => setSelectedOption(e.target.value)}
            >
                {dropdownOptions.map(option => (
                    <option key={option.value} value={option.value}>
                        {option.label}
                    </option>
                ))}
            </select>
            <input
                type="text"
                value={number2}
                onChange={(e) => setNumber2(e.target.value)}
                placeholder="Input B"
            />
            <button type="submit">=</button>
            <div className="result">
                {result}
            </div>
        </form>
    );
}

export default MyForm;