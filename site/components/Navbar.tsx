"use client";

import { useState } from "react";

export default function Navbar() {
  const [open, setOpen] = useState(false);
  const menuItems = [
    "Home",
    "Love & Relationships",
    "Past Life",
    "Dream Meaning",
    "Angel Numbers",
  ];
  return (
    <nav className="fixed top-0 left-0 w-full bg-[#080625]/80 backdrop-blur-sm text-[#ffffff] font-[Inter,ui-serif] z-50">
      <div className="max-w-7xl mx-auto flex items-center justify-between p-4">
        <div className="text-xl font-bold">SOULSTARR</div>
        <div className="hidden sm:flex space-x-6">
          {menuItems.map((item) => (
            <a href="#" key={item} className="hover:text-[#9d3f3f] transition-colors">
              {item}
            </a>
          ))}
        </div>
        <button
          className="sm:hidden focus:outline-none"
          onClick={() => setOpen(!open)}
          aria-label="Toggle menu"
        >
          <svg
            className="w-6 h-6"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
          >
            {open ? (
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            ) : (
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
            )}
          </svg>
        </button>
      </div>
      {open && (
        <div className="sm:hidden bg-[#080625] text-[#ffffff] pb-4">
          {menuItems.map((item) => (
            <a href="#" key={item} className="block px-4 py-2 hover:bg-[#9d3f3f]/20">
              {item}
            </a>
          ))}
        </div>
      )}
    </nav>
  );
}
