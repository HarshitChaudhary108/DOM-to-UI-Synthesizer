"use client";
import { useState } from 'react';

export default function Navbar() {
  const [open, setOpen] = useState(false);
  return (
    <nav className="sticky top-0 bg-[#080625] text-[#FFFFFF] font-[Inter,sans-serif] z-10">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between h-16">
        <div className="flex-shrink-0 text-xl font-bold">SOULSTARR</div>
        <div className="hidden md:flex space-x-6">
          <a href="#" className="hover:underline">Home</a>
          <a href="#" className="hover:underline">Love &amp; Relationships</a>
          <a href="#" className="hover:underline">Past Life</a>
          <a href="#" className="hover:underline">Dream Meaning</a>
          <a href="#" className="hover:underline">Angel Numbers</a>
        </div>
        <button
          className="md:hidden focus:outline-none"
          onClick={() => setOpen(!open)}
          aria-label="Toggle menu"
        >
          <svg className="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            {open ? (
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            ) : (
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
            )}
          </svg>
        </button>
      </div>
      {open && (
        <div className="md:hidden bg-[#080625] px-2 pt-2 pb-3 space-y-1">
          <a href="#" className="block px-3 py-2 rounded-md text-base font-medium hover:bg-[#1a1a3a]">Home</a>
          <a href="#" className="block px-3 py-2 rounded-md text-base font-medium hover:bg-[#1a1a3a]">Love &amp; Relationships</a>
          <a href="#" className="block px-3 py-2 rounded-md text-base font-medium hover:bg-[#1a1a3a]">Past Life</a>
          <a href="#" className="block px-3 py-2 rounded-md text-base font-medium hover:bg-[#1a1a3a]">Dream Meaning</a>
          <a href="#" className="block px-3 py-2 rounded-md text-base font-medium hover:bg-[#1a1a3a]">Angel Numbers</a>
        </div>
      )}
    </nav>
  );
}
