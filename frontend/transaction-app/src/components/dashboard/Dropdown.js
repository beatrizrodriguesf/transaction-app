import React, { useState} from 'react';
import './Dashboard.css';

function DropdownButton({ name, options, onOptionSelect }) {
  const [isOpen, setIsOpen] = useState(false);

  const toggleDropdown = () => {
    setIsOpen(!isOpen);
  };
  
  const handleOptionClick = (option) => {
    onOptionSelect(option);
  };

  return (
    <div>
      <button className = "dropdown" onClick={toggleDropdown}>
        {name} {isOpen ? "▲" : "▼"}
      </button>
      {isOpen && (
        <ul>
            {options.map((option, index) => (
                <li key={index} style={{ cursor: "pointer" }} onClick={() => handleOptionClick(option.name)}>
                {option.name}
                </li>
            ))}
        </ul>
      )}
    </div>
  );
}

export default DropdownButton;