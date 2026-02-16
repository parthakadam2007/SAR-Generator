import React from 'react';
const CircularLoader: React.FC = () => {
  return (
    <div className="flex items-center justify-center  ">
      <div
        className="w-12 h-12 rounded-full border-4 border-transparent animate-spin"
        style={{ borderTopColor: 'rgb(43, 127, 255)' }}
      ></div>
    </div>
  );
};

export default CircularLoader;
