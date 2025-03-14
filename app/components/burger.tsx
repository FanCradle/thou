import React, { useState } from 'react';
import Button from '../components/ui/button';
import ParentComponent from './bholder';

const Burger: React.FC = () => {
  const [account, setAccount] = useState<string | null>(null);
  const [balance, setBalance] = useState<number>(0);


  return (
    <nav className="bg-gray-800">
      <div className="container mx-auto px-6 py-3 md:flex md:justify-between md:items-center">
        <div className="flex items-center justify-between">
          <div className="text-white font-bold text-2xl">Crypto 💜💜</div>
          <div className="md:hidden">
            <button
              type="button"
              className="text-gray-500 hover:text-white focus:outline-none focus:text-white"
            >
              <svg className="h-6 w-6 fill-current" viewBox="0 0 24 24">
                <path
                  fillRule="evenodd"
                  clipRule="evenodd"
                  d="M3 5h18v2H3V5zm0 6h18v2H3v-2zm0 6h18v2H3v-2z"
                ></path>
              </svg>
            </button>
          </div>
        </div>
        <div className="md:flex items-center justify-between space-x-4">

          <Button onClick={() => console.log('Button clicked')} text="Click me" />
          {/* Render ParentComponent as a component, no need for props if not needed */}
          <ParentComponent />
        
        </div>
      </div>
    </nav>
  );
};

export default Burger;
